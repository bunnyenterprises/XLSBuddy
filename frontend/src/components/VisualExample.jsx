import React from "react";

/**
 * Tries to parse "A1", "A1: label", "A1 (note)", "A1=x" into {col, row}.
 * Returns null if not a recognisable cell reference.
 */
function parseCellRef(str) {
  const s = String(str || "").trim();
  const m = s.match(/^([A-Z]{1,2})(\d+)/);
  if (!m) return null;
  return { col: m[1], row: parseInt(m[2], 10) };
}

function colToIdx(col) { return col.charCodeAt(0) - 65; }
function idxToCol(idx) { return String.fromCharCode(65 + idx); }

/**
 * VisualExample — renders a realistic Excel-style grid preview.
 */
export const VisualExample = ({ example }) => {
  if (!example) return null;
  const { data = [], formula_cell, formula, result } = example;

  // Build cell map from data rows
  const cellMap = {};
  data.forEach(([ref, val]) => {
    const parsed = parseCellRef(String(ref));
    if (parsed) {
      cellMap[`${parsed.col}${parsed.row}`] = String(val);
    }
  });

  // Parse formula cell position
  const fParsed = parseCellRef(formula_cell);

  // Determine grid bounds
  const allParsed = Object.keys(cellMap).map(k => parseCellRef(k)).filter(Boolean);
  if (fParsed) allParsed.push(fParsed);

  if (allParsed.length === 0) {
    return <FallbackTable data={data} formula={formula} formula_cell={formula_cell} result={result} />;
  }

  const maxColIdx = Math.max(...allParsed.map(c => colToIdx(c.col)));
  const minRow = Math.min(...allParsed.map(c => c.row));
  const maxRow = Math.max(...allParsed.map(c => c.row));

  // Always show at least 2 extra columns and 1 extra row for authentic feel
  const cols = Array.from({ length: Math.max(maxColIdx + 2, 3) }, (_, i) => idxToCol(i));
  const rows = Array.from({ length: Math.max(maxRow - minRow + 2, 3) }, (_, i) => i + minRow);

  return (
    <div className="rounded-sm overflow-hidden shadow-lg border border-[#bfbfbf] text-[11px] select-none font-sans">

      {/* ── Title bar ── */}
      <div className="bg-[#217346] px-3 py-1.5 flex items-center gap-2">
        <span className="text-base">📊</span>
        <span className="text-white text-xs font-semibold tracking-wide">Microsoft Excel</span>
        <div className="ml-auto flex gap-1">
          {["─", "□", "✕"].map(s => (
            <span key={s} className="text-white/60 text-xs px-1.5 py-0.5 hover:bg-white/10 cursor-default rounded-sm">{s}</span>
          ))}
        </div>
      </div>

      {/* ── Ribbon tabs ── */}
      <div className="bg-[#f3f2f1] border-b border-[#c8c6c4] px-3 pt-1 flex gap-1 text-[10px]">
        {["Home", "Insert", "Formulas", "Data", "Review", "View"].map(tab => (
          <span key={tab} className={`px-3 py-1 cursor-default rounded-t-sm ${
            tab === "Formulas"
              ? "bg-white border border-b-0 border-[#c8c6c4] text-[#217346] font-semibold"
              : "text-[#605e5c] hover:bg-white/60"
          }`}>{tab}</span>
        ))}
      </div>

      {/* ── Formula bar ── */}
      <div className="bg-white border-b border-[#c8c6c4] flex items-center text-[11px]">
        <div className="border-r border-[#c8c6c4] px-2 py-1 w-14 text-center font-mono text-[#252423] bg-[#f9f9f9]">
          {formula_cell}
        </div>
        <div className="px-2 text-[#217346] font-bold text-sm border-r border-[#c8c6c4] py-1">ƒx</div>
        <div className="flex-1 px-3 py-1 font-mono text-[#0d3880] bg-white">{formula}</div>
      </div>

      {/* ── Spreadsheet grid ── */}
      <div className="overflow-auto bg-white">
        <table className="border-collapse" style={{ minWidth: "100%" }}>
          <thead>
            <tr>
              {/* Corner cell */}
              <th className="w-8 min-w-[32px] bg-[#f0efee] border border-[#d0d0d0] sticky left-0 z-10" />
              {cols.map(col => {
                const isActive = fParsed && col === fParsed.col;
                return (
                  <th key={col} className={`border border-[#d0d0d0] text-center py-0.5 font-medium min-w-[72px] px-2 ${
                    isActive ? "bg-[#d6e8d6] text-[#1a5e38]" : "bg-[#f0efee] text-[#5a5a5a]"
                  }`}>
                    {col}
                  </th>
                );
              })}
            </tr>
          </thead>
          <tbody>
            {rows.map(row => (
              <tr key={row}>
                {/* Row number */}
                <td className={`border border-[#d0d0d0] text-center text-[#5a5a5a] px-1 py-0.5 sticky left-0 z-10 ${
                  fParsed && row === fParsed.row ? "bg-[#d6e8d6] text-[#1a5e38] font-medium" : "bg-[#f0efee]"
                }`}>
                  {row}
                </td>
                {cols.map(col => {
                  const ref = `${col}${row}`;
                  const isFormulaCell = ref === formula_cell;
                  const rawVal = cellMap[ref] ?? "";

                  if (isFormulaCell) {
                    return (
                      <td key={col}
                        className="border-2 border-[#217346] bg-[#e8f5e8] px-2 py-0.5 font-mono font-bold text-[#1a5e38] min-w-[72px]"
                      >
                        {String(result)}
                      </td>
                    );
                  }

                  return (
                    <td key={col}
                      className={`border border-[#d0d0d0] px-2 py-0.5 min-w-[72px] ${
                        rawVal ? "bg-white text-[#252423] font-mono" : "bg-white"
                      }`}
                    >
                      {rawVal}
                    </td>
                  );
                })}
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* ── Status bar ── */}
      <div className="bg-[#217346] px-3 py-0.5 flex items-center justify-between text-white text-[10px]">
        <span className="opacity-80">Ready</span>
        <div className="flex gap-5 opacity-90">
          <span>Average: <strong>{String(result)}</strong></span>
          <span>Count: <strong>{data.length + 1}</strong></span>
          <span>Sum: <strong>{String(result)}</strong></span>
        </div>
      </div>
    </div>
  );
};

/** Fallback for functions whose data rows can't be parsed into cell refs */
function FallbackTable({ data, formula, formula_cell, result }) {
  return (
    <div className="rounded-sm overflow-hidden shadow-lg border border-[#bfbfbf] text-[11px] select-none font-sans">
      <div className="bg-[#217346] px-3 py-1.5 flex items-center gap-2">
        <span className="text-base">📊</span>
        <span className="text-white text-xs font-semibold tracking-wide">Microsoft Excel</span>
      </div>
      <div className="bg-white border-b border-[#c8c6c4] flex items-center text-[11px]">
        <div className="border-r border-[#c8c6c4] px-2 py-1 w-14 text-center font-mono text-[#252423] bg-[#f9f9f9]">{formula_cell}</div>
        <div className="px-2 text-[#217346] font-bold text-sm border-r border-[#c8c6c4] py-1">ƒx</div>
        <div className="flex-1 px-3 py-1 font-mono text-[#0d3880]">{formula}</div>
      </div>
      <div className="overflow-auto bg-white">
        <table className="border-collapse w-full">
          <thead>
            <tr>
              <th className="w-8 bg-[#f0efee] border border-[#d0d0d0]" />
              <th className="bg-[#f0efee] border border-[#d0d0d0] text-center text-[#5a5a5a] font-medium py-0.5 px-6">A</th>
              <th className="bg-[#f0efee] border border-[#d0d0d0] text-center text-[#5a5a5a] font-medium py-0.5 px-6">B</th>
            </tr>
          </thead>
          <tbody>
            {data.map(([label, val], i) => (
              <tr key={i}>
                <td className="bg-[#f0efee] border border-[#d0d0d0] text-center text-[#5a5a5a] px-1">{i + 1}</td>
                <td className="border border-[#d0d0d0] px-2 py-0.5 font-mono text-[#252423]">{String(label)}</td>
                <td className="border border-[#d0d0d0] px-2 py-0.5 font-mono text-[#252423]">{String(val)}</td>
              </tr>
            ))}
            <tr>
              <td className="bg-[#d6e8d6] border border-[#d0d0d0] text-center text-[#1a5e38] font-medium px-1">{data.length + 1}</td>
              <td className="border border-[#d0d0d0] px-2 py-0.5 font-mono text-[#0d3880]">{formula_cell}</td>
              <td className="border-2 border-[#217346] bg-[#e8f5e8] px-2 py-0.5 font-mono font-bold text-[#1a5e38]">{String(result)}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div className="bg-[#217346] px-3 py-0.5 flex items-center justify-between text-white text-[10px]">
        <span className="opacity-80">Ready</span>
        <div className="flex gap-5 opacity-90">
          <span>Result: <strong>{String(result)}</strong></span>
        </div>
      </div>
    </div>
  );
}
