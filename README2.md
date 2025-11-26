# TasksTrackr – Milestone Project 3 (Data-Centric Development)

TasksTrackr is a full-stack, data-centric task manager built with Flask, MongoDB, HTML, CSS, Bootstrap 5, and JavaScript. It lets users manage tasks, monitor deadlines, and see urgency via an automated RAG (Red–Amber–Green) system. Superadmins govern users, tasks, and categories through RBAC.

## Executive Summary
TasksTrackr demonstrates secure, scalable data-centric development for Milestone Project 3. Flask powers the backend, MongoDB Atlas stores data, and Bootstrap 5 delivers a responsive UI. RAG logic is derived from due dates; authentication uses hashing, session management, and account-freeze protection. Superadmins can adjust roles, freeze/unfreeze accounts, manage categories, and oversee all tasks. The architecture is modular and ready for enhancements like recurring tasks, calendar integration, and email/SMS reminders.

## Table of Contents
1. Project Overview
2. Technical Architecture
3. UX / UI Design
4. Features
5. Data Model
6. Folder Structure
7. Technologies Used
8. Security Considerations
9. Testing
10. Deployment
11. Future Improvements
12. Credits

## 1. Project Overview
TasksTrackr organizes personal and professional work with CRUD task management and a dynamic RAG indicator based on due dates. Flask handles routing and logic; MongoDB persists users/tasks/categories; Bootstrap/Jinja2 render a responsive interface; session protection secures routes.

**Purpose & Value**
- Role-aware, secure task tracking.
- Supports users and superadmins with governance capabilities.
- Fast task entry/filtering plus dynamic RAG logic and admin oversight.

## 2. Technical Architecture
```
End User (browser)
    |
    |  HTTPS
    v
Flask App (app.py)
  - Routing, auth, sessions
  - CRUD controllers
  - RAG computation
    |
    | Jinja2 templates / Flask-PyMongo
    v
MongoDB Atlas
  - users
  - tasks
  - categories
    ^
    | data rendered to templates
    v
Frontend
  - HTML5/Jinja2
  - CSS/Bootstrap 5
  - JS (flash handling)
```

## 3. UX / UI Design
**User goals:** manage tasks quickly, see urgency at a glance, use across devices.  
**Project goals:** demonstrate full-stack CRUD, secure auth/sessions, and data-driven RAG logic in a clean, accessible UI.

- Responsive Bootstrap 5 grid.
- Category badges and RAG labels.
- Accordion-based task listing.
- Mobile-friendly navigation/forms. (Wireframes: add Figma/Balsamiq links if available.)

## 4. Features
**User Authentication**
- Registration, login, logout.
- Password hashing; freeze after 3 failed logins.
- Password reset tokens (shown on request for demo).
- Session-based access control.

**Task Management (CRUD)**
- Create, edit, delete tasks.
- Filter tasks by category.
- Ownership checks on delete (owner or superadmin).
- RAG highlighting: red (due/overdue), amber (≤2 days), green (3+ days).

**Admin / Superadmin**
- Admins: freeze/unfreeze accounts (not superadmins/self); view and delete any task with owner filter; manage categories (add; delete blocked if in use).
- Superadmins: all admin powers plus promote/demote users and delete users (not self/other superadmins) along with their tasks.

**Planned Enhancements**
- Email/SMS reminders.
- Calendar integration; recurring tasks.
- Dark mode; configurable RAG thresholds.
- API endpoints/mobile integration.

## 5. Data Model (MongoDB)
**users**
```json
{
  "username": "alice",
  "password": "<hashed>",
  "role": "superadmin",
  "is_frozen": false,
  "failed_logins": 0,
  "reset_token": "<token>",
  "reset_expires": "<datetime>"
}
```
**tasks**
```json
{
  "task_name": "Buy groceries",
  "task_description": "Milk, eggs, bread",
  "category_name": "Shopping",
  "is_urgent": "on",
  "due_date": "2025-01-20",
  "created_by": "alice"
}
```
**categories**
```json
{ "category_name": "Shopping" }
```

Relationships are implicit via `created_by` and `category_name`. For production, add indexes on `users.username`, `tasks.created_by`/`due_date`, and `categories.category_name`; optionally store category ObjectIds for stricter integrity.

## 6. Folder Structure
```
TasksTrackr/
├── app.py
├── requirements.txt
├── README.md
├── TESTING.md
├── env.py (optional, local vars)
├── static/
│   ├── css/style.css
│   ├── js/flash-alerts.js
│   └── img/clipboard.png
└── templates/
    ├── base.html
    ├── welcome.html
    ├── login.html
    ├── register.html
    ├── add_task.html
    ├── edit_task.html
    ├── my_tasks.html
    ├── admin_users.html
    ├── admin_tasks.html
    └── admin_categories.html
```

## 7. Technologies Used
- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript.
- **Backend:** Flask, Jinja2, Flask-PyMongo.
- **Database:** MongoDB Atlas.
- **Other:** Werkzeug (password hashing), Git/GitHub, Heroku/Render (deployment target).

## 8. Security Considerations
- Passwords hashed (Werkzeug); sessions for auth.
- Account freeze after 3 failed logins; superadmin can unfreeze.
- Role-guarded routes (superadmin-only admin UI/actions).
- Reset tokens with 1-hour expiry (link flashed; no email transport in this build).
- Delete guarded: owner/superadmin; admin view delete for any task.

## 9. Testing
- Manual test plan in `TESTING.md` (auth, tasks, admin, responsiveness, accessibility, data integrity).
- Commands: `python3 -m py_compile app.py` (syntax), `flake8 app.py` (style if available).
- Validate HTML/CSS via W3C after deployment.

## 10. Deployment
1) **Prerequisites:** Python 3.x, pip/virtualenv; MongoDB URI.  
2) **Install deps:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3) **Env vars:** `MONGO_URI`, `SECRET_KEY`, `IP`, `PORT` (export or `.env`).  
4) **Run:** `python3 app.py` (debug=False by default).  
5) **Superadmin:** set `role: "superadmin"` (and `is_frozen: false`, `failed_logins: 0`) on a user in Mongo, then use Admin UI.

## 11. Future Improvements
- Email/SMS reminders; notifications.
- Enforce task edit ownership (delete already does).
- Indexes/schema validation in Mongo.
- Automated tests and accessibility validations.
- Recurring tasks, calendar integration, configurable RAG thresholds.

## 12. Credits
- Flask, Flask-PyMongo, MongoDB, Bootstrap, Werkzeug.
- Code Institute for project framework guidance.
