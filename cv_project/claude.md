# Project Context: cv_project

## Overview
`cv_project` is a Django-based web application designed to serve as a personal CV / portfolio site.

## Directory Structure
```
cv_project/
├── manage.py
├── db.sqlite3
├── cvsite/               # Main project configuration app
│   ├── settings.py       # Settings, installed apps, static file configs
│   ├── urls.py           # Root URL routing
│   ├── wsgi.py / asgi.py # Server interfaces
├── cv/                   # Main application for CV content
│   ├── models.py         # Data models for CV/portfolio sections
│   ├── views.py          # View logic
│   ├── urls.py           # App-level routing
│   ├── admin.py          # Admin interface registration
│   ├── static/cv/        # Static assets
│   │   ├── css/style.css
│   │   ├── img/
│   │   └── js/script.js
│   └── templates/cv/     # HTML templates
│       ├── base.html
│       └── index.html
```

## Common Commands

### Development Server
```bash
python manage.py runserver
```

### Database Management
```bash
# Make new migrations based on models changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### Testing
```bash
# Run tests for the cv app
python manage.py test cv
```

### Admin User Creation
```bash
python manage.py createsuperuser
```

## Code Style & Guidelines

- **Architecture**: Standard Django MVT (Model-View-Template) pattern. Keep business logic in `models.py` or helper modules, presentation logic in `views.py` / templates.
- **Naming Conventions**:
  - Python: `snake_case` for variables/functions, `PascalCase` for classes (Models, Views).
  - Templates: HTML files in `cv/templates/cv/` using Django template tag formatting (`{% %}`, `{{ }}`).
- **Static Assets**: All CSS, JS, and image assets for the `cv` app should be stored inside `cv/static/cv/` and referenced using `{% load static %}` in templates.