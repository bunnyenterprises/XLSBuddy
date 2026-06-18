import axios from "axios";

const BACKEND_URL = "http://127.0.0.1:8000";

export const API = `${BACKEND_URL}/api`;

export const api = axios.create({
  baseURL: API,
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("em_token");

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});

api.interceptors.response.use(
  (r) => r,
  (err) => {
    if (err.response?.status === 401) {
      localStorage.removeItem("em_token");
      localStorage.removeItem("em_user");

      if (
        !window.location.pathname.startsWith("/login") &&
        !window.location.pathname.startsWith("/signup") &&
        window.location.pathname !== "/"
      ) {
        window.location.href = "/login";
      }
    }

    return Promise.reject(err);
  }
);