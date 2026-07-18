import React from "react";
import { Link } from "react-router-dom";

const Section = ({ title, children }) => (
  <section className="mb-10">
    <h2 className="text-lg font-extrabold tracking-tight text-slate-900 dark:text-white mb-3 pb-2 border-b border-foreground/10">{title}</h2>
    <div className="space-y-3 text-slate-600 dark:text-slate-300 leading-7 text-[15px]">{children}</div>
  </section>
);

export default function PrivacyPolicy() {
  return (
    <div className="min-h-screen bg-white dark:bg-slate-950 dark:text-white">
      {/* Header */}
      <header className="border-b border-foreground/10 bg-white dark:bg-slate-950 sticky top-0 z-40">
        <div className="max-w-[860px] mx-auto px-6 py-4 flex items-center justify-between">
          <Link to="/" className="flex items-center gap-2 shrink-0">
            <div className="w-7 h-7 bg-[#002FA7] flex items-center justify-center">
              <span style={{fontFamily:"Georgia,'Times New Roman',serif",fontStyle:"italic",fontWeight:"bold",color:"white",fontSize:"12px",lineHeight:1}}>ƒx</span>
            </div>
            <span className="font-black tracking-tight dark:text-white whitespace-nowrap">XLS<span className="text-[#002FA7]">Buddy</span></span>
          </Link>
          <Link to="/" className="text-sm text-[#002FA7] font-semibold hover:underline">← Back to home</Link>
        </div>
      </header>

      <main className="max-w-[860px] mx-auto px-6 py-12 lg:py-16">
        {/* Title */}
        <div className="mb-12">
          <div className="text-[10px] font-bold tracking-[0.2em] text-[#002FA7] mb-2">LEGAL</div>
          <h1 className="text-3xl lg:text-4xl font-extrabold tracking-tight text-slate-900 dark:text-white mb-3">Privacy Policy</h1>
          <p className="text-slate-500 dark:text-slate-400 text-sm">Last updated: July 2026 · Effective immediately</p>
        </div>

        <Section title="1. Who We Are">
          <p>XLSBuddy ("we", "our", "us") is an Excel learning platform operated by Bunny Enterprises. We provide Excel function references, AI-assisted learning, tutorials, and productivity tools at <strong>xlsbuddy.com</strong>.</p>
          <p>For privacy questions, contact us at: <a href="mailto:xlsbuddy@gmail.com" className="text-[#002FA7] underline font-medium">xlsbuddy@gmail.com</a></p>
        </Section>

        <Section title="2. Information We Collect">
          <p><strong>When you create an account:</strong></p>
          <ul className="list-disc pl-5 space-y-1">
            <li>Name and email address</li>
            <li>Password (stored as a secure hash — we never store your plain password)</li>
            <li>Google account details if you use "Sign in with Google" (name, email, Google ID)</li>
          </ul>
          <p><strong>When you use the app:</strong></p>
          <ul className="list-disc pl-5 space-y-1">
            <li>AI chat messages and formula queries (used to generate responses via Groq AI)</li>
            <li>Bookmarks and saved functions</li>
            <li>Payment records if you upgrade to Pro (order ID, payment status — no card details)</li>
            <li>Login timestamps and failed login attempts (for account security)</li>
          </ul>
          <p><strong>Automatically collected:</strong></p>
          <ul className="list-disc pl-5 space-y-1">
            <li>Session cookie (<code className="bg-slate-100 dark:bg-slate-800 px-1 rounded text-sm">xlsbuddy_session</code>) for keeping you logged in</li>
            <li>Browser type and device info for displaying the app correctly</li>
          </ul>
        </Section>

        <Section title="3. How We Use Your Information">
          <ul className="list-disc pl-5 space-y-2">
            <li>To create and manage your account</li>
            <li>To provide AI responses to your Excel questions</li>
            <li>To process payments and manage your Pro subscription</li>
            <li>To send password reset emails when requested</li>
            <li>To protect your account (lockout after repeated failed logins)</li>
            <li>To improve the app based on usage patterns</li>
          </ul>
          <p>We do <strong>not</strong> sell your personal data to third parties. We do <strong>not</strong> use your data for advertising.</p>
        </Section>

        <Section title="4. Third-Party Services">
          <p>We use the following third-party services to operate XLSBuddy:</p>
          <div className="overflow-x-auto">
            <table className="w-full text-sm border border-foreground/10">
              <thead>
                <tr className="bg-slate-50 dark:bg-slate-900">
                  <th className="text-left px-4 py-2 border-b border-foreground/10 font-bold">Service</th>
                  <th className="text-left px-4 py-2 border-b border-foreground/10 font-bold">Purpose</th>
                  <th className="text-left px-4 py-2 border-b border-foreground/10 font-bold">Privacy Policy</th>
                </tr>
              </thead>
              <tbody>
                {[
                  ["MongoDB Atlas", "Database — stores your account and content", "mongodb.com/legal/privacy-policy"],
                  ["Groq AI (LLaMA)", "Powers AI chat and formula generation", "groq.com/privacy"],
                  ["Razorpay", "Payment processing for Pro subscriptions", "razorpay.com/privacy"],
                  ["Google OAuth", "Optional sign-in with Google", "policies.google.com/privacy"],
                  ["Render.com", "Backend server hosting", "render.com/privacy"],
                  ["Vercel", "Frontend hosting", "vercel.com/legal/privacy-policy"],
                ].map(([name, purpose, url]) => (
                  <tr key={name} className="border-b border-foreground/10">
                    <td className="px-4 py-2 font-medium">{name}</td>
                    <td className="px-4 py-2 text-slate-500 dark:text-slate-400">{purpose}</td>
                    <td className="px-4 py-2">
                      <a href={`https://${url}`} target="_blank" rel="noopener noreferrer" className="text-[#002FA7] underline text-xs">{url}</a>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </Section>

        <Section title="5. Cookies">
          <p>We use a single session cookie (<code className="bg-slate-100 dark:bg-slate-800 px-1 rounded text-sm">xlsbuddy_session</code>) to keep you logged in. This cookie:</p>
          <ul className="list-disc pl-5 space-y-1">
            <li>Is HttpOnly and Secure — cannot be read by JavaScript</li>
            <li>Expires after 30 days of inactivity</li>
            <li>Is deleted when you sign out</li>
          </ul>
          <p>We do not use advertising cookies, tracking pixels, or analytics cookies.</p>
        </Section>

        <Section title="6. Data Retention">
          <ul className="list-disc pl-5 space-y-2">
            <li>Your account data is kept as long as your account is active</li>
            <li>AI chat messages are not stored long-term — they are sent to Groq to generate a response and not retained by us</li>
            <li>Payment records are kept for 7 years as required by Indian tax law</li>
            <li>You can request deletion of your account at any time by emailing us</li>
          </ul>
        </Section>

        <Section title="7. Your Rights">
          <p>You have the right to:</p>
          <ul className="list-disc pl-5 space-y-1">
            <li><strong>Access</strong> — request a copy of the data we hold about you</li>
            <li><strong>Correction</strong> — update your name or email from your account</li>
            <li><strong>Deletion</strong> — request we delete your account and personal data</li>
            <li><strong>Portability</strong> — request your data in a machine-readable format</li>
          </ul>
          <p>To exercise any of these rights, email us at <a href="mailto:xlsbuddy@gmail.com" className="text-[#002FA7] underline font-medium">xlsbuddy@gmail.com</a>. We will respond within 30 days.</p>
        </Section>

        <Section title="8. Children's Privacy">
          <p>XLSBuddy is not intended for users under the age of 13. We do not knowingly collect personal information from children. If you believe a child has provided us with personal information, please contact us and we will delete it promptly.</p>
        </Section>

        <Section title="9. Data Security">
          <p>We take the following steps to protect your data:</p>
          <ul className="list-disc pl-5 space-y-1">
            <li>Passwords are hashed using bcrypt — never stored in plain text</li>
            <li>All data is transmitted over HTTPS</li>
            <li>Session tokens are stored in secure, HttpOnly cookies</li>
            <li>Account lockout after 3 failed login attempts</li>
            <li>CSRF protection on all API endpoints</li>
          </ul>
        </Section>

        <Section title="10. Changes to This Policy">
          <p>We may update this Privacy Policy from time to time. We will notify you of significant changes by posting a notice on the app or emailing you. The "Last updated" date at the top of this page reflects the most recent revision.</p>
        </Section>

        <Section title="11. Contact Us">
          <p>For any privacy concerns, data requests, or questions about this policy:</p>
          <div className="bg-slate-50 dark:bg-slate-900 border border-foreground/10 p-5 mt-3">
            <p className="font-bold text-slate-900 dark:text-white">XLSBuddy / Bunny Enterprises</p>
            <p>Email: <a href="mailto:xlsbuddy@gmail.com" className="text-[#002FA7] underline">xlsbuddy@gmail.com</a></p>
            <p>Website: <a href="https://xlsbuddy.com" className="text-[#002FA7] underline">xlsbuddy.com</a></p>
          </div>
        </Section>
      </main>

      <footer className="border-t border-foreground/10 py-6 text-center text-sm text-slate-400">
        <div className="flex items-center justify-center gap-4">
          <Link to="/privacy-policy" className="hover:text-[#002FA7] transition-colors">Privacy Policy</Link>
          <span>·</span>
          <Link to="/terms" className="hover:text-[#002FA7] transition-colors">Terms of Service</Link>
          <span>·</span>
          <Link to="/" className="hover:text-[#002FA7] transition-colors">Back to XLSBuddy</Link>
        </div>
        <p className="mt-2">© 2026 XLSBuddy · Bunny Enterprises</p>
      </footer>
    </div>
  );
}
