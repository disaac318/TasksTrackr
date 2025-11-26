# TasksTrackr – Milestone Project 3 (Data-Centric Development)

TasksTrackr is a full-stack, data-centric task manager built with Flask, MongoDB, HTML, CSS, Bootstrap 5, and JavaScript. It lets users manage tasks, monitor deadlines, and see urgency via an automated RAG (Red–Amber–Green) system. Superadmins govern users, tasks, and categories through RBAC.

## Executive Summary
TasksTrackr demonstrates secure, scalable data-centric development for Milestone Project 3. Flask powers the backend, MongoDB Atlas stores data, and Bootstrap 5 delivers a responsive UI. RAG logic is derived from due dates; authentication uses hashing, session management, and account-freeze protection. Superadmins can adjust roles, freeze/unfreeze accounts, manage categories, and oversee all tasks. The architecture is modular and ready for enhancements like recurring tasks, calendar integration, and email/SMS reminders.

![Mockup image](docs/wireFrame/responsiveMockUp%20copy.jpg)

[Live webpage](https://tasks-tracker-77e68e91c21c.herokuapp.com)

## Table of Contents
1. Project Overview
2. Project Goals
3. Technical Architecture
4. UX / UI Design
5. Features
6. Data Model
7. Folder Structure
8. Technologies Used
9. Security Considerations
10. Testing
11. Deployment
12. Future Improvements
13. Credits

## 1. Project Overview
TasksTrackr™ organizes personal and professional work with CRUD task management and a dynamic RAG indicator based on due dates. Flask handles routing and logic; MongoDB persists users/tasks/categories; Bootstrap/Jinja2 render a responsive interface; session protection secures routes.

**Purpose & Value**
- Role-aware, secure task tracking.
- Supports users and superadmins with governance capabilities.
- Fast task entry/filtering plus dynamic RAG logic and admin oversight.

## 2. UX / UI Design
 ### Project goals: demonstrate full-stack CRUD, secure auth/sessions, and data-driven RAG logic in a clean, accessible UI.

- Responsive Bootstrap 5 grid.
- Category badges and RAG labels.
- Accordion-based task listing.
- Mobile-friendly navigation/forms. 
  
### Wireframes
<details><summary>Desktop</summary>
<img src="./docs/wireFrame/wireFrame_desktop-01.webp">
</details>
<details><summary>Tablet</summary>
<img src="./docs/wireFrame/wireFrame_tablet.webp">
</details>
<details><summary>Phone</summary>
<img src="./docs/wireFrame/wireFrame_phone.webp">
</details>

### 🎯 User Goals
- To manage tasks quickly, see urgency at a glance, use across devices. 
- To stay organised and avoid forgetting important tasks.- 
Users want a reliable tool that prevents things from slipping through the cracks.
- To prioritise work more effectively
The RAG status helps users understand what needs immediate attention and what can wait.
- To manage multiple responsibilities in one place
Users prefer consolidating personal, work, and project tasks into a single, structured system.
- To improve productivity and reduce wasted time
A clear task list helps users plan their day efficiently and complete tasks faster.
- To keep track of deadlines
Users want to see upcoming due dates clearly so they can plan ahead and avoid last-minute pressure.
- To see progress and maintain motivation
Checking off tasks provides a sense of accomplishment and encourages continued productivity.
- To adapt quickly when plans change
Users need a tool that allows easy editing, re-prioritisation, and re-organisation whenever circumstances shift.
- To access tasks anytime, anywhere
A responsive, cross-device interface ensures users can manage their obligations on the go.


### 🧑‍💼 Site Owner’s Goals
- Deliver a reliable and secure task-tracking platform. 
Ensure the system operates smoothly, protects user data, and maintains stable performance across all core features.
- Demonstrate full-stack technical competency
Showcase practical implementation of CRUD operations, authentication, session management, database modeling, and role-based access control.
- Create an intuitive and accessible user experience
Provide a clean, responsive interface that lowers user friction, enhances usability, and supports accessibility principles.
- Support meaningful oversight and governance.
Enable admins and superadmins to manage users, monitor activity, enforce rules, and maintain the system’s integrity.
- Maintain scalable and maintainable code architecture.
Structure the project to support future enhancements, including new features, improved logic, and integration with external services.
- Use data effectively to drive system logic.
Apply due-date calculations, RAG priority rules, and category structures to deliver an intelligent, data-centric experience.
- Deploy a trustworthy, production-ready application.
Ensure the project can be hosted securely (Heroku/Render/MongoDB Atlas), with clear documentation for installation and maintenance.

### 🎯 Target Audience
- Busy Professionals.
Individuals working in office environments, healthcare, IT, education, or customer-facing roles who manage multiple responsibilities and need a structured tool to stay on top of daily tasks.
- Students and Learners.
College, university, and online learners who must juggle lectures, assignments, deadlines, exams, and personal commitments.
- Freelancers and Self-Employed Workers.
Designers, writers, developers, consultants, and gig workers who need to keep track of client projects, delivery dates, and personal workloads.
- Parents and Home Managers.
Individuals managing family schedules, home tasks, appointments, bills, and personal activities who benefit from a simple, centralised system.
- Small Teams or Community Groups.
Small organisations, clubs, volunteer groups, or project teams that need to coordinate tasks, deadlines, and responsibilities.
- Individuals with Organisation or Time-Management Challenges.
People who struggle with planning, remembering deadlines, or staying focused and benefit from clear visual cues like RAG priority indicators.
- People Who Prefer Digital Productivity Tools.
Users who enjoy structured, digital task management rather than paper planners, sticky notes, or unorganised spreadsheets.


### User Stories
#### What I need to know as a First-time User
- As an individual using the app for the first time, I need to know how to add a task quickly so I can immediately start organising my day without confusion.
- As a student who is new to the app, I need to understand how the RAG colours work so I can instantly see which assignments or deadlines are most urgent.
- As a professional logging in for the first time, I need to know how to categorise my tasks clearly so I can separate work priorities and manage multiple projects effectively.

#### What I need to know as Returning Customer
- As a returning individual user, I want to instantly see which tasks are urgent so I can plan my day without feeling overwhelmed.
- As a returning individual user, I want to pick up where I left off so I can continue completing my personal tasks without redoing anything.
- As a returning student, I want to view all upcoming deadlines at a glance so I don’t fall behind on assignments or revision.
- As a returning student, I want to update my tasks quickly so I can adjust my workload whenever my study schedule changes.
- As a returning professional, I want the dashboard to show today’s critical work tasks so I can manage my workload efficiently.
- As a returning professional, I want to revise tasks or deadlines easily so I can adapt to changes in my projects or responsibilities.
  



## 3. Technical Architecture
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


## 5. Features
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

## 6. Data Model (MongoDB)
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

## 7. Folder Structure
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

## 8. Technologies Used
- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript.
- **Backend:** Flask, Jinja2, Flask-PyMongo.
- **Database:** MongoDB Atlas.
- **Other:** Werkzeug (password hashing), Git/GitHub, Heroku/Render (deployment target).

## 9. Security Considerations
- Passwords hashed (Werkzeug); sessions for auth.
- Account freeze after 3 failed logins; superadmin can unfreeze.
- Role-guarded routes (superadmin-only admin UI/actions).
- Reset tokens with 1-hour expiry (link flashed; no email transport in this build).
- Delete guarded: owner/superadmin; admin view delete for any task.

## 10. Testing
- Manual test plan in `TESTING.md` (auth, tasks, admin, responsiveness, accessibility, data integrity).
- Commands: `python3 -m py_compile app.py` (syntax), `flake8 app.py` (style if available).
- Validate HTML/CSS via W3C after deployment.
### HTML Validation
<details><summary>HTML</summary>
<img src="./docs/validation/html validation.png">
</details>

### CSS Validation
<details><summary>style.css</summary>
<img src="./docs/validation/css validation.png">
</details>

### Performance
Google Lighthouse in Google Chrome Developer Tools was used to test the performance of the website.

<details><summary>Performance Test on Lighthouse</summary>
<img src="./docs/validation/lightHouse.png">
</details>

###  Performing tests on various devices

The website was tested on the following devices:

-  Imac 24-inch M1 2021
-  Ipad Pro 11 2021
-  Apple Iphone 14 Pro

In addition, the website was tested using Google Chrome Developer Tools Device Toggeling option for all available device options.

### Browser compatibility

The website was tested on the following browsers:

-  Safari
-  Google Chrome
-  Mozilla Firefox
-  Microsoft Edge
  

## Development Challenges and Resolutions
### Problem 1: Flask–MongoDB Connection Failure
- The first and most significant challenge I encountered was establishing a reliable connection between Flask and MongoDB Atlas. I spent two days troubleshooting—searching social media posts, YouTube tutorials, and various online forums—but no solution worked.
I eventually sought support from Code Institute’s tutoring service. Tom explained that Flask-PyMongo has changed substantially since version 3, and many online examples (including the connection string from MongoDB Atlas) no longer work without adjustments. After reviewing my configuration, he identified the issue within the connection URI and instructed me to modify it by replacing the deprecated parameter with  "&tlsAllowInvalidCertificates=true."

Once updated, Flask-PyMongo connected successfully.  This issue would have been extremely difficult to resolve independently, and the tutor’s guidance was essential in unblocking my progress.

### Problem 2: Bootstrap Navbar Not Responding
- Another major challenge occurred when my Bootstrap navbar and accordion stopped functioning. After extensive trial and error and reviewing online forums, I discovered that the issue stemmed from loading Bootstrap JavaScript twice—once in the <head> and again at the bottom of the <body>.

This double initialisation caused event conflicts that broke interactive components such as:
Navbar collapse
Accordion collapse
Tooltips

Reviewing the official Bootstrap documentation clarified the problem. The fix was straightforward:
- Remove the Bootstrap JS bundle from the <"head">
- Keep only the script loaded at the bottom of the <"body">
  
This ensures JavaScript loads after the HTML content, preventing broken events and restoring all interactive behaviour.

### Problem 3: Accordion Items Opening Simultaneously
- The third challenge was that all accordion items opened at the same time, despite Bootstrap’s accordion component being designed to allow only one open item by default.
  
The cause was that all accordion sections shared identical IDs (collapseOne, headingOne), which violates Bootstrap’s requirement for unique identifiers.

The solution involved:
- Assigning unique IDs using {{ loop.index }} (e.g., heading1, collapse1, heading2, collapse2, etc.)
- Setting aria-expanded="false" for collapsed defaults
- Removing the show class so no item opens automatically
- Ensuring data-bs-parent="#accordionTasks" was present so only one accordion pane opens at a time

After implementing these changes, the accordion behaved correctly, allowing only one section to expand at once.

### Problem 4: Deprecated Delete Route in Flask-PyMongo
  The final challenge involved deprecated MongoDB operations. I originally used:
  - mongo.db.tasks.remove() in my delete route
  
  However, remove() is deprecated in modern versions of PyMongo. The correct approach is to use:
- delete_one() for deleting a single document
- delete_many() for deleting multiple documents
- I learned this from watching youtube toturial on mongoDB presented by BroCode (https://www.youtube.com/watch?v=c2M-rlkkT5o&t=2799s)
  
Updating the delete route to use delete_one() resolved the issue and aligned the project with current MongoDB best practices.

## What I Learned Along the Way
1. The Importance of Understanding Version Changes
One of the biggest lessons I learned was that documentation and tutorials quickly become outdated when libraries release new versions. Flask-PyMongo introduced breaking changes after version 3, which meant examples from MongoDB Atlas and online guides no longer matched the current implementation. This experience reinforced the value of always checking version-specific documentation and release notes rather than relying solely on older tutorials.

2. Debugging Requires Methodical Investigation
The connection issue between Flask and MongoDB demonstrated the importance of patience and structured debugging. I learned to examine error messages closely, test assumptions one step at a time, validate environment variables, and isolate potential causes. Trial-and-error becomes productive only when paired with a deliberate method.

3. Front-End Behaviour Depends on Proper Script Management
The Bootstrap issue taught me that loading JavaScript incorrectly can break an entire interface. I learned the correct script order—HTML first, then JavaScript—and gained a clearer understanding of how event-driven components rely on proper initialisation. This knowledge is essential for building stable, responsive UIs.

4. Unique Identifiers Are Critical for Interactive Components
The accordion issue showed me how even small details, such as duplicated IDs, can completely disrupt functionality. I learned to generate dynamic, unique IDs using Jinja’s loop.index and to pay attention to ARIA attributes and Bootstrap’s required structure. Good UI behaviour relies on clean and predictable markup.

5. Deprecated Code Can Lead to Silent Failures
The removal of MongoDB’s remove() method reinforced the need to recognise deprecated functions and adopt modern equivalents such as delete_one(). Staying updated with library changes prevents technical debt and ensures stability in production.

6. Knowing When to Seek Help Is Part of Being a Developer
Reaching out to a tutor was essential in resolving an issue that would have taken much longer on my own. This experience taught me that collaboration and asking for assistance are not signs of weakness—they are part of professional practice. Effective problem-solving often involves knowing when a fresh pair of eyes can help.

7. Documentation and Official Sources Are Essential
When fixing Bootstrap and MongoDB issues, I learned that official documentation is often the fastest route to accurate solutions. Community forums are useful, but authoritative references provide reliable answers that match current versions.

8. Small Errors Can Cause Major Issues
From missing symbols in a URI to duplicated IDs in an accordion, I learned that attention to detail is crucial. One misplaced character or duplicated attribute can break an entire feature. This reinforced the importance of careful reviewing, validation, and incremental testing.


## 11. Deployment
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

## 12. Future Improvements
- Email/SMS reminders; notifications.
- Enforce task edit ownership (delete already does).
- Indexes/schema validation in Mongo.
- Automated tests and accessibility validations.
- Recurring tasks, calendar integration, configurable RAG thresholds.

## 13. Credits
- Flaticon for the landing page image.
- Flask, Flask-PyMongo, MongoDB, Bootstrap, Werkzeug.
- Code Institute for project framework guidance.
