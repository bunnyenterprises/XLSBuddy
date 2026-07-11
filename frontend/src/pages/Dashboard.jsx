import React from "react";
import { Link } from "react-router-dom";
import { Header } from "@/components/Header";
import { useAuth } from "@/context/AuthContext";
import { Button } from "@/components/ui/button";
import { ChartLine, BookOpen, ChatCircleDots, MagnifyingGlass, BookmarkSimple, ArrowUpRight, Sparkle } from "@phosphor-icons/react";

export default function Dashboard() {
  const { user } = useAuth();

  const tiles = [
    { to: "/functions", title: "Functions Library", desc: "Browse 60+ Excel functions by category. Syntax, examples, and real use cases.", icon: ChartLine },
    { to: "/chat", title: "AI Assistant", desc: "Ask anything about Excel — formulas, errors, best practices — and get instant answers.", icon: ChatCircleDots },
    { to: "/tutorials", title: "Tutorials", desc: "Curated guides for pivots, lookups, conditional formatting, errors, and more.", icon: BookOpen },
    { to: "/bookmarks", title: "Bookmarks", desc: "Quick access to functions and tutorials you've saved.", icon: BookmarkSimple },
    { to: "/formula-generator", title: "Formula Generator", desc: "Describe what you want in plain English — get the exact Excel formula instantly.", icon: Sparkle },
    { to: "/functions?focus=search", title: "Quick Search", desc: "Find any function in less than a second by name or use case.", icon: MagnifyingGlass },
  ];

  return (
    <div className="min-h-screen page-bg">
      <Header />
      <main className="max-w-[1400px] mx-auto px-6 lg:px-10 py-10 lg:py-14">

        {/* Hero — sharp, klein, consistent with rest of app */}
        <div className="bg-klein text-white p-8 lg:p-12 mb-10 relative overflow-hidden">
          <div className="absolute right-0 top-0 bottom-0 flex items-center justify-end pr-8 pointer-events-none opacity-[0.06]">
            <div className="text-[180px] font-black leading-none select-none">XLS</div>
          </div>
          <div className="relative">
            <div className="overline mb-4 text-white/70">XLSBUDDY DASHBOARD</div>
            <h1 className="text-3xl lg:text-5xl font-extrabold tracking-tight mb-4">
              Welcome back, {user?.name?.split(" ")[0] || "there"}.
            </h1>
            <p className="text-lg text-blue-100 max-w-2xl mb-6">
              Search Excel formulas, learn tutorials, and get AI-powered help in seconds.
            </p>
            <div className="flex flex-wrap gap-3">
              <Link to="/functions">
                <Button className="rounded-none bg-white text-klein hover:bg-white/90 h-11 px-6 font-bold">
                  Browse Functions
                </Button>
              </Link>
              <Link to="/chat">
                <Button variant="outline" className="rounded-none border-white/40 text-white hover:bg-white/10 h-11 px-6">
                  Ask AI
                </Button>
              </Link>
              <Link to="/tutorials">
                <Button variant="outline" className="rounded-none border-white/40 text-white hover:bg-white/10 h-11 px-6">
                  Tutorials
                </Button>
              </Link>
            </div>
          </div>
        </div>

        {/* Stats row */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-0 border-l border-t border-foreground/15 mb-10">
          {[
            { k: "60+", v: "FUNCTIONS" },
            { k: "12+", v: "TUTORIALS" },
            { k: "AI", v: "ASSISTANT" },
            { k: "24/7", v: "SUPPORT" },
          ].map((s) => (
            <div key={s.v} className="border-r border-b border-foreground/15 p-6 lg:p-8 bg-white dark:bg-[#111827]">
              <div className="metric-title klein">{s.k}</div>
              <div className="overline mt-2 text-muted-foreground">{s.v}</div>
            </div>
          ))}
        </div>

        {/* Tools grid */}
        <div className="overline klein mb-3">TOOLS</div>
        <h2 className="text-2xl font-extrabold tracking-tight mb-8">Everything you need.</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-0 border-l border-t border-foreground/15">
          {tiles.map((t, i) => {
            const Icon = t.icon;
            return (
              <Link
                to={t.to}
                key={t.to}
                data-testid={`tile-${t.title.toLowerCase().replace(/[^a-z]/g, "-")}`}
                className="group border-r border-b border-foreground/15 p-8 lg:p-10 lift bg-white dark:bg-[#111827] hover:bg-secondary dark:hover:bg-[#1a2235] transition-colors"
              >
                <Icon size={32} weight="duotone" className="klein mb-4" />
                <div className="overline mb-2 text-muted-foreground">0{i + 1}</div>
                <h3 className="font-bold text-lg tracking-tight mb-2">{t.title}</h3>
                <p className="text-sm leading-relaxed text-muted-foreground">{t.desc}</p>
                <ArrowUpRight size={20} className="mt-4 opacity-40 group-hover:opacity-100 group-hover:text-klein transition-all" />
              </Link>
            );
          })}
        </div>

      </main>
    </div>
  );
}
