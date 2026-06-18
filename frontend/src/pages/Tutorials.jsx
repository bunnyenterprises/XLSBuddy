import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { Header } from "@/components/Header";
import { api } from "@/lib/api";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";
import { MagnifyingGlass, BookOpen, ArrowRight } from "@phosphor-icons/react";

export default function Tutorials() {
  const navigate = useNavigate();
  const [tuts, setTuts] = useState([]);
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get("/tutorials").then((r) => setTuts(r.data)).finally(() => setLoading(false));
  }, []);

  const filtered = tuts.filter((t) => {
    const s = search.trim().toLowerCase();
    return !s || t.title.toLowerCase().includes(s) || t.summary.toLowerCase().includes(s) || t.category.toLowerCase().includes(s);
  });

  return (
    <div className="min-h-screen bg-white">
      <Header />
      <main className="max-w-[1400px] mx-auto px-6 lg:px-10 py-10 lg:py-14" data-testid="tutorials-page">
        <div className="overline klein mb-3">// TUTORIALS</div>
        <h1 className="text-4xl lg:text-5xl font-black tracking-tighter mb-3">Excel, level by level.</h1>
        <p className="text-muted-foreground max-w-2xl mb-8">
          Curated guides on the things that actually slow you down.
        </p>

        <div className="relative mb-8 max-w-2xl">
          <MagnifyingGlass size={18} className="absolute left-4 top-1/2 -translate-y-1/2 text-muted-foreground" />
          <Input
            data-testid="tutorials-search-input"
            placeholder="Search tutorials…"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="rounded-none border-foreground/30 h-12 pl-12 text-base"
          />
        </div>

        {loading ? (
          <div className="overline text-muted-foreground">Loading tutorials…</div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-0 border-l border-t border-foreground/15">
            {filtered.map((t, i) => (
              <button
                key={t.id}
                onClick={() => navigate(`/tutorials/${t.id}`)}
                data-testid={`tutorial-card-${i}`}
                className="text-left border-r border-b border-foreground/15 p-8 bg-white hover:bg-secondary lift group relative"
              >
                <div className="flex items-center justify-between mb-4">
                  <BookOpen size={32} className="klein" weight="duotone" />
                  <div className="flex gap-2">
                    <Badge variant="outline" className="rounded-none border-foreground/20 text-xs">{t.category}</Badge>
                    <Badge className="rounded-none bg-klein text-xs">{t.level}</Badge>
                  </div>
                </div>
                <h3 className="text-2xl font-bold tracking-tight mb-2 group-hover:klein transition-colors">{t.title}</h3>
                <p className="text-sm text-muted-foreground leading-relaxed mb-4">{t.summary}</p>
                <div className="overline flex items-center gap-2 klein">
                  READ <ArrowRight size={14} weight="bold" />
                </div>
              </button>
            ))}
          </div>
        )}
      </main>
    </div>
  );
}
