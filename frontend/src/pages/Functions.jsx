import React, { useEffect, useState, useMemo } from "react";
import { useNavigate, useSearchParams } from "react-router-dom";
import { Header } from "@/components/Header";
import { api } from "@/lib/api";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";
import { MagnifyingGlass, Function as FunctionIcon } from "@phosphor-icons/react";

export default function Functions() {
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();
  const [funcs, setFuncs] = useState([]);
  const [categories, setCategories] = useState([]);
  const [activeCat, setActiveCat] = useState("All");
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    Promise.all([
      api.get("/functions/categories"),
      api.get("/functions"),
    ]).then(([cats, fns]) => {
      setCategories(["All", ...cats.data]);
      setFuncs(fns.data);
    }).finally(() => setLoading(false));
  }, []);

  useEffect(() => {
    if (searchParams.get("focus") === "search") {
      const el = document.getElementById("functions-search");
      el?.focus();
    }
  }, [searchParams]);

  const filtered = useMemo(() => {
    return funcs.filter((f) => {
      const catOk = activeCat === "All" || f.category === activeCat;
      const s = search.trim().toLowerCase();
      const sOk = !s || f.name.toLowerCase().includes(s) ||
                       f.description.toLowerCase().includes(s) ||
                       f.use_case.toLowerCase().includes(s);
      return catOk && sOk;
    });
  }, [funcs, activeCat, search]);

  return (
    <div className="min-h-screen bg-white">
      <Header />
      <main className="max-w-[1400px] mx-auto px-6 lg:px-10 py-10 lg:py-14" data-testid="functions-page">
        <div className="overline klein mb-3">// FUNCTIONS LIBRARY</div>
        <h1 className="text-4xl lg:text-5xl font-black tracking-tighter mb-3">All Excel functions.</h1>
        <p className="text-muted-foreground max-w-2xl mb-8">
          Browse by category, search by name or use case. Click any to see syntax, examples, and tips.
        </p>

        {/* Search */}
        <div className="relative mb-6 max-w-2xl">
          <MagnifyingGlass size={18} className="absolute left-4 top-1/2 -translate-y-1/2 text-muted-foreground" />
          <Input
            id="functions-search"
            data-testid="functions-search-input"
            placeholder="Search SUM, VLOOKUP, error, formula…"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="rounded-none border-foreground/30 h-12 pl-12 text-base"
          />
        </div>

        {/* Categories */}
        <div className="flex flex-wrap gap-0 border-l border-t border-foreground/15 mb-8" data-testid="functions-categories">
          {categories.map((c) => (
            <button
              key={c}
              onClick={() => setActiveCat(c)}
              data-testid={`cat-${c.toLowerCase().replace(/[^a-z]/g, '-')}`}
              className={`text-sm font-medium px-5 py-3 border-r border-b border-foreground/15 transition-colors ${
                activeCat === c ? "bg-klein text-white" : "bg-white hover:bg-secondary"
              }`}
            >
              {c}
            </button>
          ))}
        </div>

        {loading ? (
          <div className="overline text-muted-foreground">Loading functions…</div>
        ) : filtered.length === 0 ? (
          <div className="border border-foreground/15 p-12 text-center">
            <div className="overline mb-2">// NO RESULTS</div>
            <div className="text-muted-foreground">No functions match your filters.</div>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-0 border-l border-t border-foreground/15">
            {filtered.map((f) => (
              <button
                key={f.id}
                onClick={() => navigate(`/functions/${f.id}`)}
                data-testid={`func-card-${f.name.toLowerCase()}`}
                className="text-left border-r border-b border-foreground/15 p-6 bg-white hover:bg-secondary lift relative group"
              >
                <div className="flex items-start justify-between mb-3">
                  <div className="flex items-center gap-2">
                    <FunctionIcon size={18} className="klein" weight="bold" />
                    <span className="font-black text-xl tracking-tight">{f.name}</span>
                  </div>
                  <Badge variant="outline" className="rounded-none border-foreground/20 text-xs">{f.category}</Badge>
                </div>
                <code className="block text-xs bg-secondary border border-foreground/10 p-2 mb-3 truncate">{f.syntax}</code>
                <p className="text-sm text-muted-foreground line-clamp-2 leading-relaxed">{f.description}</p>
              </button>
            ))}
          </div>
        )}
      </main>
    </div>
  );
}
