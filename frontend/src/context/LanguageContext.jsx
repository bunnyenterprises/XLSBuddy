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

const T = {
  en: {
    dashboard: "Dashboard", learn: "Learn", functions: "Functions",
    aiChat: "AI Chat", formulaAI: "Formula AI", excelAI: "Excel AI",
    pricing: "Pricing", signIn: "Sign in", signOut: "Sign out",
    upgrade: "Upgrade", getStarted: "Get Started", bookmarks: "Bookmarks",
    reviews: "Reviews", admin: "Admin", aiRespondingIn: "AI responds in",
    signedInAs: "Signed in as", free: "FREE", pro: "PRO",
    upgradeToProMenu: "Upgrade to Pro",
  },
  hi: {
    dashboard: "डैशबोर्ड", learn: "सीखें", functions: "फ़ंक्शन",
    aiChat: "AI चैट", formulaAI: "फ़ॉर्मूला AI", excelAI: "Excel AI",
    pricing: "मूल्य", signIn: "साइन इन", signOut: "साइन आउट",
    upgrade: "अपग्रेड", getStarted: "शुरू करें", bookmarks: "बुकमार्क",
    reviews: "समीक्षाएं", admin: "एडमिन", aiRespondingIn: "AI जवाब देगा",
    signedInAs: "लॉग इन:", free: "मुफ़्त", pro: "PRO",
    upgradeToProMenu: "Pro में अपग्रेड करें",
  },
  ta: {
    dashboard: "டாஷ்போர்டு", learn: "கற்றுக்கொள்", functions: "செயல்பாடுகள்",
    aiChat: "AI அரட்டை", formulaAI: "சூத்திர AI", excelAI: "Excel AI",
    pricing: "விலை", signIn: "உள்நுழை", signOut: "வெளியேறு",
    upgrade: "மேம்படுத்து", getStarted: "தொடங்கு", bookmarks: "புக்மார்க்",
    reviews: "மதிப்புரைகள்", admin: "நிர்வாகம்", aiRespondingIn: "AI பதிலளிக்கிறது",
    signedInAs: "உள்நுழைந்தவர்:", free: "இலவசம்", pro: "PRO",
    upgradeToProMenu: "Pro-க்கு மேம்படுத்து",
  },
  te: {
    dashboard: "డాష్‌బోర్డ్", learn: "నేర్చుకో", functions: "ఫంక్షన్లు",
    aiChat: "AI చాట్", formulaAI: "ఫార్ములా AI", excelAI: "Excel AI",
    pricing: "ధర", signIn: "సైన్ ఇన్", signOut: "సైన్ అవుట్",
    upgrade: "అప్‌గ్రేడ్", getStarted: "ప్రారంభించు", bookmarks: "బుక్‌మార్క్లు",
    reviews: "సమీక్షలు", admin: "అడ్మిన్", aiRespondingIn: "AI జవాబిస్తుంది",
    signedInAs: "లాగిన్:", free: "ఉచితం", pro: "PRO",
    upgradeToProMenu: "Pro కి అప్‌గ్రేడ్",
  },
  mr: {
    dashboard: "डॅशबोर्ड", learn: "शिका", functions: "फंक्शन",
    aiChat: "AI चॅट", formulaAI: "फॉर्म्युला AI", excelAI: "Excel AI",
    pricing: "किंमत", signIn: "साइन इन", signOut: "साइन आउट",
    upgrade: "अपग्रेड", getStarted: "सुरुवात करा", bookmarks: "बुकमार्क",
    reviews: "पुनरावलोकने", admin: "प्रशासक", aiRespondingIn: "AI उत्तर देतो",
    signedInAs: "लॉग इन:", free: "मोफत", pro: "PRO",
    upgradeToProMenu: "Pro मध्ये अपग्रेड करा",
  },
  gu: {
    dashboard: "ડેશબોર્ડ", learn: "શીખો", functions: "ફંક્શન",
    aiChat: "AI ચૅટ", formulaAI: "ફૉર્મ્યુલા AI", excelAI: "Excel AI",
    pricing: "કિંમત", signIn: "સાઇન ઇન", signOut: "સાઇન આઉટ",
    upgrade: "અપગ્રેડ", getStarted: "શરૂ કરો", bookmarks: "બુકમાર્ક",
    reviews: "સમીક્ષાઓ", admin: "એડમિન", aiRespondingIn: "AI જવાબ આપે છે",
    signedInAs: "લૉગ ઇન:", free: "મફત", pro: "PRO",
    upgradeToProMenu: "Pro માં અપગ્રેડ કરો",
  },
  kn: {
    dashboard: "ಡ್ಯಾಶ್‌ಬೋರ್ಡ್", learn: "ಕಲಿಯಿರಿ", functions: "ಕಾರ್ಯಗಳು",
    aiChat: "AI ಚಾಟ್", formulaAI: "ಫಾರ್ಮುಲಾ AI", excelAI: "Excel AI",
    pricing: "ಬೆಲೆ", signIn: "ಸೈನ್ ಇನ್", signOut: "ಸೈನ್ ಔಟ್",
    upgrade: "ಅಪ್‌ಗ್ರೇಡ್", getStarted: "ಪ್ರಾರಂಭಿಸಿ", bookmarks: "ಬುಕ್‌ಮಾರ್ಕ್‌ಗಳು",
    reviews: "ವಿಮರ್ಶೆಗಳು", admin: "ಆಡ್ಮಿನ್", aiRespondingIn: "AI ಉತ್ತರಿಸುತ್ತದೆ",
    signedInAs: "ಲಾಗಿನ್:", free: "ಉಚಿತ", pro: "PRO",
    upgradeToProMenu: "Pro ಗೆ ಅಪ್‌ಗ್ರೇಡ್",
  },
  ml: {
    dashboard: "ഡാഷ്‌ബോർഡ്", learn: "പഠിക്കൂ", functions: "ഫങ്ഷനുകൾ",
    aiChat: "AI ചാറ്റ്", formulaAI: "ഫോർമുല AI", excelAI: "Excel AI",
    pricing: "വില", signIn: "സൈൻ ഇൻ", signOut: "സൈൻ ഔട്ട്",
    upgrade: "അപ്‌ഗ്രേഡ്", getStarted: "ആരംഭിക്കൂ", bookmarks: "ബുക്ക്‌മാർക്കുകൾ",
    reviews: "അവലോകനങ്ങൾ", admin: "അഡ്‌മിൻ", aiRespondingIn: "AI മറുപടി നൽകുന്നു",
    signedInAs: "ലോഗിൻ:", free: "സൗജന്യം", pro: "PRO",
    upgradeToProMenu: "Pro-ലേക്ക് അപ്‌ഗ്രേഡ്",
  },
  bn: {
    dashboard: "ড্যাশবোর্ড", learn: "শিখুন", functions: "ফাংশন",
    aiChat: "AI চ্যাট", formulaAI: "ফর্মুলা AI", excelAI: "Excel AI",
    pricing: "মূল্য", signIn: "সাইন ইন", signOut: "সাইন আউট",
    upgrade: "আপগ্রেড", getStarted: "শুরু করুন", bookmarks: "বুকমার্ক",
    reviews: "পর্যালোচনা", admin: "অ্যাডমিন", aiRespondingIn: "AI উত্তর দেয়",
    signedInAs: "লগইন:", free: "বিনামূল্যে", pro: "PRO",
    upgradeToProMenu: "Pro-তে আপগ্রেড করুন",
  },
  pa: {
    dashboard: "ਡੈਸ਼ਬੋਰਡ", learn: "ਸਿੱਖੋ", functions: "ਫੰਕਸ਼ਨ",
    aiChat: "AI ਚੈਟ", formulaAI: "ਫਾਰਮੂਲਾ AI", excelAI: "Excel AI",
    pricing: "ਕੀਮਤ", signIn: "ਸਾਈਨ ਇਨ", signOut: "ਸਾਈਨ ਆਊਟ",
    upgrade: "ਅੱਪਗ੍ਰੇਡ", getStarted: "ਸ਼ੁਰੂ ਕਰੋ", bookmarks: "ਬੁੱਕਮਾਰਕ",
    reviews: "ਸਮੀਖਿਆਵਾਂ", admin: "ਐਡਮਿਨ", aiRespondingIn: "AI ਜਵਾਬ ਦਿੰਦਾ ਹੈ",
    signedInAs: "ਲੌਗਇਨ:", free: "ਮੁਫ਼ਤ", pro: "PRO",
    upgradeToProMenu: "Pro ਵਿੱਚ ਅੱਪਗ੍ਰੇਡ ਕਰੋ",
  },
};

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

  const t = (key) => T[language]?.[key] ?? T.en[key] ?? key;

  return (
    <LanguageContext.Provider value={{ language, setLanguage, current, LANGUAGES, t }}>
      {children}
    </LanguageContext.Provider>
  );
}

export const useLanguage = () => useContext(LanguageContext);
