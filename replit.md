# Portoo — Flask Portfolio App

A personal portfolio web application for Brendan Wilson Santoso, built with Flask and a TiDB Cloud (MySQL) database.

## Stack

- **Backend**: Python / Flask with blueprints
- **Database**: TiDB Cloud (MySQL-compatible), accessed via SQLAlchemy + PyMySQL
- **Image hosting**: Cloudinary
- **Email**: Resend API
- **Frontend**: Vanilla HTML/CSS/JS in `frontend/`

## How to run

The workflow `Start application` runs `python app.py`, which starts Flask on port 5000.

All credentials are loaded from `.env` via `python-dotenv`. The env file contains:
- `SECRET_KEY` — Flask session secret
- `DATABASE_URL` — TiDB Cloud MySQL connection string
- `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`
- `RESEND_API_KEY`

## Project structure

```
app.py          — Flask app entry point, blueprint registration
config.py       — Config class reading env vars
model.py        — SQLAlchemy models
backend/        — Flask blueprints (admin: login, profiles, skills, experience, projects, upload, contact)
frontend/       — HTML templates and static assets (CSS, JS, images)
```

## Notes

- `static_url_path=""` is set so Flask serves `/admin/css/...` and `/img/...` directly from `frontend/` without a `/static/` prefix.
- The admin panel is at `/admin/dashboard` (requires login).

## User preferences

- Keep existing project structure and stack.
