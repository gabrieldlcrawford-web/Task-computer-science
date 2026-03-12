# Task Manager (Frontend + Backend + Database)

This project is a **Python task manager app** split into three parts:

- **Frontend**: Flask + HTML/JS UI (`frontend/`)
- **Backend**: FastAPI REST API (`backend/`)
- **Database**: PostgreSQL (`database/` + Docker service)

## Architecture

- Frontend runs on `http://localhost:3000`
- Backend API runs on `http://localhost:8000`
- PostgreSQL runs on `localhost:5432`

## Run with Docker Compose

```bash
docker compose up --build
```

Then open `http://localhost:3000`.

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
