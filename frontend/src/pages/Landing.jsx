import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { Header } from "@/components/Header";
import { Button } from "@/components/ui/button";
import { api } from "@/lib/api";
import { ArrowRight, ChartLine, BookOpen, Table, MagnifyingGlass, Lightning, Sparkle, Star, Quotes } from "@phosphor-icons/react";

const FEATURE_IMG = "https://images.unsplash.com/photo-1770816306252-b970806ebdf1?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDQ2Mzl8MHwxfHNlYXJjaHwyfHxhYnN0cmFjdCUyMHdoaXRlJTIwZ3JpZCUyMGFyY2hpdGVjdHVyZXxlbnwwfHx8fDE3NzgxNjYzNjJ8MA&ixlib=rb-4.1.0&q=85";

function ExcelMockup() {
  const cols = ["", "A", "B", "C", "D", "E"];
  const rows = [
    { n: 1, cells: ["Sales Rep", "Region", "Product", "Revenue", "Target"], header: true },
    { n: 2, cells: ["Alice Chen", "East", "XLOOKUP", "₹48,200", "₹50,000"], formula: 2 },
    { n: 3, cells: ["Bob Kumar", "West", "SUMIFS", "₹31,500", "₹40,000"] },
    { n: 4, cells: ["Carol Singh", "East", "IF / IFS", "₹62,800", "₹55,000"], hi: true },
    { n: 5, cells: ["David Rao", "North", "VLOOKUP", "₹29,100", "₹35,000"] },
    { n: 6, cells: ["", "", "TOTAL", "=SUM(D2:D5)", "=SUM(E2:E5)"], sum: true },
  ];

  return (
    <div className="relative select-none">
      {/* Window chrome */}
      <div className="shadow-2xl border border-white/10 overflow-hidden text-[11px]">
        {/* Title bar - Excel green */}
        <div className="bg-[#1D6F42] px-3 py-2 flex items-center gap-3">
          <div className="flex gap-1.5">
            <div className="w-2.5 h-2.5 rounded-full bg-white/25" />
            <div className="w-2.5 h-2.5 rounded-full bg-white/25" />
            <div className="w-2.5 h-2.5 rounded-full bg-white/25" />
          </div>
          <span className="text-white text-[11px] font-medium ml-1 opacity-90">SalesTracker.xlsx — Excel</span>
        </div>

        {/* Formula bar */}
        <div className="bg-[#f0f0f0] px-2 py-1 flex items-center gap-2 border-b border-gray-300">
          <span className="bg-white border border-gray-300 px-2 py-0.5 font-mono text-gray-700 min-w-[36px] text-center">D6</span>
          <span className="text-gray-400 font-bold">fx</span>
          <span className="font-mono text-[#7030A0] flex-1 truncate">=SUM(D2:D5)</span>
        </div>

        {/* Column headers */}
        <div className="flex bg-[#e8e8e8] border-b border-gray-300">
          {cols.map((c, i) => (
            <div key={i} className={`font-semibold text-center text-gray-600 border-r border-gray-300 py-1 ${
              i === 0 ? "w-7 bg-[#e0e0e0]" : i === 4 ? "flex-1 bg-[#d9e8ff] text-blue-700" : "flex-1"
            }`}>{c}</div>
          ))}
        </div>

        {/* Data rows */}
        {rows.map((row) => (
          <div key={row.n} className={`flex border-b border-gray-200 ${row.header ? "bg-[#1D6F42] text-white font-semibold" : "bg-white"} ${row.hi ? "bg-[#e8f4e8]" : ""} ${row.sum ? "bg-[#f0f0f0] font-semibold" : ""}`}>
            <div className={`w-7 text-center border-r border-gray-300 py-1.5 shrink-0 ${row.header ? "bg-[#155734] text-white/80" : "bg-[#f0f0f0] text-gray-500"}`}>{row.n}</div>
            {row.cells.map((cell, ci) => (
              <div key={ci} className={`flex-1 px-1.5 py-1.5 border-r border-gray-200 truncate ${
                row.formula === ci ? "text-[#7030A0] font-mono" : ""
              } ${row.sum && ci === 3 ? "text-[#7030A0] font-mono text-blue-700" : ""
              } ${row.sum && ci === 4 ? "text-[#7030A0] font-mono text-blue-700" : ""
              } ${ci === 3 && !row.header && !row.sum ? "bg-[#eef4ff] text-blue-800 font-medium" : ""
              } ${row.header ? "text-white" : ""}`}>{cell}</div>
            ))}
          </div>
        ))}

        {/* Status bar */}
        <div className="bg-[#1D6F42] px-3 py-1 flex items-center gap-6 text-white/80">
          <span>READY</span>
          <div className="ml-auto flex gap-4">
            <span>SUM: ₹1,71,600</span>
            <span>AVERAGE: ₹42,900</span>
            <span>COUNT: 4</span>
          </div>
        </div>
      </div>

      {/* Floating formula badges */}
      <div className="absolute -top-3 -right-3 bg-[#7030A0] text-white font-mono px-3 py-1 text-xs shadow-lg">=VLOOKUP()</div>
      <div className="absolute -bottom-3 -left-3 bg-[#1D6F42] text-white font-mono px-3 py-1 text-xs shadow-lg">=SUMIFS()</div>
      <div className="absolute top-1/2 -right-5 bg-klein text-white font-mono px-2 py-0.5 text-xs shadow-md rotate-90 origin-center">=IF()</div>
    </div>
  );
}

export default function Landing() {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    api.get("/reviews").then((r) => setReviews(r.data.slice(0, 6))).catch(() => {});
  }, []);

  const avg = reviews.length
    ? (reviews.reduce((s, r) => s + r.rating, 0) / reviews.length).toFixed(1)
    : null;

  return (
    <div className="min-h-screen page-bg text-foreground dark:text-white">
      <Header />

      {/* HERO — clean white with Excel mockup */}
      <section className="relative overflow-hidden border-b border-foreground/15 bg-white dark:bg-[#030712]">
        {/* Subtle spreadsheet grid pattern */}
        <div className="absolute inset-0 opacity-[0.035] dark:opacity-[0.06]" style={{
          backgroundImage: "linear-gradient(rgba(0,47,167,0.6) 1px, transparent 1px), linear-gradient(90deg, rgba(0,47,167,0.6) 1px, transparent 1px)",
          backgroundSize: "44px 26px"
        }} aria-hidden />
        {/* Blue brand glow bottom-right */}
        <div className="absolute right-0 bottom-0 w-[50%] h-[70%] pointer-events-none" style={{ background: "radial-gradient(ellipse at 80% 80%, rgba(37,99,235,0.10) 0%, transparent 65%)" }} aria-hidden />
        {/* Fade left edge so text area is clean */}
        <div className="absolute inset-0 dark:hidden pointer-events-none" style={{ background: "linear-gradient(105deg, rgba(255,255,255,1) 0%, rgba(255,255,255,0.95) 40%, rgba(255,255,255,0.4) 70%, rgba(255,255,255,0) 100%)" }} aria-hidden />
        <div className="absolute inset-0 hidden dark:block pointer-events-none" style={{ background: "linear-gradient(105deg, rgba(3,7,18,1) 0%, rgba(3,7,18,0.95) 40%, rgba(3,7,18,0.4) 70%, rgba(3,7,18,0) 100%)" }} aria-hidden />

        <div className="relative max-w-[1400px] mx-auto px-6 lg:px-10 pt-20 pb-28">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">

            {/* Left — copy */}
            <div className="lg:col-span-6 slide-in">
              <div className="overline klein mb-6">EXCEL · DECODED</div>
              <h1 className="text-4xl sm:text-5xl lg:text-[3.25rem] font-extrabold tracking-tight leading-tight mb-8">
                Every Excel formula.<br/>
                Every error.<br/>
                <span className="klein">Solved.</span>
              </h1>
              <p className="text-base sm:text-lg max-w-xl text-muted-foreground mb-10 leading-relaxed">
                Browse 60+ Excel functions with live examples. Read curated tutorials.
                Ask our AI anything — get answers in seconds, not hours.
              </p>
              <div className="flex flex-wrap items-center gap-4">
                <Link to="/signup" data-testid="hero-cta-signup">
                  <Button size="lg" className="rounded-none bg-klein hover:bg-[#002FA7]/90 text-white h-14 px-8 text-base font-bold">
                    Start Free <ArrowRight size={18} className="ml-2" />
                  </Button>
                </Link>
                <Link to="/login" data-testid="hero-cta-login">
                  <Button size="lg" variant="outline" className="rounded-none border-foreground/30 h-14 px-8 text-base">
                    Sign in
                  </Button>
                </Link>
              </div>
              <div className="mt-12 flex flex-wrap gap-x-10 gap-y-3 overline text-foreground/50">
                <span>100+ FUNCTIONS</span>
                <span>LIVE EXCEL PREVIEW</span>
                <span>0$ TO START</span>
                {avg && <span>⭐ {avg} RATED</span>}
              </div>
            </div>

            {/* Right — Excel spreadsheet mockup */}
            <div className="lg:col-span-6 hidden lg:block px-4">
              <ExcelMockup />
            </div>

          </div>
        </div>
      </section>

      {/* FEATURES — Tetris grid */}
      <section className="border-b border-foreground/15 dark:border-white/10">
        <div className="max-w-[1400px] mx-auto px-6 lg:px-10 py-20">
          <div className="overline klein mb-3">CAPABILITIES</div>
          <h2 className="text-2xl sm:text-3xl font-extrabold tracking-tight mb-12 max-w-3xl">
            100+ formulas. Four tools. Zero spreadsheet panic.
          </h2>

          <div className="grid grid-cols-1 md:grid-cols-12 gap-0 border-l border-t border-foreground/15">
            <div className="md:col-span-7 border-r border-b border-foreground/15 p-8 lg:p-12 lift bg-white dark:bg-[#111827]">
              <ChartLine size={36} weight="duotone" className="klein mb-6" />
              <div className="overline mb-2">01 / FUNCTIONS LIBRARY</div>
              <h3 className="text-2xl lg:text-3xl font-bold tracking-tight mb-4">60+ formulas. Categorized. Explained.</h3>
              <p className="text-muted-foreground leading-relaxed mb-6 max-w-xl">
                SUM, VLOOKUP, XLOOKUP, INDEX/MATCH, PMT, SUMIFS — every function ships
                with syntax, real-world example, and use case.
              </p>
              <div className="flex flex-wrap gap-2">
                {["Math", "Logical", "Lookup", "Text", "Date", "Stats", "Financial"].map((t) => (
                  <span key={t} className="text-xs border border-foreground/20 px-3 py-1 font-medium">{t}</span>
                ))}
              </div>
            </div>

            <div className="md:col-span-5 border-r border-b border-foreground/15 p-8 lg:p-12 lift bg-[#0a1628] text-white relative overflow-hidden">
              <div className="absolute inset-0 opacity-5" style={{
                backgroundImage: "linear-gradient(rgba(255,255,255,0.8) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.8) 1px, transparent 1px)",
                backgroundSize: "28px 18px"
              }} />
              <div className="relative">
                <Table size={36} weight="duotone" className="mb-6" style={{ color: "#7AA0FF" }} />
                <div className="overline mb-2 text-blue-300/70">02 / LIVE EXCEL PREVIEW</div>
                <h3 className="text-2xl lg:text-3xl font-bold tracking-tight mb-4">See every formula in a real spreadsheet.</h3>
                <p className="text-blue-100/70 leading-relaxed">
                  Each function shows a live Excel-style grid with your data, formula bar,
                  and highlighted result — exactly as it appears in Excel.
                </p>
              </div>
            </div>

            <div className="md:col-span-4 border-r border-b border-foreground/15 p-8 lg:p-12 lift bg-white dark:bg-[#111827]">
              <BookOpen size={36} weight="duotone" className="klein mb-6" />
              <div className="overline mb-2">03 / TUTORIALS</div>
              <h3 className="text-xl lg:text-2xl font-bold tracking-tight mb-3">Pivots, lookups, charts, errors.</h3>
              <p className="text-muted-foreground text-sm leading-relaxed">Curated guides for the tasks you actually do every week.</p>
            </div>

            <div className="md:col-span-4 border-r border-b border-foreground/15 p-8 lg:p-12 lift bg-secondary dark:bg-[#1a2235]">
              <MagnifyingGlass size={36} weight="duotone" className="klein mb-6" />
              <div className="overline mb-2">04 / SEARCH</div>
              <h3 className="text-xl lg:text-2xl font-bold tracking-tight mb-3">Find any function in &lt;1 second.</h3>
              <p className="text-muted-foreground text-sm leading-relaxed">Search by name, error code, or use case.</p>
            </div>

            <div className="md:col-span-4 border-r border-b border-foreground/15 p-8 lg:p-12 lift bg-klein text-white">
              <Lightning size={36} weight="duotone" className="mb-6" />
              <div className="overline mb-2 text-white/80">05 / SPEED</div>
              <h3 className="text-xl lg:text-2xl font-bold tracking-tight mb-3">No menus. No fluff.</h3>
              <p className="text-white/80 text-sm leading-relaxed">Keyboard-first. Always one click to the answer.</p>
            </div>
          </div>
        </div>
      </section>

      {/* REVIEWS SECTION */}
      {reviews.length > 0 && (
        <section className="border-b border-foreground/15 bg-secondary dark:bg-[#0d1117]">
          <div className="max-w-[1400px] mx-auto px-6 lg:px-10 py-20">
            <div className="overline klein mb-3">COMMUNITY</div>
            <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-6 mb-12">
              <div>
                <h2 className="text-2xl sm:text-3xl font-extrabold tracking-tight">What people say.</h2>
                {avg && (
                  <div className="flex items-center gap-3 mt-3">
                    <span className="metric-title klein">{avg}</span>
                    <div className="flex">
                      {[1, 2, 3, 4, 5].map((i) => (
                        <Star key={i} size={20} weight={i <= Math.round(avg) ? "fill" : "regular"} className={i <= Math.round(avg) ? "klein" : "text-foreground/20"} />
                      ))}
                    </div>
                    <span className="text-sm text-muted-foreground">from {reviews.length} review{reviews.length !== 1 && "s"}</span>
                  </div>
                )}
              </div>
              <Link to="/reviews">
                <Button variant="outline" className="rounded-none border-foreground/30">
                  See all reviews <ArrowRight size={14} className="ml-2" />
                </Button>
              </Link>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-0 border-l border-t border-foreground/15">
              {reviews.map((r) => (
                <div key={r.id} className="border-r border-b border-foreground/15 p-8 bg-white dark:bg-[#111827] lift">
                  <Quotes size={28} className="text-foreground/15 mb-4" weight="fill" />
                  <div className="flex mb-3">
                    {[1, 2, 3, 4, 5].map((i) => (
                      <Star key={i} size={14} weight={i <= r.rating ? "fill" : "regular"} className={i <= r.rating ? "klein" : "text-foreground/20"} />
                    ))}
                  </div>
                  <p className="text-sm leading-relaxed mb-4 text-foreground/80 line-clamp-4">{r.comment}</p>
                  <div className="flex items-center gap-2">
                    <div className="w-7 h-7 bg-klein flex items-center justify-center text-white text-xs font-bold">
                      {r.user_name?.[0]?.toUpperCase() || "?"}
                    </div>
                    <div>
                      <div className="font-bold text-sm">{r.user_name}</div>
                      <div className="overline text-muted-foreground">{r.updated_at?.slice(0, 10)}</div>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* CTA */}
      <section className="bg-black text-white py-24 lg:py-32">
        <div className="max-w-[1400px] mx-auto px-6 lg:px-10">
          <div className="grid grid-cols-1 md:grid-cols-12 gap-8 items-end">
            <div className="md:col-span-8">
              <div className="overline mb-4 text-white/60">READY?</div>
              <h2 className="text-4xl sm:text-5xl lg:text-6xl font-extrabold tracking-tight leading-tight">
                Stop googling.<br/>
                Start <span style={{ color: "#7AA0FF" }}>mastering</span>.
              </h2>
            </div>
            <div className="md:col-span-4">
              <Link to="/signup" data-testid="footer-cta-signup">
                <Button size="lg" className="rounded-none bg-white text-black hover:bg-white/90 h-16 px-10 text-lg w-full sm:w-auto">
                  <Sparkle size={20} weight="fill" className="mr-2" />
                  Create free account
                </Button>
              </Link>
              <div className="mt-6 overline text-white/60">NO CARD · INSTANT ACCESS</div>
            </div>
          </div>
        </div>
      </section>

      {/* FOOTER */}
      <footer className="bg-black text-white border-t border-white/10 py-10">
        <div className="max-w-[1400px] mx-auto px-6 lg:px-10 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
          <div className="flex items-center gap-2">
            <div className="w-6 h-6 bg-klein flex items-center justify-center">
              <span className="text-white font-black text-xs">X</span>
            </div>
            <span className="font-bold tracking-tight">XLSBUDDY</span>
          </div>
          <div className="overline text-white/50">© 2026 · Built with rigor</div>
        </div>
      </footer>
    </div>
  );
}
