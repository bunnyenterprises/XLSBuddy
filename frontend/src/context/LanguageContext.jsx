import { createContext, useContext, useState } from "react";

export const LANGUAGES = [
  { code: "en",  name: "English",   native: "English" },
  { code: "hi",  name: "Hindi",     native: "हिंदी" },
  { code: "ta",  name: "Tamil",     native: "தமிழ்" },
  { code: "te",  name: "Telugu",    native: "తెలుగు" },
  { code: "mr",  name: "Marathi",   native: "मराठी" },
  { code: "gu",  name: "Gujarati",  native: "ગુજરાતી" },
  { code: "kn",  name: "Kannada",   native: "ಕನ್ನಡ" },
  { code: "ml",  name: "Malayalam", native: "മലയാളം" },
  { code: "bn",  name: "Bengali",   native: "বাংলা" },
  { code: "pa",  name: "Punjabi",   native: "ਪੰਜਾਬੀ" },
];

const LanguageContext = createContext(null);

export function LanguageProvider({ children }) {
  const [language, setLanguageState] = useState(
    () => localStorage.getItem("xlsbuddy_lang") || "en"
  );

  const setLanguage = (code) => {
    localStorage.setItem("xlsbuddy_lang", code);
    setLanguageState(code);
  };

  const current = LANGUAGES.find((l) => l.code === language) || LANGUAGES[0];

  return (
    <LanguageContext.Provider value={{ language, setLanguage, current, LANGUAGES }}>
      {children}
    </LanguageContext.Provider>
  );
}

export const useLanguage = () => useContext(LanguageContext);
