import React, { useId } from "react";

export function XLSBuddyIcon({ size = 36 }) {
  const uid = useId();
  const blueId  = `${uid}b`;
  const greenId = `${uid}g`;
  const clipId  = `${uid}c`;

  return (
    <svg width={size} height={size} viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id={blueId} x1="0" y1="0" x2="40" y2="40" gradientUnits="userSpaceOnUse">
          <stop offset="0%"   stopColor="#818cf8" />
          <stop offset="100%" stopColor="#3b82f6" />
        </linearGradient>
        <linearGradient id={greenId} x1="40" y1="0" x2="0" y2="40" gradientUnits="userSpaceOnUse">
          <stop offset="0%"   stopColor="#4ade80" />
          <stop offset="100%" stopColor="#16a34a" />
        </linearGradient>
        <clipPath id={clipId}>
          <rect width="40" height="40" rx="9" />
        </clipPath>
      </defs>

      {/* Dark background */}
      <rect width="40" height="40" rx="9" fill="#0f172a" />

      <g clipPath={`url(#${clipId})`}>
        {/* Blue diagonal arm — top-left to bottom-right (\) */}
        <line x1="-3" y1="-3" x2="43" y2="43"
          stroke={`url(#${blueId})`}  strokeWidth="16" strokeLinecap="butt" />

        {/* Green diagonal arm — top-right to bottom-left (/) */}
        <line x1="43" y1="-3" x2="-3" y2="43"
          stroke={`url(#${greenId})`} strokeWidth="16" strokeLinecap="butt" />
      </g>
    </svg>
  );
}

export function XLSBuddyWordmark({ iconSize = 36, dark = false, className = "" }) {
  return (
    <span className={`flex items-center gap-2 ${className}`}>
      <XLSBuddyIcon size={iconSize} />
      <span className="font-black tracking-tight text-lg leading-none whitespace-nowrap">
        <span className={dark ? "text-white" : "text-gray-900 dark:text-white"}>XLS</span>
        <span className="text-[#3b82f6]">Buddy</span>
      </span>
    </span>
  );
}
