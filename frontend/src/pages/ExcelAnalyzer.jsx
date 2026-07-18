import React, { useState, useRef, useCallback } from "react";
import * as XLSX from "xlsx";
import { Header } from "@/components/Header";
import { api } from "@/lib/api";
import { toast } from "sonner";
import {
  UploadSimple, Sparkle, X, ArrowRight, FileXls, Table,
  ChatCircleDots, PencilSimple, DownloadSimple, MagicWand,
} from "@phosphor-icons/react";

// ─── HELPERS ──────────────────────────────────────────────────────────────────

function parseFile(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = (e) => {
      try {
        const wb = XLSX.read(e.target.result, { type: "array" });
        const sheets = {};
        wb.SheetNames.forEach((name) => {
          const ws = wb.Sheets[name];
          const data = XLSX.utils.sheet_to_json(ws, { header: 1, defval: "" });
          sheets[name] = data;
        });
        resolve({ sheetNames: wb.SheetNames, sheets });
      } catch (err) {
        reject(err);
      }
    };
    reader.onerror = reject;
    reader.readAsArrayBuffer(file);
  });
}

function buildContext(sheetData, sheetName, maxRows = 60) {
  if (!sheetData || sheetData.length === 0) return "";
  const headers = sheetData[0];
  const rows = sheetData.slice(1, maxRows + 1);
  const totalRows = sheetData.length - 1;
  let ctx = `Sheet: "${sheetName}" | ${headers.length} columns | ${totalRows} rows total\n\n`;
  ctx += "COLUMNS: " + headers.join(" | ") + "\n\n";
  ctx += "DATA (first " + Math.min(rows.length, maxRows) + " rows):\n";
  rows.forEach((row, i) => {
    ctx += `Row ${i + 1}: ` + row.join(" | ") + "\n";
  });
  return ctx;
}

// Convert 2D array to CSV string
function arrayToCSV(data) {
  return data.map(row =>
    row.map(cell => {
      const s = String(cell ?? "");
      return s.includes(",") || s.includes('"') || s.includes("\n")
        ? `"${s.replace(/"/g, '""')}"`
        : s;
    }).join(",")
  ).join("\n");
}

// Parse CSV string back to 2D array
function csvToArray(csv) {
  const rows = [];
  const lines = csv.split("\n");
  for (const line of lines) {
    if (!line.trim()) continue;
    const row = [];
    let cur = "";
    let inQuotes = false;
    for (let i = 0; i < line.length; i++) {
      const ch = line[i];
      if (ch === '"') {
        if (inQuotes && line[i + 1] === '"') { cur += '"'; i++; }
        else { inQuotes = !inQuotes; }
      } else if (ch === "," && !inQuotes) {
        row.push(cur); cur = "";
      } else {
        cur += ch;
      }
    }
    row.push(cur);
    rows.push(row);
  }
  return rows;
}

// ─── SPREADSHEET TABLE ────────────────────────────────────────────────────────

function SpreadsheetTable({ data }) {
  if (!data || data.length === 0) return (
    <div className="flex-1 flex items-center justify-center text-slate-400 text-sm">No data in this sheet.</div>
  );

  const headers = data[0] || [];
  const rows = data.slice(1);
  const cols = ["", ...headers.map((_, i) => String.fromCharCode(65 + (i % 26)))];

  return (
    <div className="flex-1 overflow-auto border border-[#bfbfbf]" style={{ fontFamily: "'Segoe UI', system-ui, sans-serif", fontSize: "12px" }}>
      <table className="border-collapse" style={{ minWidth: "100%" }}>
        <thead>
          <tr>
            {cols.map((c, ci) => (
              <th key={ci} className={`border border-[#d0d0d0] px-3 py-1.5 text-center font-semibold whitespace-nowrap sticky top-0 z-10 ${ci === 0 ? "w-10 bg-[#f0efee] text-[#5a5a5a]" : "bg-[#dce6f1] text-[#1f3864] min-w-[90px]"}`}>
                {c || ""}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          <tr>
            <td className="border border-[#d0d0d0] bg-[#d6e8d6] text-center text-[#1a5e38] font-bold px-2 py-1 sticky left-0">1</td>
            {headers.map((h, ci) => (
              <td key={ci} className="border border-[#bfc9d6] bg-[#dce6f1] px-3 py-1.5 font-bold text-[#1f3864] whitespace-nowrap">
                {String(h)}
              </td>
            ))}
          </tr>
          {rows.map((row, ri) => (
            <tr key={ri} className={ri % 2 === 0 ? "bg-white" : "bg-[#f9f9ff]"}>
              <td className="border border-[#d0d0d0] bg-[#f0efee] text-center text-[#5a5a5a] px-2 py-1 sticky left-0 font-medium">{ri + 2}</td>
              {headers.map((_, ci) => (
                <td key={ci} className="border border-[#e0e0e0] px-3 py-1.5 text-[#252423] whitespace-nowrap max-w-[200px] overflow-hidden text-ellipsis">
                  {String(row[ci] ?? "")}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

// ─── MAIN PAGE ────────────────────────────────────────────────────────────────

export default function ExcelAnalyzer() {
  const [file, setFile] = useState(null);
  const [workbook, setWorkbook] = useState(null);
  const [activeSheet, setActiveSheet] = useState(null);
  const [parsing, setParsing] = useState(false);
  const [dragging, setDragging] = useState(false);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [aiLoading, setAiLoading] = useState(false);
  const [mode, setMode] = useState("analyze"); // "analyze" | "edit"
  const [hasEdits, setHasEdits] = useState(false);
  const [originalFileName, setOriginalFileName] = useState("");
  const fileRef = useRef(null);
  const chatEndRef = useRef(null);

  const handleFile = useCallback(async (f) => {
    if (!f) return;
    const ext = f.name.split(".").pop().toLowerCase();
    if (!["xlsx", "xls", "csv"].includes(ext)) {
      toast.error("Please upload an .xlsx, .xls, or .csv file");
      return;
    }
    setParsing(true);
    try {
      const wb = await parseFile(f);
      setFile(f);
      setOriginalFileName(f.name);
      setWorkbook(wb);
      setActiveSheet(wb.sheetNames[0]);
      setHasEdits(false);
      setMessages([{
        role: "assistant",
        text: `✅ **${f.name}** loaded — ${wb.sheetNames.length} sheet(s), ${wb.sheets[wb.sheetNames[0]].length - 1} rows in "${wb.sheetNames[0]}".\n\nUse **Ask AI** to analyze your data, or switch to **Edit with AI** to modify it.`,
      }]);
    } catch {
      toast.error("Could not read file. Make sure it's a valid Excel or CSV.");
    } finally {
      setParsing(false);
    }
  }, []);

  const onDrop = useCallback((e) => {
    e.preventDefault();
    setDragging(false);
    handleFile(e.dataTransfer.files[0]);
  }, [handleFile]);

  const sendMessage = async () => {
    if (!input.trim() || aiLoading || !workbook) return;
    const q = input.trim();
    setInput("");
    setMessages(prev => [...prev, { role: "user", text: q }]);
    setAiLoading(true);
    setTimeout(() => chatEndRef.current?.scrollIntoView({ behavior: "smooth" }), 50);

    const sheetData = workbook.sheets[activeSheet] || [];

    if (mode === "edit") {
      // Send full data as CSV for editing
      const csvData = arrayToCSV(sheetData);
      try {
        const { data } = await api.post("/excel/edit", {
          instruction: q,
          csv_data: csvData,
          sheet_name: activeSheet,
        });

        const newData = csvToArray(data.modified_csv);
        if (newData.length > 0) {
          // Apply changes to workbook
          setWorkbook(prev => ({
            ...prev,
            sheets: { ...prev.sheets, [activeSheet]: newData },
          }));
          setHasEdits(true);
          setMessages(prev => [...prev, {
            role: "assistant",
            text: `✅ Done! ${data.explanation}\n\nThe table above has been updated. Click **Download modified file** when ready.`,
            isEdit: true,
          }]);
        } else {
          setMessages(prev => [...prev, { role: "assistant", text: "Could not apply changes. Please try rephrasing your instruction." }]);
        }
      } catch (e) {
        setMessages(prev => [...prev, { role: "assistant", text: e.response?.data?.detail || "Error applying edit. Please try again." }]);
      }
    } else {
      // Analyze mode
      const context = buildContext(sheetData, activeSheet);
      try {
        const { data } = await api.post("/excel/analyze", { question: q, context });
        setMessages(prev => [...prev, { role: "assistant", text: data.reply || "I couldn't analyze that. Try rephrasing." }]);
      } catch {
        setMessages(prev => [...prev, { role: "assistant", text: "Error connecting to AI. Please try again." }]);
      }
    }

    setAiLoading(false);
    setTimeout(() => chatEndRef.current?.scrollIntoView({ behavior: "smooth" }), 50);
  };

  const downloadModified = () => {
    if (!workbook) return;
    const wb = XLSX.utils.book_new();
    workbook.sheetNames.forEach((name) => {
      const ws = XLSX.utils.aoa_to_sheet(workbook.sheets[name]);
      XLSX.utils.book_append_sheet(wb, ws, name);
    });
    const base = originalFileName.replace(/\.[^.]+$/, "");
    XLSX.writeFile(wb, `${base}_modified.xlsx`);
    toast.success("File downloaded!");
  };

  const reset = () => {
    setFile(null);
    setWorkbook(null);
    setActiveSheet(null);
    setMessages([]);
    setInput("");
    setHasEdits(false);
    setMode("analyze");
  };

  const currentData = workbook?.sheets[activeSheet] || [];
  const rowCount = currentData.length > 0 ? currentData.length - 1 : 0;
  const colCount = currentData[0]?.length || 0;

  return (
    <div className="min-h-screen flex flex-col bg-slate-50 dark:bg-slate-950 dark:text-white">
      <Header />

      <main className="flex-1 flex flex-col max-w-[1400px] w-full mx-auto px-4 lg:px-8 py-6 gap-4">

        {/* Page header */}
        <div className="flex items-center justify-between flex-wrap gap-3">
          <div>
            <div className="text-[10px] font-bold tracking-[0.2em] text-[#002FA7] mb-1">EXCEL ANALYZER</div>
            <h1 className="text-2xl font-extrabold tracking-tight dark:text-white">Upload & Work with Your Spreadsheet</h1>
            <p className="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Analyze data or let AI make changes — then download the result</p>
          </div>
          <div className="flex items-center gap-2">
            {hasEdits && (
              <button
                onClick={downloadModified}
                className="flex items-center gap-2 bg-[#217346] text-white px-4 py-2 text-sm font-bold hover:bg-[#1a5e38] transition-colors"
              >
                <DownloadSimple size={16} weight="bold" /> Download modified file
              </button>
            )}
            {file && (
              <button onClick={reset} className="flex items-center gap-2 border border-foreground/20 px-4 py-2 text-sm font-semibold text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors">
                <X size={14} /> Upload new file
              </button>
            )}
          </div>
        </div>

        {/* Upload zone */}
        {!file && (
          <div
            onDragOver={(e) => { e.preventDefault(); setDragging(true); }}
            onDragLeave={() => setDragging(false)}
            onDrop={onDrop}
            onClick={() => fileRef.current?.click()}
            className={`border-2 border-dashed rounded-none cursor-pointer transition-all flex flex-col items-center justify-center py-20 px-6 text-center ${dragging ? "border-[#002FA7] bg-[#002FA7]/5" : "border-foreground/20 hover:border-[#002FA7]/40 hover:bg-slate-100/50 dark:hover:bg-slate-900/50"}`}
          >
            <input ref={fileRef} type="file" accept=".xlsx,.xls,.csv" className="hidden" onChange={(e) => handleFile(e.target.files[0])} />
            {parsing ? (
              <div className="flex flex-col items-center gap-3">
                <div className="w-10 h-10 border-4 border-[#002FA7] border-t-transparent rounded-full animate-spin" />
                <p className="text-sm font-semibold text-slate-600 dark:text-slate-300">Reading your file…</p>
              </div>
            ) : (
              <>
                <div className="w-16 h-16 bg-[#002FA7]/10 dark:bg-[#002FA7]/20 flex items-center justify-center mb-5">
                  <FileXls size={36} className="text-[#002FA7]" weight="fill" />
                </div>
                <p className="text-lg font-extrabold text-slate-800 dark:text-white mb-1">
                  {dragging ? "Drop it here!" : "Drop your Excel file here"}
                </p>
                <p className="text-sm text-slate-500 dark:text-slate-400 mb-5">or click to browse · supports .xlsx, .xls, .csv</p>
                <button className="bg-[#002FA7] text-white px-6 py-2.5 text-sm font-bold hover:bg-[#002FA7]/90 transition-colors flex items-center gap-2">
                  <UploadSimple size={16} weight="bold" /> Choose file
                </button>
                <p className="text-xs text-slate-400 mt-4">Your file is processed locally — nothing is stored on our servers</p>
              </>
            )}
          </div>
        )}

        {/* Main workspace */}
        {file && workbook && (
          <div className="flex flex-col lg:flex-row gap-4 flex-1 min-h-0" style={{ height: "calc(100vh - 240px)" }}>

            {/* Left: Spreadsheet viewer */}
            <div className="flex flex-col flex-1 min-w-0 border border-foreground/10 bg-white dark:bg-slate-900 overflow-hidden">
              <div className="bg-[#217346] px-4 py-2 flex items-center gap-3">
                <FileXls size={16} className="text-white" weight="fill" />
                <span className="text-white text-xs font-semibold truncate">{file.name}</span>
                {hasEdits && (
                  <span className="bg-yellow-400 text-black text-[10px] font-bold px-2 py-0.5 rounded-full ml-1">MODIFIED</span>
                )}
                <div className="ml-auto flex items-center gap-3 text-white/70 text-[11px]">
                  <span className="flex items-center gap-1"><Table size={11} /> {rowCount} rows × {colCount} cols</span>
                </div>
              </div>

              {workbook.sheetNames.length > 1 && (
                <div className="flex border-b border-foreground/10 bg-slate-50 dark:bg-slate-800 overflow-x-auto">
                  {workbook.sheetNames.map((name) => (
                    <button
                      key={name}
                      onClick={() => setActiveSheet(name)}
                      className={`px-4 py-2 text-xs font-semibold border-r border-foreground/10 whitespace-nowrap transition-colors ${activeSheet === name ? "bg-white dark:bg-slate-900 text-[#217346] border-b-2 border-b-[#217346]" : "text-slate-500 hover:bg-white/50 dark:hover:bg-slate-700"}`}
                    >
                      {name}
                    </button>
                  ))}
                </div>
              )}

              <SpreadsheetTable data={currentData} />

              <div className="bg-[#217346] px-4 py-1 text-[10px] text-white/70 flex items-center gap-4">
                <span>Sheet: {activeSheet}</span>
                <span>·</span>
                <span>{rowCount} rows</span>
                <span>·</span>
                <span>{colCount} columns</span>
                {rowCount > 60 && mode === "analyze" && <span className="text-yellow-300">· AI analyzes first 60 rows</span>}
              </div>
            </div>

            {/* Right: AI Chat */}
            <div className="flex flex-col w-full lg:w-[400px] shrink-0 border border-foreground/10 bg-white dark:bg-slate-900">

              {/* Mode toggle */}
              <div className="border-b border-foreground/10 p-2 bg-slate-50 dark:bg-slate-800 flex gap-1">
                <button
                  onClick={() => { setMode("analyze"); setInput(""); }}
                  className={`flex-1 flex items-center justify-center gap-2 py-2 text-xs font-bold transition-colors ${mode === "analyze" ? "bg-[#002FA7] text-white" : "text-slate-500 hover:bg-slate-200 dark:hover:bg-slate-700"}`}
                >
                  <ChatCircleDots size={14} weight="fill" /> Ask AI
                </button>
                <button
                  onClick={() => { setMode("edit"); setInput(""); }}
                  className={`flex-1 flex items-center justify-center gap-2 py-2 text-xs font-bold transition-colors ${mode === "edit" ? "bg-[#217346] text-white" : "text-slate-500 hover:bg-slate-200 dark:hover:bg-slate-700"}`}
                >
                  <MagicWand size={14} weight="fill" /> Edit with AI
                </button>
              </div>

              {/* Mode description */}
              <div className={`px-3 py-2 text-[10px] font-medium border-b border-foreground/10 ${mode === "edit" ? "bg-emerald-50 dark:bg-emerald-950/30 text-emerald-700 dark:text-emerald-300" : "bg-blue-50 dark:bg-blue-950/30 text-blue-700 dark:text-blue-300"}`}>
                {mode === "edit"
                  ? "✏️ Edit mode — AI will modify your spreadsheet. Changes are applied live."
                  : "💬 Ask mode — AI will answer questions about your data."}
              </div>

              {/* Messages */}
              <div className="flex-1 overflow-y-auto px-4 py-3 space-y-3 min-h-0">
                {messages.map((m, i) => (
                  <div key={i} className={`flex ${m.role === "user" ? "justify-end" : "justify-start"}`}>
                    {m.role === "assistant" && (
                      <div className={`w-6 h-6 flex items-center justify-center shrink-0 mr-2 mt-0.5 ${m.isEdit ? "bg-[#217346]" : "bg-[#002FA7]"}`}>
                        {m.isEdit ? <PencilSimple size={12} className="text-white" weight="fill" /> : <Sparkle size={12} className="text-white" weight="fill" />}
                      </div>
                    )}
                    <div
                      className={`max-w-[85%] px-3 py-2.5 text-sm leading-6 ${m.role === "user" ? (mode === "edit" ? "bg-[#217346] text-white" : "bg-[#002FA7] text-white") : "bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-slate-100"}`}
                      style={{ whiteSpace: "pre-wrap" }}
                    >
                      {m.text}
                    </div>
                  </div>
                ))}
                {aiLoading && (
                  <div className="flex justify-start">
                    <div className={`w-6 h-6 flex items-center justify-center shrink-0 mr-2 ${mode === "edit" ? "bg-[#217346]" : "bg-[#002FA7]"}`}>
                      <Sparkle size={12} className="text-white" weight="fill" />
                    </div>
                    <div className="bg-slate-100 dark:bg-slate-800 px-4 py-3 flex gap-1 items-center">
                      {[0,1,2].map(i => <span key={i} className="w-2 h-2 bg-slate-400 rounded-full animate-bounce" style={{animationDelay:`${i*0.15}s`}} />)}
                    </div>
                  </div>
                )}
                <div ref={chatEndRef} />
              </div>

              {/* Quick prompts */}
              {messages.length <= 1 && (
                <div className="px-4 pb-2 flex flex-wrap gap-1.5">
                  {mode === "analyze" ? [
                    "Summarize this data",
                    "Find duplicate rows",
                    "What are the totals?",
                    "Which row has max value?",
                    "Suggest a formula",
                  ] : [
                    "Sort by first column A→Z",
                    "Add a Total column",
                    "Remove duplicate rows",
                    "Add a Serial No column",
                    "Fill blank cells with 0",
                  ].map(q => (
                    <button key={q} onClick={() => setInput(q)}
                      className={`text-[10px] font-semibold px-2.5 py-1 border transition-colors ${mode === "edit" ? "border-[#217346]/30 text-[#217346] hover:bg-[#217346]/5 dark:text-emerald-300 dark:border-emerald-700" : "border-[#002FA7]/30 text-[#002FA7] hover:bg-[#002FA7]/5 dark:text-blue-300 dark:border-blue-700"}`}>
                      {q}
                    </button>
                  ))}
                </div>
              )}

              {/* Input */}
              <div className="border-t border-foreground/10 p-3 flex gap-2">
                <input
                  className="flex-1 border border-foreground/20 bg-white dark:bg-slate-800 dark:text-white px-3 py-2 text-sm outline-none focus:border-[#002FA7] transition-colors"
                  placeholder={mode === "edit" ? "Tell AI what to change…" : "Ask anything about your data…"}
                  value={input}
                  onChange={e => setInput(e.target.value)}
                  onKeyDown={e => { if (e.key === "Enter" && !e.shiftKey) sendMessage(); }}
                  disabled={aiLoading}
                />
                <button
                  onClick={sendMessage}
                  disabled={aiLoading || !input.trim()}
                  className={`text-white px-3 py-2 disabled:opacity-40 transition-colors ${mode === "edit" ? "bg-[#217346] hover:bg-[#1a5e38]" : "bg-[#002FA7] hover:bg-[#002FA7]/90"}`}
                >
                  <ArrowRight size={16} weight="bold" />
                </button>
              </div>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}
