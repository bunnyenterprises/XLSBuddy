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

        {/* Hero card — rounded, indigo gradient */}
        <div className="rounded-2xl text-white p-8 lg:p-12 mb-8 relative overflow-hidden shadow-xl"
          style={{ background: "linear-gradient(135deg, #1a3fad 0%, #002FA7 50%, #1e1b8f 100%)" }}>
          {/* Decorative dots */}
          {[[85,20],[92,60],[8,75]].map(([x,y],i)=>(
            <div key={i} className="absolute rounded-full pointer-events-none opacity-10"
              style={{ left:`${x}%`, top:`${y}%`, width:i===0?120:i===1?80:60, height:i===0?120:i===1?80:60, background:"white" }}/>
          ))}
          <div className="absolute right-0 top-0 bottom-0 flex items-center justify-end pr-8 pointer-events-none opacity-[0.05]">
            <div className="text-[180px] font-black leading-none select-none">XLS</div>
          </div>
          <div className="relative">
            <p className="text-xs font-bold tracking-widest text-white/60 uppercase mb-3">XLSBUDDY DASHBOARD</p>
            <h1 className="text-3xl lg:text-5xl font-extrabold tracking-tight mb-4">
              Welcome back, {user?.name?.split(" ")[0] || "there"}.
            </h1>
            <p className="text-lg text-blue-100/80 max-w-2xl mb-6">
              Search Excel formulas, learn tutorials, and get AI-powered help in seconds.
            </p>
            <div className="flex flex-wrap gap-3">
              <Link to="/functions">
                <Button className="rounded-full bg-white text-[#002FA7] hover:bg-white/90 h-11 px-6 font-bold shadow-lg">
                  Browse Functions
                </Button>
              </Link>
              <Link to="/chat">
                <Button variant="outline" className="rounded-full border-white/40 text-white hover:bg-white/10 h-11 px-6">
                  Ask AI
                </Button>
              </Link>
              <Link to="/tutorials">
                <Button variant="outline" className="rounded-full border-white/40 text-white hover:bg-white/10 h-11 px-6">
                  Tutorials
                </Button>
              </Link>
            </div>
          </div>
        </div>

        {/* Stats row — rounded cards with shadows */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
          {[
            { k: "60+", v: "FUNCTIONS", color: "text-indigo-600" },
            { k: "12+", v: "TUTORIALS", color: "text-emerald-600" },
            { k: "AI", v: "ASSISTANT", color: "text-violet-600" },
            { k: "24/7", v: "SUPPORT", color: "text-blue-600" },
          ].map((s) => (
            <div key={s.v} className="rounded-2xl p-6 lg:p-8 bg-white dark:bg-[#111827] shadow-sm border border-white/60 dark:border-white/5">
              <div className={`text-4xl font-black tracking-tight ${s.color}`}>{s.k}</div>
              <div className="text-[11px] font-bold tracking-widest text-muted-foreground mt-2 uppercase">{s.v}</div>
            </div>
          ))}
        </div>

        {/* Tools grid — rounded cards */}
        <p className="text-xs font-bold tracking-widest text-indigo-500 uppercase mb-2">TOOLS</p>
        <h2 className="text-2xl font-extrabold tracking-tight mb-6">Everything you need.</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {tiles.map((t, i) => {
            const Icon = t.icon;
            return (
              <Link
                to={t.to}
                key={t.to}
                data-testid={`tile-${t.title.toLowerCase().replace(/[^a-z]/g, "-")}`}
                className="group rounded-2xl p-7 lg:p-8 bg-white dark:bg-[#111827] shadow-sm border border-white/60 dark:border-white/5 hover:shadow-md hover:-translate-y-0.5 transition-all duration-200"
              >
                <Icon size={32} weight="duotone" className="text-indigo-600 mb-4" />
                <div className="text-[10px] font-bold tracking-widest text-muted-foreground mb-2">0{i + 1}</div>
                <h3 className="font-bold text-lg tracking-tight mb-2">{t.title}</h3>
                <p className="text-sm leading-relaxed text-muted-foreground">{t.desc}</p>
                <ArrowUpRight size={20} className="mt-4 opacity-30 group-hover:opacity-100 group-hover:text-indigo-600 transition-all" />
              </Link>
            );
          })}
        </div>

        {/* Promo banner */}
        <div className="mt-8 rounded-2xl overflow-hidden shadow-sm relative" style={{ background: "linear-gradient(135deg, #1D6F42 0%, #0f4a2c 100%)" }}>
          <div className="absolute right-0 top-0 bottom-0 flex items-center pr-8 pointer-events-none opacity-[0.07]">
            <div className="text-[140px] font-black leading-none select-none text-white">XLS</div>
          </div>
          <div className="relative flex flex-col md:flex-row items-start md:items-center justify-between gap-6 p-8 lg:p-10">
            <div>
              <div className="flex items-center gap-2 mb-2">
                <span className="text-[10px] font-bold tracking-widest text-emerald-300 uppercase">Pro Tip</span>
              </div>
              <h3 className="text-xl lg:text-2xl font-extrabold text-white tracking-tight mb-1">
                Unlock unlimited AI chat + advanced tutorials
              </h3>
              <p className="text-emerald-100/80 text-sm max-w-lg">
                Upgrade to XLSBuddy Pro and get unlimited formula help, priority AI responses, and exclusive advanced Excel content.
              </p>
            </div>
            <div className="flex gap-3 shrink-0">
              <Link to="/pricing">
                <Button className="rounded-full bg-white text-[#1D6F42] hover:bg-white/90 font-bold px-6 shadow-lg">
                  Upgrade to Pro
                </Button>
              </Link>
              <a href="https://wa.me/?text=Check%20out%20XLSBuddy%20-%20the%20best%20Excel%20formula%20helper!%20https://xlsbuddy.vercel.app" target="_blank" rel="noopener noreferrer">
                <Button variant="outline" className="rounded-full border-white/40 text-white hover:bg-white/10 px-6">
                  Share App
                </Button>
              </a>
            </div>
          </div>
        </div>

      </main>
    </div>
  );
}
