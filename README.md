# Task Manager (Frontend + Backend + Database)

This project is a **Python task manager app** split into three parts:

- **Frontend**: Flask + HTML/JS UI (`frontend/`)
- **Backend**: FastAPI REST API (`backend/`)
- **Database**: PostgreSQL (`database/` + Docker service)

## Architecture

- Frontend runs on `http://localhost:3000`
- Backend API runs on `http://localhost:8000`
- PostgreSQL runs on `localhost:5432`

## Option A: Run all services with Docker Compose

```bash
docker compose up --build
```

Then open `http://localhost:3000`.

### See the database in terminal (Docker)

```bash
docker compose exec db psql -U taskuser -d taskdb
```

Inside `psql`:

```sql
\dt
SELECT * FROM tasks;
```

## Option B: Run locally without Docker (SQLite database file)

If Docker is not available in your VS Code terminal, use the local SQLite DB file.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt -r frontend/requirements.txt
python backend/scripts/init_db.py
```

This creates `tasks.db` in the project root.

Start backend:

```bash
uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

Start frontend in a second terminal:

```bash
python frontend/app.py
```

Show DB rows directly from terminal:

```bash
python backend/scripts/show_tasks.py
```

## API endpoints

- `GET /health`
- `GET /tasks`
- `POST /tasks`
- `PATCH /tasks/{task_id}`
- `DELETE /tasks/{task_id}`

## Local backend test

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```
