import { useState, useRef, useEffect } from "react";
import { Globe, Check } from "@phosphor-icons/react";
import { useLanguage } from "@/context/LanguageContext";


export default function LanguageSelector() {
  const { language, setLanguage, current, LANGUAGES, t } = useLanguage();
  const [open, setOpen] = useState(false);
  const ref = useRef(null);

  useEffect(() => {
    const close = (e) => {
      if (ref.current && !ref.current.contains(e.target)) setOpen(false);
    };
    document.addEventListener("mousedown", close);
    return () => document.removeEventListener("mousedown", close);
  }, []);

  return (
    <div className="relative" ref={ref}>
      <button
        onClick={() => setOpen((o) => !o)}
        title="Choose language / भाषा चुनें"
        className="h-9 px-2.5 flex items-center gap-1.5 border border-foreground/15 dark:border-white/15 hover:bg-secondary dark:hover:bg-white/10 transition-colors text-sm font-medium dark:text-white"
      >
        <Globe size={15} />
        <span className="hidden sm:inline text-sm">{current.native}</span>
      </button>

      {open && (
        <div className="absolute right-0 top-full mt-1 w-52 bg-white dark:bg-[#1c2640] border border-gray-200 dark:border-gray-700 shadow-xl z-50 py-1 max-h-80 overflow-y-auto">
          <div className="px-3 py-2 border-b border-gray-100 dark:border-gray-700">
            <p className="text-[10px] font-bold text-gray-400 dark:text-gray-500 uppercase tracking-widest">
              {t("aiRespondingIn")}
            </p>
          </div>
          {LANGUAGES.map((lang) => {
            const active = language === lang.code;
            return (
              <button
                key={lang.code}
                onClick={() => { setLanguage(lang.code); setOpen(false); }}
                className={`w-full text-left px-4 py-2.5 text-sm flex items-center justify-between transition-colors ${
                  active
                    ? "bg-green-50 dark:bg-green-900/20 text-green-700 dark:text-green-400"
                    : "text-gray-700 dark:text-gray-200 hover:bg-gray-50 dark:hover:bg-white/5"
                }`}
              >
                <div>
                  <span className="font-semibold">{lang.native}</span>
                  {lang.code !== "en" && (
                    <span className="ml-2 text-xs text-gray-400 dark:text-gray-500">{lang.name}</span>
                  )}
                </div>
                {active && <Check size={14} weight="bold" className="shrink-0" />}
              </button>
            );
          })}
        </div>
      )}
    </div>
  );
}
