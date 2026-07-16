import React from "react";
import { Link } from "react-router-dom";

const Section = ({ title, children }) => (
  <section className="mb-10">
    <h2 className="text-lg font-extrabold tracking-tight text-slate-900 dark:text-white mb-3 pb-2 border-b border-foreground/10">{title}</h2>
    <div className="space-y-3 text-slate-600 dark:text-slate-300 leading-7 text-[15px]">{children}</div>
  </section>
);

export default function Terms() {
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
          <h1 className="text-3xl lg:text-4xl font-extrabold tracking-tight text-slate-900 dark:text-white mb-3">Terms of Service</h1>
          <p className="text-slate-500 dark:text-slate-400 text-sm">Last updated: July 2026 · By using XLSBuddy, you agree to these terms.</p>
        </div>

        <Section title="1. Acceptance of Terms">
          <p>By accessing or using XLSBuddy ("the Service") at xlsbuddy.com, you agree to be bound by these Terms of Service and our <Link to="/privacy-policy" className="text-[#002FA7] underline font-medium">Privacy Policy</Link>. If you do not agree, do not use the Service.</p>
          <p>These terms are governed by the laws of India. Any disputes shall be subject to the jurisdiction of courts in India.</p>
        </Section>

        <Section title="2. Description of Service">
          <p>XLSBuddy provides:</p>
          <ul className="list-disc pl-5 space-y-1">
            <li>An indexed library of Excel functions with explanations, syntax, and examples</li>
            <li>AI-powered chat assistant for Excel questions (powered by Groq / LLaMA)</li>
            <li>Formula generator tool</li>
            <li>Guided interactive tutorials</li>
            <li>A Pro subscription with access to advanced content</li>
          </ul>
          <p>We reserve the right to modify, suspend, or discontinue any part of the Service at any time with reasonable notice.</p>
        </Section>

        <Section title="3. User Accounts">
          <ul className="list-disc pl-5 space-y-2">
            <li>You must be at least 13 years old to create an account</li>
            <li>You are responsible for maintaining the confidentiality of your password</li>
            <li>You are responsible for all activity that occurs under your account</li>
            <li>You must provide accurate information when creating your account</li>
            <li>One person may not maintain more than one free account</li>
            <li>Accounts showing signs of abuse may be suspended or deleted</li>
          </ul>
        </Section>

        <Section title="4. Pro Subscription and Payments">
          <p><strong>Pricing:</strong> The Pro plan is currently priced at <strong>₹299 per month</strong>. Prices may change with 30 days' notice.</p>
          <p><strong>Payment:</strong> Payments are processed securely by Razorpay. We accept UPI, credit/debit cards, net banking, and wallets. We do not store your card details.</p>
          <p><strong>What Pro includes:</strong></p>
          <ul className="list-disc pl-5 space-y-1">
            <li>Access to all Advanced-difficulty functions (XLOOKUP, FILTER, SORT, UNIQUE, dynamic arrays, financial functions)</li>
            <li>Unlimited AI chat messages per day</li>
            <li>Access to Pro-only tutorials</li>
          </ul>
          <p><strong>Cancellation:</strong> You can cancel your Pro subscription at any time from your account settings. Access continues until the end of the current billing period.</p>
          <p><strong>Refund Policy:</strong> We offer a <strong>7-day refund</strong> if you are not satisfied. Contact us at <a href="mailto:rajel88@gmail.com" className="text-[#002FA7] underline">rajel88@gmail.com</a> within 7 days of payment. No refunds after 7 days.</p>
        </Section>

        <Section title="5. Free Tier Limits">
          <p>Free accounts are subject to usage limits including:</p>
          <ul className="list-disc pl-5 space-y-1">
            <li>Limited AI chat messages per day (limit set by admin)</li>
            <li>Access to free-tier functions and tutorials only</li>
            <li>Advanced and Pro content is locked behind the Pro subscription</li>
          </ul>
          <p>We reserve the right to adjust free tier limits at any time.</p>
        </Section>

        <Section title="6. Acceptable Use">
          <p>You agree not to:</p>
          <ul className="list-disc pl-5 space-y-1">
            <li>Use the Service for any unlawful purpose</li>
            <li>Attempt to bypass, hack, or reverse-engineer any part of the Service</li>
            <li>Use automated bots or scripts to scrape content from XLSBuddy</li>
            <li>Share your Pro account credentials with others</li>
            <li>Submit harmful, offensive, or misleading content through AI chat</li>
            <li>Attempt to circumvent usage limits or payment requirements</li>
          </ul>
          <p>Violation of these rules may result in immediate account suspension without refund.</p>
        </Section>

        <Section title="7. AI-Generated Content">
          <p>XLSBuddy uses AI (Groq / LLaMA) to generate responses to your Excel questions. Please note:</p>
          <ul className="list-disc pl-5 space-y-1">
            <li>AI responses may occasionally be incorrect — always verify formulas before using them in important work</li>
            <li>We are not responsible for errors in AI-generated content</li>
            <li>Do not share sensitive or confidential business data in AI chat messages</li>
            <li>Your chat inputs may be sent to Groq's servers to generate responses (see their privacy policy)</li>
          </ul>
        </Section>

        <Section title="8. Intellectual Property">
          <p>All content on XLSBuddy — including tutorials, explanations, UI design, and code — is owned by Bunny Enterprises and protected by Indian copyright law.</p>
          <p>You may not copy, reproduce, or distribute our content without written permission. Excel is a registered trademark of Microsoft Corporation — XLSBuddy is an independent learning platform and is not affiliated with Microsoft.</p>
          <p>Content you create (bookmarks, notes) remains yours. By submitting reviews or feedback, you grant us a non-exclusive license to display it on the platform.</p>
        </Section>

        <Section title="9. Disclaimer of Warranties">
          <p>XLSBuddy is provided "as is" and "as available" without warranties of any kind. We do not guarantee that:</p>
          <ul className="list-disc pl-5 space-y-1">
            <li>The Service will be uninterrupted or error-free</li>
            <li>AI-generated formulas will be accurate for your specific use case</li>
            <li>The Service will meet your specific requirements</li>
          </ul>
        </Section>

        <Section title="10. Limitation of Liability">
          <p>To the maximum extent permitted by applicable law, Bunny Enterprises shall not be liable for any indirect, incidental, or consequential damages arising from your use of XLSBuddy, including but not limited to data loss, business loss, or financial loss resulting from AI-generated content.</p>
          <p>Our total liability to you shall not exceed the amount you paid us in the 3 months prior to the claim.</p>
        </Section>

        <Section title="11. Termination">
          <p>We reserve the right to terminate or suspend your account at any time for violation of these Terms. You may terminate your account at any time by contacting us.</p>
          <p>Upon termination, your right to use the Service ceases immediately. We may retain certain data as required by law.</p>
        </Section>

        <Section title="12. Changes to Terms">
          <p>We may update these Terms from time to time. We will notify you of material changes via email or a notice on the app. Continued use of the Service after changes constitutes acceptance of the new Terms.</p>
        </Section>

        <Section title="13. Contact">
          <div className="bg-slate-50 dark:bg-slate-900 border border-foreground/10 p-5">
            <p className="font-bold text-slate-900 dark:text-white">XLSBuddy / Bunny Enterprises</p>
            <p>Email: <a href="mailto:rajel88@gmail.com" className="text-[#002FA7] underline">rajel88@gmail.com</a></p>
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
