import React from "react";
import "@/App.css";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { Toaster } from "@/components/ui/sonner";
import { AuthProvider, useAuth } from "@/context/AuthContext";
import { ThemeProvider } from "@/context/ThemeContext";
import { ProtectedRoute } from "@/components/ProtectedRoute";

import Landing from "@/pages/Landing";
import Login from "@/pages/Login";
import Signup from "@/pages/Signup";
import Dashboard from "@/pages/Dashboard";
import Functions from "@/pages/Functions";
import FunctionDetail from "@/pages/FunctionDetail";
import Tutorials from "@/pages/Tutorials";
import TutorialDetail from "@/pages/TutorialDetail";
import Pricing from "@/pages/Pricing";
import Reviews from "@/pages/Reviews";
import Admin from "@/pages/Admin";
import Bookmarks from "@/pages/Bookmarks";

const HomeGuard = () => {
  const { user, loading } = useAuth();
  if (loading) return null;
  return user ? <Navigate to="/dashboard" replace /> : <Landing />;
};

function App() {
  return (
    <div className="App">
      <ThemeProvider>
        <AuthProvider>
          <BrowserRouter>
            <Routes>
              <Route path="/" element={<HomeGuard />} />
              <Route path="/login" element={<Login />} />
              <Route path="/signup" element={<Signup />} />
              <Route path="/pricing" element={<Pricing />} />
              <Route path="/reviews" element={<Reviews />} />
              <Route path="/dashboard" element={<ProtectedRoute><Dashboard /></ProtectedRoute>} />
              <Route path="/functions" element={<ProtectedRoute><Functions /></ProtectedRoute>} />
              <Route path="/functions/:id" element={<ProtectedRoute><FunctionDetail /></ProtectedRoute>} />
              <Route path="/tutorials" element={<Tutorials />} />
              <Route path="/tutorials/:id" element={<TutorialDetail />} />
              <Route path="/bookmarks" element={<ProtectedRoute><Bookmarks /></ProtectedRoute>} />
              <Route path="/admin" element={<ProtectedRoute><Admin /></ProtectedRoute>} />
              <Route path="*" element={<Navigate to="/" replace />} />
            </Routes>
            <Toaster richColors position="top-right" />
          </BrowserRouter>
        </AuthProvider>
      </ThemeProvider>
    </div>
  );
}
export default App;
