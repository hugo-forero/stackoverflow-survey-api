# Stack Overflow Survey Insights API

A production-ready REST API built with FastAPI, exposing insights from the
Stack Overflow Developer Survey dataset.

Built as a portfolio project to demonstrate professional Python backend
development practices.

## Tech stack

- **FastAPI** — async REST framework
- **SQLAlchemy 2.0** — async ORM with typed models
- **Alembic** — database migrations
- **Pydantic / pydantic-settings** — data validation and config management
- **SQLite** (local) / **PostgreSQL** (production)
- **Render** — cloud deployment

## Project status

🚧 In active development

| Phase | Description | Status |
|---|---|---|
| 1 | Project structure & environment | ✅ Done |
| 2 | Data models & database setup | 🔄 In progress |
| 3 | API endpoints & business logic | ⏳ Pending |
| 4 | Auth, observability & CI/CD | ⏳ Pending |
| 5 | Deployment to Render | ⏳ Pending |

## Local setup

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/stackoverflow-survey-api
cd stackoverflow-survey-api

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Run migrations
alembic upgrade head

# Start the server
uvicorn app.main:app --reload
```

## Environment variables

| Variable | Description | Default |
|---|---|---|
| `APP_NAME` | Application name | — |
| `APP_VERSION` | Current version | — |
| `ENVIRONMENT` | `development` or `production` | — |
| `DATABASE_URL` | SQLAlchemy async DB URL | — |
