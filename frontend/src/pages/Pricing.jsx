import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { Header } from "@/components/Header";
import { api } from "@/lib/api";
import { useAuth } from "@/context/AuthContext";
import { Button } from "@/components/ui/button";
import { toast } from "sonner";
import { Check, Crown, Sparkle, ShieldCheck, Gift } from "@phosphor-icons/react";

function daysLeft(isoDate) {
  if (!isoDate) return 0;
  const exp = new Date(isoDate);
  const now = new Date();
  return Math.max(0, Math.ceil((exp - now) / (1000 * 60 * 60 * 24)));
}

export default function Pricing() {
  const navigate = useNavigate();
  const { user } = useAuth();
  const [config, setConfig] = useState(null);
  const [loading, setLoading] = useState(false);
  const [checkoutReady, setCheckoutReady] = useState(Boolean(window.Razorpay));
  const razorpayKey = process.env.REACT_APP_RAZORPAY_KEY_ID || config?.razorpay_key_id;

  useEffect(() => {
    api.get("/config").then((r) => setConfig(r.data));
  }, []);

  useEffect(() => {
    if (window.Razorpay) { setCheckoutReady(true); return undefined; }
    if (document.getElementById("razorpay-script")) return undefined;
    const s = document.createElement("script");
    s.id = "razorpay-script";
    s.src = "https://checkout.razorpay.com/v1/checkout.js";
    s.async = true;
    s.onload = () => setCheckoutReady(true);
    s.onerror = () => toast.error("Could not load secure checkout. Please try again.");
    document.body.appendChild(s);
    return () => { s.onload = null; s.onerror = null; };
  }, []);

  const handleTrial = async () => {
    if (!user) { navigate("/login"); return; }
    setLoading(true);
    try {
      await api.post("/payments/start-trial");
      toast.success("7-day free trial started! Enjoy Pro features.");
      setTimeout(() => window.location.reload(), 1200);
    } catch (e) {
      toast.error(e.response?.data?.detail || "Could not start trial");
    } finally {
      setLoading(false);
    }
  };

  const handleUpgrade = async () => {
    if (!user) { navigate("/login"); return; }
    if (!config?.razorpay_configured) {
      toast.error("Payments not yet configured. Please try later.");
      return;
    }
    if (!window.Razorpay) {
      toast.error("Secure checkout is still loading. Please try again.");
      return;
    }
    if (!razorpayKey) {
      toast.error("Payments are not configured. Please try again later.");
      return;
    }
    setLoading(true);
    try {
      const { data } = await api.post("/payments/create-order", { plan: "pro_monthly" });
      const options = {
        key: razorpayKey,
        amount: data.amount,
        currency: data.currency,
        name: "XLSBuddy Pro",
        description: "Monthly Pro Plan",
        order_id: data.order_id,
        prefill: { name: user.name, email: user.email, contact: "" },
        theme: { color: "#002FA7" },
        method: { upi: true, card: true, netbanking: true, wallet: true },
        handler: async (res) => {
          try {
            await api.post("/payments/verify", {
              razorpay_order_id: res.razorpay_order_id,
              razorpay_payment_id: res.razorpay_payment_id,
              razorpay_signature: res.razorpay_signature,
            });
            toast.success("Welcome to Pro! Reloading…");
            setTimeout(() => window.location.reload(), 1200);
          } catch (e) {
            toast.error(e.response?.data?.detail || "Verification failed");
          } finally {
            setLoading(false);
          }
        },
        modal: { ondismiss: () => setLoading(false) },
      };
      const rz = new window.Razorpay(options);
      rz.on("payment.failed", (response) => {
        toast.error(response.error?.description || "Payment failed. Please try again.");
        setLoading(false);
      });
      rz.open();
    } catch (e) {
      toast.error(e.response?.data?.detail || "Could not start payment");
    }
  };

  const price = config?.pro_price_inr ?? 299;
  const limit = config?.free_daily_chat_limit ?? 5;
  const trialDays = user?.is_trial ? daysLeft(user.trial_expires_at) : 0;
  const hasUsedTrial = Boolean(user?.trial_started_at);

  const renderProCTA = () => {
    // Paid Pro (not trial)
    if (user?.is_pro && !user?.is_trial) {
      return (
        <Button disabled className="rounded-none w-full h-12 bg-white text-black" data-testid="pro-current">
          <Crown size={16} weight="fill" className="mr-2" /> You're on Pro
        </Button>
      );
    }

    // On trial
    if (user?.is_trial) {
      return (
        <div className="space-y-3">
          <div className="rounded-lg bg-white/10 border border-white/20 px-4 py-3 text-center">
            <p className="text-white font-bold text-sm">Trial active — {trialDays} day{trialDays !== 1 ? "s" : ""} left</p>
            <p className="text-white/60 text-xs mt-0.5">Upgrade before trial ends to keep Pro access</p>
          </div>
          <Button
            onClick={handleUpgrade}
            disabled={loading || !checkoutReady || !config?.razorpay_configured}
            className="rounded-none w-full h-12 bg-white text-black hover:bg-white/90 font-bold disabled:opacity-50"
          >
            {loading ? "Opening checkout…" : <><Sparkle size={16} weight="fill" className="mr-2" /> Upgrade to Pro — ₹{price}/mo</>}
          </Button>
          <button
            onClick={async () => {
              if (!window.confirm("Cancel your free trial and return to the Free plan?")) return;
              setLoading(true);
              try {
                await api.post("/payments/cancel-trial");
                toast.success("Trial cancelled. You're back on the Free plan.");
                setTimeout(() => window.location.reload(), 1200);
              } catch (e) {
                toast.error(e.response?.data?.detail || "Could not cancel trial");
              } finally {
                setLoading(false);
              }
            }}
            disabled={loading}
            className="w-full text-xs text-white/40 hover:text-white/70 underline py-1 transition-colors"
          >
            Cancel trial
          </button>
        </div>
      );
    }

    // Trial expired (has used trial, not pro)
    if (hasUsedTrial && !user?.is_pro) {
      return (
        <div className="space-y-3">
          <p className="text-xs text-white/60 text-center">Your free trial has ended</p>
          <Button
            onClick={handleUpgrade}
            disabled={loading || !checkoutReady || !config?.razorpay_configured}
            className="rounded-none w-full h-12 bg-white text-black hover:bg-white/90 font-bold disabled:opacity-50"
            data-testid="upgrade-button"
          >
            {loading ? "Opening checkout…" : <><Sparkle size={16} weight="fill" className="mr-2" /> Upgrade to Pro — ₹{price}/mo</>}
          </Button>
        </div>
      );
    }

    // New user — show free trial CTA
    return (
      <div className="space-y-2">
        <Button
          onClick={handleTrial}
          disabled={loading}
          className="rounded-none w-full h-12 bg-white text-black hover:bg-white/90 font-bold disabled:opacity-50"
          data-testid="trial-button"
        >
          {loading ? "Starting trial…" : <><Gift size={16} weight="fill" className="mr-2" /> Start 7-Day Free Trial</>}
        </Button>
        <p className="text-xs text-white/50 text-center">No payment needed · Full Pro access for 7 days</p>
      </div>
    );
  };

  return (
    <div className="min-h-screen page-bg">
      <Header />
      <main className="max-w-[1200px] mx-auto px-6 lg:px-10 py-12 lg:py-16" data-testid="pricing-page">
        <div className="overline klein mb-3">PRICING</div>
        <h1 className="page-title mb-3">Simple. Honest. One plan.</h1>
        <p className="text-muted-foreground max-w-2xl mb-12">
          Start with a 7-day free trial. No credit card required.
        </p>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-0 border-l border-t border-foreground/15">
          {/* FREE */}
          <div className="border-r border-b border-foreground/15 p-8 lg:p-10 bg-white" data-testid="plan-free">
            <div className="overline mb-4">FREE</div>
            <div className="flex items-baseline gap-2 mb-6">
              <span className="metric-title">₹0</span>
              <span className="text-muted-foreground">/forever</span>
            </div>
            <ul className="space-y-3 mb-10">
              {[
                "55+ core Excel functions",
                "11 free tutorials",
                "Visual mini-sheet examples",
                `${limit} AI chats per day`,
                "Search across functions & tutorials",
              ].map((f) => (
                <li key={f} className="flex items-start gap-2 text-sm">
                  <Check size={18} weight="bold" className="klein shrink-0 mt-0.5" />
                  {f}
                </li>
              ))}
            </ul>
            <Button
              variant="outline"
              className="rounded-none w-full h-12 border-foreground/30"
              disabled
              data-testid="free-current-plan"
            >
              {user && !user.is_pro ? "Your current plan" : "Get started free"}
            </Button>
          </div>

          {/* PRO */}
          <div className="border-r border-b border-foreground/15 p-8 lg:p-10 bg-black text-white relative" data-testid="plan-pro">
            <div className="absolute top-0 right-0 bg-klein text-white text-xs font-bold px-4 py-1 overline">MOST POPULAR</div>
            <div className="overline mb-4 text-white/60 flex items-center gap-2">
              <Crown size={14} weight="fill" /> PRO
            </div>
            <div className="flex items-baseline gap-2 mb-1">
              <span className="metric-title text-[#7AA0FF]">₹{price}</span>
              <span className="text-white/60">/month</span>
            </div>
            <p className="text-xs text-white/50 mb-2">INR billing · UPI, cards, netbanking</p>

            {/* 7-day trial badge */}
            {!hasUsedTrial && !user?.is_pro && (
              <div className="flex items-center gap-2 bg-emerald-500/20 border border-emerald-500/40 rounded-lg px-3 py-2 mb-5">
                <Gift size={14} className="text-emerald-400 shrink-0" weight="fill" />
                <span className="text-emerald-300 text-xs font-bold">First 7 days FREE — no card needed</span>
              </div>
            )}

            <ul className="space-y-3 mb-8">
              {[
                "Everything in Free",
                "All 76 functions incl. LAMBDA, Dynamic Arrays",
                "All 22 tutorials (incl. advanced guides)",
                "Unlimited AI chats (Claude Sonnet 4.5)",
                "Save & organize chat history",
                "Email support",
              ].map((f) => (
                <li key={f} className="flex items-start gap-2 text-sm">
                  <Check size={18} weight="bold" className="text-[#7AA0FF] shrink-0 mt-0.5" />
                  {f}
                </li>
              ))}
            </ul>

            {renderProCTA()}

            {!config?.razorpay_configured && !user?.is_pro && !user?.is_trial && !hasUsedTrial && (
              <p className="text-xs text-white/50 mt-3 text-center">
                Payments coming soon. Start your free trial now.
              </p>
            )}
          </div>
        </div>

        <div className="mt-12 grid grid-cols-1 md:grid-cols-3 gap-0 border-l border-t border-foreground/15">
          <div className="border-r border-b border-foreground/15 p-6 bg-secondary">
            <ShieldCheck size={28} className="klein mb-3" weight="duotone" />
            <div className="font-bold mb-1">Secure payments</div>
            <p className="text-sm text-muted-foreground">Powered by Razorpay. PCI-DSS compliant. UPI, cards, wallets.</p>
          </div>
          <div className="border-r border-b border-foreground/15 p-6 bg-white">
            <Gift size={28} className="klein mb-3" weight="duotone" />
            <div className="font-bold mb-1">7-day free trial</div>
            <p className="text-sm text-muted-foreground">Full Pro access for 7 days. No credit card required to start.</p>
          </div>
          <div className="border-r border-b border-foreground/15 p-6 bg-secondary">
            <Crown size={28} className="klein mb-3" weight="duotone" />
            <div className="font-bold mb-1">Built for power users</div>
            <p className="text-sm text-muted-foreground">From analysts to students — designed for daily Excel workflows.</p>
          </div>
        </div>
      </main>
    </div>
  );
}
