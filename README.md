# XLSBuddy

An AI-powered Excel assistant. Learn Excel functions and formulas through interactive tutorials, a searchable function library, and an AI chat that answers your spreadsheet questions.

## Tech stack

| Layer | Technology |
|-------|-----------|
| Backend | FastAPI, Motor (async MongoDB), PyJWT, bcrypt, Razorpay |
| Frontend | React 19, React Router 7, Tailwind CSS, shadcn/ui |
| AI | Claude Sonnet via emergentintegrations |
| Payments | Razorpay (INR) |

## Quick start

See [LOCAL_SETUP.md](LOCAL_SETUP.md) for full local setup instructions including MongoDB, backend, and frontend configuration.

**Short version:**

```bash
# Backend
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn server:app --reload --host 0.0.0.0 --port 8001

# Frontend (separate terminal)
cd frontend
yarn install && yarn start
```

Then open http://localhost:3000.

## Project structure

```
xlsbuddy/
├── backend/
│   ├── server.py        # FastAPI app + main routes
│   ├── admin.py         # Admin/settings/payments router
│   ├── auth.py          # JWT + bcrypt
│   └── seed_data.py     # Excel functions + tutorials seed data
└── frontend/
    └── src/
        ├── pages/       # Route-level page components
        ├── components/  # Shared UI components
        ├── context/     # Auth + Theme context providers
        └── lib/         # API client + utilities
```
