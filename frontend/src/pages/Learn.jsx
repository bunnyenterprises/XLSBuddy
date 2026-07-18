import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { BookOpen, Lock, CheckCircle, ArrowRight, Lightning, Trophy, Star, ChatCircleDots, Sparkle, MagnifyingGlass } from "@phosphor-icons/react";
import api from "@/lib/api";
import { Header } from "@/components/Header";

const PATH_VISUALS = {
  beginner: {
    gradient: "linear-gradient(135deg, #11998e 0%, #38ef7d 100%)",
    topics: ["What is Excel?", "Cells & Rows", "SUM & AVERAGE", "Basic Formatting", "Save & Share"],
    tagline: "Perfect starting point — zero experience needed",
    formula: "=SUM(A1:A10)",
    color: "#11998e",
  },
  intermediate: {
    gradient: "linear-gradient(135deg, #002FA7 0%, #4a80f5 100%)",
    topics: ["VLOOKUP", "IF Statements", "Pivot Tables", "Charts & Graphs", "Data Validation"],
    tagline: "Go beyond basics and work smarter",
    formula: "=VLOOKUP(A2,B:C,2,0)",
    color: "#002FA7",
  },
  advanced: {
    gradient: "linear-gradient(135deg, #6b21a8 0%, #a855f7 100%)",
    topics: ["INDEX MATCH", "Array Formulas", "Power Query", "Macros & VBA", "Dashboard Design"],
    tagline: "Master Excel like a professional analyst",
    formula: "=INDEX(B:B,MATCH(A2,A:A,0))",
    color: "#6b21a8",
  },
};

function PathCard({ path }) {
  const visual = PATH_VISUALS[path.level] || PATH_VISUALS.beginner;
  const isComplete = path.progress_pct === 100;
  const hasStarted = path.completed_lessons > 0;

  return (
    <div className="rounded-2xl overflow-hidden bg-white dark:bg-[#1c2640] border border-gray-200 dark:border-gray-700 hover:shadow-xl transition-all duration-300 hover:-translate-y-1 flex flex-col">

      {/* Visual Banner */}
      <div className="relative h-44 overflow-hidden" style={{ background: visual.gradient }}>
        {/* Grid pattern */}
        <svg className="absolute inset-0 w-full h-full opacity-10" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <pattern id={`grid-${path.id}`} width="28" height="28" patternUnits="userSpaceOnUse">
              <path d="M 28 0 L 0 0 0 28" fill="none" stroke="white" strokeWidth="1"/>
            </pattern>
          </defs>
          <rect width="100%" height="100%" fill={`url(#grid-${path.id})`} />
        </svg>

        {/* Big emoji */}
        <div className="absolute top-4 left-5 text-5xl drop-shadow-lg">{path.emoji}</div>

        {/* Formula preview */}
        <div className="absolute bottom-4 left-5 right-5">
          <div className="bg-black/25 backdrop-blur-sm rounded-lg px-3 py-2 inline-block">
            <code className="text-white text-xs font-mono">{visual.formula}</code>
          </div>
        </div>

        {/* Level badge */}
        <div className="absolute top-4 right-4">
          <span className="bg-white/20 backdrop-blur-sm text-white text-[10px] font-black uppercase tracking-widest px-2.5 py-1 rounded-full border border-white/30">
            {path.level}
          </span>
        </div>

        {/* Lock / Complete overlay */}
        {path.locked && (
          <div className="absolute inset-0 bg-black/40 backdrop-blur-[2px] flex items-center justify-center">
            <div className="bg-white/10 border border-white/20 rounded-xl px-4 py-2 flex items-center gap-2">
              <Lock size={16} weight="bold" className="text-amber-300" />
              <span className="text-white text-sm font-bold">Pro Only</span>
            </div>
          </div>
        )}
        {isComplete && (
          <div className="absolute top-4 left-1/2 -translate-x-1/2">
            <div className="bg-emerald-500 text-white text-xs font-black px-3 py-1 rounded-full flex items-center gap-1">
              <CheckCircle size={12} weight="fill" /> COMPLETED
            </div>
          </div>
        )}
      </div>

      {/* Card body */}
      <div className="p-5 flex flex-col flex-1">
        <h2 className="text-lg font-black text-gray-900 dark:text-white mb-1">{path.title}</h2>
        <p className="text-xs text-gray-500 dark:text-gray-400 mb-3 italic">{visual.tagline}</p>
        <p className="text-sm text-gray-600 dark:text-gray-400 leading-relaxed mb-4">{path.description}</p>

        {/* What you'll learn */}
        <div className="mb-4">
          <p className="text-[10px] font-black uppercase tracking-widest text-gray-400 dark:text-gray-500 mb-2">What you'll learn</p>
          <div className="flex flex-wrap gap-1.5">
            {visual.topics.map((topic) => (
              <span key={topic} className="text-xs px-2 py-0.5 rounded-md font-semibold"
                style={{ background: `${visual.color}18`, color: visual.color }}>
                {topic}
              </span>
            ))}
          </div>
        </div>

        {/* Stats */}
        <div className="flex items-center gap-4 text-xs text-gray-400 dark:text-gray-500 mb-4">
          <span className="flex items-center gap-1"><BookOpen size={12} /> {path.total_lessons} lessons</span>
          <span className="flex items-center gap-1"><Lightning size={12} /> {path.total_xp} XP</span>
          <span>~{path.estimated_hours}h</span>
        </div>

        {/* Progress */}
        <div className="mb-4">
          <div className="flex justify-between text-xs text-gray-400 mb-1">
            <span>{path.completed_lessons}/{path.total_lessons} done</span>
            <span>{path.progress_pct}%</span>
          </div>
          <div className="h-1.5 bg-gray-100 dark:bg-gray-700 rounded-full overflow-hidden">
            <div className="h-full rounded-full transition-all duration-700"
              style={{ width: `${path.progress_pct}%`, background: visual.gradient }} />
          </div>
        </div>

        {/* CTA */}
        <div className="mt-auto">
          {path.locked ? (
            <Link to="/pricing"
              className="w-full flex items-center justify-center gap-2 py-3 rounded-xl bg-amber-500 hover:bg-amber-600 text-white font-bold text-sm transition-colors">
              <Lock size={14} weight="bold" /> Unlock with Pro
            </Link>
          ) : (
            <Link to={`/learn/${path.slug}`}
              className="w-full flex items-center justify-center gap-2 py-3 rounded-xl text-white font-bold text-sm transition-all hover:opacity-90"
              style={{ background: visual.gradient }}>
              {isComplete ? <><Trophy size={14} weight="fill" /> Review Path</>
                : hasStarted ? <><ArrowRight size={14} weight="bold" /> Continue Learning</>
                : <><BookOpen size={14} weight="bold" /> Start Path</>}
            </Link>
          )}
        </div>
      </div>
    </div>
  );
}

export default function Learn() {
  const [paths, setPaths] = useState([]);
  const [progress, setProgress] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const load = async () => {
      try {
        const [pathsRes, progressRes] = await Promise.all([
          api.get("/learn/paths"),
          api.get("/learn/progress"),
        ]);
        setPaths(pathsRes.data.paths);
        setProgress(progressRes.data);
      } catch {
        // handled by auth context redirect
      } finally {
        setLoading(false);
      }
    };
    load();
  }, []);

  if (loading) {
    return (
      <div className="min-h-screen page-bg flex items-center justify-center">
        <div className="text-center">
          <div className="w-10 h-10 border-3 border-[#002FA7] border-t-transparent rounded-full animate-spin mx-auto mb-4" />
          <p className="text-gray-500 dark:text-gray-400 text-sm">Loading your learning paths...</p>
        </div>
      </div>
    );
  }

  const totalCompleted = paths.reduce((s, p) => s + p.completed_lessons, 0);
  const totalLessons = paths.reduce((s, p) => s + p.total_lessons, 0);

  return (
    <div className="min-h-screen page-bg">
      <Header />
      <div className="max-w-6xl mx-auto px-4 py-10">

        {/* Hero */}
        <div className="rounded-2xl text-white p-8 lg:p-12 mb-8 relative overflow-hidden shadow-xl"
          style={{ background: "linear-gradient(135deg, #1a3fad 0%, #002FA7 50%, #1e1b8f 100%)" }}>
          <div className="absolute right-0 top-0 bottom-0 flex items-center pr-8 pointer-events-none opacity-[0.05]">
            <div className="text-[140px] font-black leading-none select-none">XLS</div>
          </div>
          <div className="relative">
            <p className="text-xs font-bold tracking-widest text-white/60 uppercase mb-3">LEARNING PATHS</p>
            <h1 className="text-3xl lg:text-4xl font-extrabold tracking-tight mb-3">
              Learn Excel with AI Coach
            </h1>
            <p className="text-blue-100/80 max-w-xl mb-6">
              From absolute basics to advanced formulas. Each lesson is bite-sized, interactive, and guided by your personal AI coach.
            </p>

            {/* Progress summary */}
            {progress && (
              <div className="flex flex-wrap items-center gap-6 bg-white/10 backdrop-blur-sm rounded-xl px-5 py-4 w-fit">
                <div className="flex items-center gap-2">
                  <span className="text-2xl">{progress.level?.emoji}</span>
                  <div>
                    <div className="font-black text-sm">{progress.level?.name}</div>
                    <div className="text-xs text-white/60">{progress.xp} XP</div>
                  </div>
                </div>
                <div className="text-center">
                  <div className="text-2xl font-black">{progress.streak} 🔥</div>
                  <div className="text-xs text-white/60">day streak</div>
                </div>
                <div className="text-center">
                  <div className="text-2xl font-black">{totalCompleted}</div>
                  <div className="text-xs text-white/60">of {totalLessons} lessons</div>
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Path cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-10">
          {paths.map((path) => (
            <PathCard key={path.id} path={path} />
          ))}
        </div>

        {/* Quick tools */}
        <div className="bg-white dark:bg-[#1c2640] rounded-2xl border border-gray-200 dark:border-gray-700 p-6 mb-6">
          <h2 className="font-black text-gray-900 dark:text-white mb-1">Practice while you learn</h2>
          <p className="text-sm text-gray-500 dark:text-gray-400 mb-4">Use these tools alongside your lessons</p>
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
            {[
              { to: "/chat", icon: ChatCircleDots, label: "Ask AI", desc: "Any Excel question" },
              { to: "/formula-generator", icon: Sparkle, label: "Formula Generator", desc: "Describe & get formula" },
              { to: "/excel-analyzer", icon: MagnifyingGlass, label: "Analyze Excel", desc: "Upload your file" },
              { to: "/functions", icon: BookOpen, label: "Function Library", desc: "60+ functions" },
            ].map((t) => {
              const Icon = t.icon;
              return (
                <Link key={t.to} to={t.to}
                  className="flex flex-col gap-1 p-4 rounded-xl bg-gray-50 dark:bg-gray-800/50 hover:bg-blue-50 dark:hover:bg-blue-900/20 border border-gray-200 dark:border-gray-700 hover:border-blue-300 transition-all">
                  <Icon size={20} className="text-[#002FA7] dark:text-blue-400" />
                  <span className="text-xs font-bold text-gray-800 dark:text-white">{t.label}</span>
                  <span className="text-[11px] text-gray-400">{t.desc}</span>
                </Link>
              );
            })}
          </div>
        </div>

        {/* Help / Contact */}
        <div className="rounded-2xl border border-gray-200 dark:border-gray-700 p-6 bg-white dark:bg-[#1c2640] flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
          <div>
            <h3 className="font-black text-gray-900 dark:text-white mb-1">Need help or have feedback?</h3>
            <p className="text-sm text-gray-500 dark:text-gray-400">Our team is here to help you learn Excel faster.</p>
          </div>
          <a href="mailto:xlsbuddy@gmail.com"
            className="shrink-0 inline-flex items-center gap-2 bg-[#002FA7] hover:bg-blue-800 text-white font-bold text-sm px-5 py-2.5 rounded-xl transition-colors">
            <Star size={14} weight="fill" /> Contact Support
          </a>
        </div>

      </div>
    </div>
  );
}
