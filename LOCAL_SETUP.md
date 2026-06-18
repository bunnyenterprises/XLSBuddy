# XLSBUDDY — Run Locally (No Emergent)

Complete instructions to run this app on your own computer.

## Prerequisites

Install these on your computer first:

| Tool | Version | Download |
|------|---------|----------|
| **Python** | 3.10+ | https://www.python.org/downloads/ |
| **Node.js** | 18+ | https://nodejs.org/ |
| **Yarn** | latest | `npm install -g yarn` |
| **MongoDB** | 6.0+ | https://www.mongodb.com/try/download/community |

Verify install: open terminal and run
```bash
python --version
node --version
yarn --version
mongod --version
```

---

## 1. Extract the project

If you got `XLSBUDDY_source.tar.gz`:
```bash
tar -xzf XLSBUDDY_source.tar.gz
cd XLSBUDDY
```

Folder structure:
```
XLSBUDDY/
├── backend/
└── frontend/
```

---

## 2. Start MongoDB

**Option A** — local MongoDB:
```bash
# macOS (homebrew)
brew services start mongodb-community

# Linux
sudo systemctl start mongod

# Windows: start "MongoDB" service from Services panel
```

**Option B** — free MongoDB Atlas (cloud, no install):
1. Go to https://www.mongodb.com/cloud/atlas/register
2. Create free cluster
3. Click "Connect" → "Drivers" → copy connection string (looks like `mongodb+srv://user:pass@cluster.mongodb.net`)
4. Use this in step 3 below

---

## 3. Backend setup (FastAPI)

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate          # macOS / Linux
# venv\Scripts\activate            # Windows

# Install dependencies
pip install -r requirements.txt
pip install emergentintegrations --extra-index-url https://d33sy5i8bnduwe.cloudfront.net/simple/
```

### Edit `backend/.env`

Open `backend/.env` and set:
```
MONGO_URL="mongodb://localhost:27017"
DB_NAME="XLSBUDDY"
CORS_ORIGINS="*"
EMERGENT_LLM_KEY="sk-emergent-7D0EfD77d7d704a15F"
JWT_SECRET="any-long-random-string-you-pick"
```

If using **MongoDB Atlas**, replace `MONGO_URL` with your Atlas connection string.

### Run backend

```bash
uvicorn server:app --reload --host 0.0.0.0 --port 8001
```

Backend will be at: **http://localhost:8001**
Test it: open http://localhost:8001/api/ in browser → should see `{"message":"XLSBUDDY API","status":"ok"}`

Keep this terminal open.

---

## 4. Frontend setup (React)

Open a **new terminal**:

```bash
cd frontend

# Install dependencies (this can take 2-3 minutes)
yarn install
```

### Edit `frontend/.env`

Open `frontend/.env` and set:
```
REACT_APP_BACKEND_URL=http://localhost:8001
WDS_SOCKET_PORT=3000
```

> ⚠️ Important: change the URL to `http://localhost:8001` (not the Emergent preview URL).

### Run frontend

```bash
yarn start
```

Frontend will open at: **http://localhost:3000**

---

## 5. First-time login

Once both backend and frontend are running:

1. Open http://localhost:3000
2. Click **Get Started** → create your account
3. To make yourself admin, sign up with email **`rajel.chavan6@gmail.com`** (the admin email is hardcoded in `backend/admin.py` — change it there if you want a different admin email)
4. After login → click your name (top-right) → **Admin Console**
5. Go to **Settings** tab → paste your Razorpay keys + Google review URL → Save

---

## 6. Razorpay setup (for payments)

1. Sign up at https://dashboard.razorpay.com
2. Go to **Settings → API Keys → Generate Test Keys**
3. Copy `Key Id` (starts with `rzp_test_`) and `Key Secret`
4. Paste in your local app: **Admin Console → Settings**

Test cards (any UPI/card works in test mode):
- Card: `4111 1111 1111 1111`
- Any future expiry, any CVV

---

## 7. (Optional) Production build

For a single optimized build:

```bash
# Backend (already production-ready with uvicorn)

# Frontend
cd frontend
yarn build
# Serve the build/ folder with any static server, e.g.:
npx serve -s build -l 3000
```

---

## Common issues

| Problem | Fix |
|---------|-----|
| `pip install` fails on `bcrypt` | Install build tools: `apt install build-essential` (Linux), Xcode CLI (macOS) |
| `yarn start` shows blank page | Check `REACT_APP_BACKEND_URL` in `frontend/.env` matches your backend URL |
| Login fails | Check backend terminal for errors; ensure MongoDB is running |
| `MONGO_URL` connection error | Start MongoDB service or use Atlas string |
| AI chat returns error | Verify `EMERGENT_LLM_KEY` is set in `backend/.env` |
| `emergentintegrations` not found | Re-run: `pip install emergentintegrations --extra-index-url https://d33sy5i8bnduwe.cloudfront.net/simple/` |

---

## Project structure reference

```
backend/
├── server.py           # FastAPI app, all main routes
├── admin.py            # Admin/settings/reviews/payments router
├── auth.py             # JWT + bcrypt
├── seed_data.py        # 65 Excel functions + 8 tutorials
├── requirements.txt
└── .env

frontend/
├── package.json
├── tailwind.config.js
├── postcss.config.js
├── craco.config.js
├── .env
└── src/
    ├── index.js
    ├── App.js / App.css / index.css
    ├── lib/api.js
    ├── context/AuthContext.jsx
    ├── components/
    │   ├── Header.jsx
    │   ├── ProtectedRoute.jsx
    │   ├── VisualExample.jsx
    │   └── ui/                  # shadcn components (40+ files)
    └── pages/
        ├── Landing.jsx, Login.jsx, Signup.jsx
        ├── Dashboard.jsx
        ├── Functions.jsx, FunctionDetail.jsx
        ├── Tutorials.jsx, TutorialDetail.jsx
        ├── Chat.jsx
        ├── Pricing.jsx, Reviews.jsx
        └── Admin.jsx
```

---

## Tech stack

- **Backend**: FastAPI, Motor (async MongoDB), bcrypt, PyJWT, Razorpay, emergentintegrations
- **Frontend**: React 19, React Router 7, Tailwind, shadcn/ui, Phosphor Icons, axios, sonner
- **AI**: Claude Sonnet 4.5 via emergentintegrations (universal LLM key)
- **Payments**: Razorpay (INR)

---

You're all set. The app runs 100% locally — no Emergent dependency needed at runtime.
