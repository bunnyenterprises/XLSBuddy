import React, { useEffect, useState, useCallback } from "react";
import { useParams, useNavigate, Link } from "react-router-dom";
import { Header } from "@/components/Header";
import { VisualExample } from "@/components/VisualExample";
import { api } from "@/lib/api";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { toast } from "sonner";
import { ArrowLeft, ChatCircleDots, Function as FunctionIcon, Copy, Check, BookmarkSimple } from "@phosphor-icons/react";

export default function FunctionDetail() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [func, setFunc] = useState(null);
  const [loading, setLoading] = useState(true);
  const [copiedSyntax, setCopiedSyntax] = useState(false);
  const [copiedExample, setCopiedExample] = useState(false);
  const [bookmarked, setBookmarked] = useState(false);
  const [bookmarkLoading, setBookmarkLoading] = useState(false);

  useEffect(() => {
    api.get(`/functions/${id}`).then((r) => setFunc(r.data)).finally(() => setLoading(false));
    // Load bookmark state
    api.get("/bookmarks").then((r) => {
      const bm = r.data.find((b) => b.item_id === id);
      setBookmarked(!!bm);
    }).catch(() => {});
  }, [id]);

  const copy = useCallback((text, which) => {
    navigator.clipboard.writeText(text).then(() => {
      if (which === "syntax") { setCopiedSyntax(true); setTimeout(() => setCopiedSyntax(false), 2000); }
      else { setCopiedExample(true); setTimeout(() => setCopiedExample(false), 2000); }
      toast.success("Copied to clipboard!");
    });
  }, []);

  const toggleBookmark = async () => {
    if (bookmarkLoading) return;
    setBookmarkLoading(true);
    try {
      if (bookmarked) {
        await api.delete(`/bookmarks/${id}`);
        setBookmarked(false);
        toast("Bookmark removed");
      } else {
        await api.post("/bookmarks", { item_type: "function", item_id: id });
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
    <div className="min-h-screen bg-white dark:bg-gray-950"><Header />
      <div className="max-w-[1400px] mx-auto px-6 lg:px-10 py-12 overline text-muted-foreground">Loading…</div>
    </div>
  );
  if (!func) return (
    <div className="min-h-screen bg-white dark:bg-gray-950"><Header />
      <div className="max-w-[1400px] mx-auto px-6 lg:px-10 py-12">Function not found.</div>
    </div>
  );

  return (
    <div className="min-h-screen bg-white dark:bg-gray-950 dark:text-white">
      <Header />
      <main className="max-w-[1100px] mx-auto px-6 lg:px-10 py-10 lg:py-14" data-testid="function-detail-page">
        <button onClick={() => navigate(-1)} className="overline mb-6 flex items-center gap-2 hover:klein dark:text-gray-400" data-testid="back-button">
          <ArrowLeft size={14} /> BACK
        </button>

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 mb-12">
          <div className="lg:col-span-8">
            <div className="flex items-center gap-3 mb-4">
              <FunctionIcon size={28} className="klein" weight="bold" />
              <Badge variant="outline" className="rounded-none border-foreground/20">{func.category}</Badge>
              <Badge variant="outline" className={`rounded-none text-xs ${
                func.difficulty === "Advanced" ? "border-red-400 text-red-600" :
                func.difficulty === "Intermediate" ? "border-yellow-500 text-yellow-700" :
                "border-green-500 text-green-700"
              }`}>{func.difficulty || "Beginner"}</Badge>
            </div>
            <h1 className="text-5xl lg:text-6xl font-black tracking-tighter mb-4">{func.name}</h1>
            <p className="text-lg text-muted-foreground leading-relaxed">{func.description}</p>
          </div>
          <div className="lg:col-span-4 flex flex-col gap-3">
            <Link to="/chat" data-testid="ask-ai-cta">
              <Button className="w-full rounded-none bg-klein hover:bg-[#002FA7]/90 text-white h-12">
                <ChatCircleDots size={18} className="mr-2" /> Ask AI about {func.name}
              </Button>
            </Link>
            <Button
              variant="outline"
              onClick={toggleBookmark}
              disabled={bookmarkLoading}
              className="w-full rounded-none border-foreground/20 h-12"
              data-testid="bookmark-button"
            >
              {bookmarked
                ? <><BookmarkSimple size={18} className="mr-2 klein" /> Bookmarked</>
                : <><BookmarkSimple size={18} className="mr-2" /> Bookmark</>
              }
            </Button>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-0 border-l border-t border-foreground/15">
          <div className="border-r border-b border-foreground/15 p-8 bg-white dark:bg-gray-900">
            <div className="flex items-center justify-between mb-3">
              <div className="overline klein">// SYNTAX</div>
              <button
                onClick={() => copy(func.syntax, "syntax")}
                className="flex items-center gap-1.5 text-xs font-medium text-muted-foreground hover:text-foreground border border-foreground/15 px-2 py-1 transition-colors"
                data-testid="copy-syntax"
              >
                {copiedSyntax ? <><Check size={13} className="text-green-600" /> Copied</> : <><Copy size={13} /> Copy</>}
              </button>
            </div>
            <pre className="text-sm bg-black text-white p-4 overflow-x-auto"><code>{func.syntax}</code></pre>
          </div>
          <div className="border-r border-b border-foreground/15 p-8 bg-secondary dark:bg-gray-800">
            <div className="flex items-center justify-between mb-3">
              <div className="overline klein">// EXAMPLE</div>
              <button
                onClick={() => copy(func.example, "example")}
                className="flex items-center gap-1.5 text-xs font-medium text-muted-foreground hover:text-foreground border border-foreground/15 px-2 py-1 transition-colors"
                data-testid="copy-example"
              >
                {copiedExample ? <><Check size={13} className="text-green-600" /> Copied</> : <><Copy size={13} /> Copy</>}
              </button>
            </div>
            <pre className="text-sm bg-black text-white p-4 overflow-x-auto"><code>{func.example}</code></pre>
          </div>
          <div className="md:col-span-2 border-r border-b border-foreground/15 p-8 bg-white dark:bg-gray-900">
            <div className="overline klein mb-3">// USE CASE</div>
            <p className="text-base leading-relaxed">{func.use_case}</p>
          </div>
        </div>

        {func.visual_example && (
          <section className="mt-12" data-testid="visual-example-section">
            <div className="overline klein mb-3">// SEE IT IN ACTION</div>
            <h2 className="text-2xl lg:text-3xl font-black tracking-tighter mb-2">Mini Excel sheet preview</h2>
            <p className="text-muted-foreground mb-6 max-w-2xl">
              Here's a tiny dataset showing how <span className="font-bold klein">{func.name}</span> works in practice.
            </p>
            <VisualExample example={func.visual_example} />
          </section>
        )}
      </main>
    </div>
  );
}
