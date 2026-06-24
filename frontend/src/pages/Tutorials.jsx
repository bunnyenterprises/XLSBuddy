import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { Header } from "@/components/Header";
import { api } from "@/lib/api";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";
import { MagnifyingGlass, BookOpen, ArrowRight, MicrosoftExcelLogo, Table } from "@phosphor-icons/react";

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
    <div className="min-h-screen excel-bg dark:text-white">
      <Header />
      <main className="max-w-[1400px] mx-auto px-6 lg:px-10 py-10 lg:py-14" data-testid="tutorials-page">
        <div className="mb-8">
          <div className="overline klein mb-3 flex items-center gap-2">
            <MicrosoftExcelLogo size={15} weight="fill" />
            Excel Tutorials
          </div>
          <h1 className="page-title mb-3 text-slate-950 dark:text-slate-100">
            Excel, level by level.
          </h1>
          <p className="text-sm lg:text-base text-slate-600 dark:text-slate-300 max-w-2xl">
            Curated guides for formulas, lookups, pivot tables, errors, and everyday spreadsheet work.
          </p>
        </div>

        <div className="relative mb-8 max-w-2xl">
          <MagnifyingGlass size={18} className="absolute left-4 top-1/2 -translate-y-1/2 text-slate-500 dark:text-slate-400" />
          <Input
            data-testid="tutorials-search-input"
            placeholder="Search tutorials..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="rounded-none border-foreground/30 bg-white/90 dark:bg-gray-900 dark:text-white dark:placeholder:text-slate-500 h-12 pl-12 text-base"
          />
        </div>

        {loading ? (
          <div className="overline text-slate-500 dark:text-slate-400">Loading tutorials...</div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-0 border-l border-t border-foreground/15">
            {filtered.map((t, i) => (
              <button
                key={t.id}
                onClick={() => navigate(`/tutorials/${t.id}`)}
                data-testid={`tutorial-card-${i}`}
                className="text-left border-r border-b border-foreground/15 p-8 bg-white/95 dark:bg-gray-900/95 hover:bg-emerald-50 dark:hover:bg-gray-800 lift group relative"
              >
                <div className="flex items-center justify-between gap-4 mb-4">
                  <div className="flex items-center gap-3">
                    <div className="h-10 w-10 flex items-center justify-center bg-emerald-600 text-white">
                      {i % 2 === 0 ? <Table size={22} weight="bold" /> : <BookOpen size={22} weight="duotone" />}
                    </div>
                    <BookOpen size={26} className="klein" weight="duotone" />
                  </div>
                  <div className="flex flex-wrap justify-end gap-2">
                    <Badge variant="outline" className="rounded-none border-foreground/20 bg-white dark:bg-gray-950 dark:text-slate-200 text-xs">{t.category}</Badge>
                    <Badge className="rounded-none bg-klein text-white text-xs">{t.level}</Badge>
                  </div>
                </div>
                <h3 className="section-title mb-2 text-gray-950 dark:text-slate-100 group-hover:klein transition-colors">{t.title}</h3>
                <p className="text-sm text-slate-600 dark:text-slate-300 leading-relaxed mb-4">{t.summary}</p>
                <div className="overline flex items-center gap-2 text-emerald-700 dark:text-emerald-400">
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
