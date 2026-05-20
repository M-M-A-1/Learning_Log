# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Commands
- Run development server: `python manage.py runserver`
- Apply migrations: `python manage.py migrate`
- Create migrations: `python manage.py makemigrations`
- Run all tests: `python manage.py test`
- Run tests for a specific app: `python manage.py test <app_name>`
- Create superuser: `python manage.py createsuperuser`
- Django shell: `python manage.py shell`
- Collect static files: `python manage.py collectstatic`

## Architecture
The project is a Django-based web application called "Learning Log".

### Application Structure
- `accounts`: Handles user lifecycle including registration, authentication (login/logout), and profile management.
- `learning_logs`: Implements the core functionality.
    - **Topics**: Users can create and list topics they are learning about.
    - **Entries**: Users can add, read, and edit journal entries associated with a specific topic.

### Data Model
- Users (managed by `accounts`) can create `Topic`s.
- Each `Topic` can have multiple `Entry`s.
- Both `Topic` and `Entry` are linked to a user.

### Tech Stack
- Framework: Django 6.0.1
- Database: SQLite (local), PostgreSQL (production via `dj-database-url`)
- Static Files: Whitenoise
- WSGI Server: Gunicorn
- Frontend: Django Templates with `django-bootstrap5`

## Production Configuration
The app is configured for production readiness using:
- **Environment Variables**: `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` are sourced from the environment.
- **Database**: Uses `dj-database-url` to configure the database connection via the `DATABASE_URL` environment variable.
- **Static Files**: `Whitenoise` is used to serve static files directly from the application.

## UI & Styling
- **Styling**: Uses `django-bootstrap5` for a responsive and consistent UI.
- **Error Handling**: Custom 404 and 500 error pages are implemented.
