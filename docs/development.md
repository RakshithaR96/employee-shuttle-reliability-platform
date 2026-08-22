# Development Guide

## Backend

```bash
cd backend
python -m venv .venv
# Windows Git Bash:
source .venv/Scripts/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API: http://localhost:8000/ and http://localhost:8000/api/health

Run tests:

```bash
pytest
```

## Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend: http://localhost:5173

## PostgreSQL

```bash
docker compose up -d db
```

The database password in `docker-compose.yml` is development-only.

## Privacy

The application does not continuously track drivers. GPS verification will be
introduced later as an event-based capability for defined trip events.
