import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { Header } from "@/components/Header";
import { api } from "@/lib/api";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { toast } from "sonner";
import {
  ArrowLeft,
  BookmarkSimple,
  MicrosoftExcelLogo,
  Table
} from "@phosphor-icons/react";

function renderMarkdown(md) {
  if (!md) return "";
  let html = md;
  html = html.replace(/```([a-z]*)\n([\s\S]*?)```/g, (_, lang, code) =>
    `<pre><code>${code.replace(/[<>&]/g, c => ({"<":"&lt;",">":"&gt;","&":"&amp;"}[c]))}</code></pre>`);
  html = html.replace(/^### (.*)$/gm, "<h3>$1</h3>");
  html = html.replace(/^## (.*)$/gm, "<h2>$1</h2>");
  html = html.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  html = html.replace(/`([^`]+)`/g, "<code>$1</code>");
  html = html.replace(/((?:^\|.*\|\s*\n)+)/gm, (block) => {
    const rows = block.trim().split("\n");
    if (rows.length < 2) return block;
    const headerCells = rows[0].split("|").slice(1, -1).map(c => `<th>${c.trim()}</th>`).join("");
    const bodyRows = rows.slice(2).map(r => {
      const cells = r.split("|").slice(1, -1).map(c => `<td>${c.trim()}</td>`).join("");
      return `<tr>${cells}</tr>`;
    }).join("");
    return `<table><thead><tr>${headerCells}</tr></thead><tbody>${bodyRows}</tbody></table>`;
  });
  html = html.replace(/(?:^- .*(?:\n|$))+/gm, (block) => {
    const items = block.trim().split("\n").map(l => `<li>${l.replace(/^- /, "")}</li>`).join("");
    return `<ul>${items}</ul>`;
  });
  html = html.replace(/(?:^\d+\. .*(?:\n|$))+/gm, (block) => {
    const items = block.trim().split("\n").map(l => `<li>${l.replace(/^\d+\. /, "")}</li>`).join("");
    return `<ol>${items}</ol>`;
  });
  html = html.split(/\n{2,}/).map(chunk =>
    /^<(h\d|ul|ol|pre|table)/.test(chunk.trim()) ? chunk : `<p>${chunk.replace(/\n/g, " ")}</p>`
  ).join("\n");
  return html;
}

export default function TutorialDetail() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [tut, setTut] = useState(null);
  const [loading, setLoading] = useState(true);
  const [bookmarked, setBookmarked] = useState(false);
  const [bookmarkLoading, setBookmarkLoading] = useState(false);

  useEffect(() => {
    api.get(`/tutorials/${id}`).then((r) => setTut(r.data)).finally(() => setLoading(false));
    api.get("/bookmarks").then((r) => {
      setBookmarked(r.data.some((b) => b.item_id === id));
    }).catch(() => {});
  }, [id]);

  const toggleBookmark = async () => {
    if (bookmarkLoading) return;
    setBookmarkLoading(true);
    try {
      if (bookmarked) {
        await api.delete(`/bookmarks/${id}`);
        setBookmarked(false);
        toast("Bookmark removed");
      } else {
        await api.post("/bookmarks", { item_type: "tutorial", item_id: id });
        setBookmarked(true);
        toast.success("Bookmarked!");
      }
    } catch {
      toast.error("Could not update bookmark");
    } finally {
      setBookmarkLoading(false);
    }
  };

  if (loading) return (
    <div className="min-h-screen excel-bg dark:text-white"><Header />
      <div className="max-w-[1100px] mx-auto px-6 lg:px-10 py-12 overline text-slate-500 dark:text-slate-400">Loading...</div>
    </div>
  );

  if (!tut) return (
    <div className="min-h-screen excel-bg dark:text-white"><Header />
      <div className="max-w-[1100px] mx-auto px-6 lg:px-10 py-12 text-gray-950 dark:text-white">Tutorial not found.</div>
    </div>
  );

  return (
    <div className="min-h-screen excel-bg dark:text-white">
      <Header />
      <main className="max-w-[860px] mx-auto px-6 lg:px-10 py-10 lg:py-14" data-testid="tutorial-detail-page">
        <button onClick={() => navigate(-1)} className="overline mb-6 flex items-center gap-2 text-slate-600 hover:klein dark:text-slate-400" data-testid="back-button">
          <ArrowLeft size={14} /> BACK
        </button>

        <article className="bg-white/95 dark:bg-slate-950/90 border border-foreground/10 p-6 lg:p-8 shadow-sm">
          <div className="flex items-center justify-between gap-4 mb-4">
            <div className="flex gap-2">
              <Badge variant="outline" className="rounded-none border-foreground/20 bg-white dark:bg-gray-900 dark:text-slate-200">{tut.category}</Badge>
              {tut.level && <Badge className="rounded-none bg-klein text-white">{tut.level}</Badge>}
            </div>
            <Button
              variant="outline"
              size="sm"
              onClick={toggleBookmark}
              disabled={bookmarkLoading}
              className="rounded-none border-foreground/20 bg-white dark:bg-gray-900 dark:text-white dark:hover:bg-gray-800"
            >
              {bookmarked
                ? <><BookmarkSimple size={15} className="mr-1.5 klein" /> Saved</>
                : <><BookmarkSimple size={15} className="mr-1.5" /> Bookmark</>
              }
            </Button>
          </div>

          <div className="overline text-emerald-700 dark:text-emerald-300/90 mb-3 flex items-center gap-2 tracking-[0.16em]">
            <MicrosoftExcelLogo size={16} weight="fill" />
            Spreadsheet lesson
          </div>
          <h1 className="max-w-3xl page-title mb-4 text-slate-950 dark:text-slate-100">{tut.title}</h1>
          <p className="text-base lg:text-[1.0625rem] text-slate-600 dark:text-slate-300 leading-7 mb-8 border-l-2 border-blue-600 pl-4">{tut.summary}</p>
          <div className="mb-10 grid grid-cols-4 border-l border-t border-emerald-700/15 dark:border-emerald-400/15 text-xs font-mono text-slate-500 dark:text-slate-400">
            {["A", "B", "C", "fx"].map((cell) => (
              <div key={cell} className="border-r border-b border-emerald-700/15 dark:border-emerald-400/15 bg-emerald-50/60 dark:bg-emerald-950/10 px-3 py-2 flex items-center gap-2">
                {cell === "fx" && <Table size={14} />}
                {cell}
              </div>
            ))}
          </div>

          <div className="markdown" dangerouslySetInnerHTML={{ __html: renderMarkdown(tut.content) }} />
        </article>
      </main>
    </div>
  );
}
