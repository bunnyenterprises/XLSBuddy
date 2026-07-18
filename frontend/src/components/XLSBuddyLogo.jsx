import React from "react";

export function XLSBuddyIcon({ size = 36 }) {
  const id = `lg${size}`;
  return (
    <svg width={size} height={size} viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id={`${id}a`} x1="0" y1="0" x2="40" y2="40" gradientUnits="userSpaceOnUse">
          <stop offset="0%" stopColor="#0f766e" />
          <stop offset="100%" stopColor="#16a34a" />
        </linearGradient>
        <linearGradient id={`${id}b`} x1="0" y1="0" x2="40" y2="40" gradientUnits="userSpaceOnUse">
          <stop offset="0%" stopColor="#134e4a" />
          <stop offset="100%" stopColor="#052e16" />
        </linearGradient>
        <clipPath id={`${id}c`}>
          <rect width="40" height="40" rx="9" />
        </clipPath>
      </defs>

      {/* Background */}
      <rect width="40" height="40" rx="9" fill={`url(#${id}b)`} />

      {/* Grid overlay */}
      <g clipPath={`url(#${id}c)`} opacity="0.18">
        {[8,14,20,26,32].map(y => (
          <line key={`h${y}`} x1="0" y1={y} x2="40" y2={y} stroke="#4ade80" strokeWidth="0.8"/>
        ))}
        {[8,14,20,26,32].map(x => (
          <line key={`v${x}`} x1={x} y1="0" x2={x} y2="40" stroke="#4ade80" strokeWidth="0.8"/>
        ))}
      </g>

      {/* Left panel — spreadsheet rows */}
      <rect x="5" y="10" width="14" height="20" rx="2" fill={`url(#${id}a)`} opacity="0.9"/>
      <rect x="7" y="13" width="10" height="2" rx="0.5" fill="white" opacity="0.9"/>
      <rect x="7" y="17" width="10" height="2" rx="0.5" fill="white" opacity="0.65"/>
      <rect x="7" y="21" width="7" height="2" rx="0.5" fill="white" opacity="0.65"/>
      <rect x="7" y="25" width="8" height="2" rx="0.5" fill="white" opacity="0.65"/>

      {/* Right panel — X mark */}
      <rect x="22" y="10" width="14" height="20" rx="2" fill={`url(#${id}a)`} opacity="0.7"/>
      <line x1="25.5" y1="13.5" x2="32.5" y2="26.5" stroke="white" strokeWidth="2.5" strokeLinecap="round"/>
      <line x1="32.5" y1="13.5" x2="25.5" y2="26.5" stroke="white" strokeWidth="2.5" strokeLinecap="round"/>

      {/* Green glow dot */}
      <circle cx="20" cy="20" r="1.5" fill="#4ade80" opacity="0.8"/>
    </svg>
  );
}

export function XLSBuddyWordmark({ iconSize = 36, className = "" }) {
  return (
    <span className={`flex items-center gap-2 ${className}`}>
      <XLSBuddyIcon size={iconSize} />
      <span className="font-black tracking-tight text-lg leading-none">
        <span className="text-gray-900 dark:text-white">XLS</span>
        <span className="text-[#16a34a]">Buddy</span>
      </span>
    </span>
  );
}
