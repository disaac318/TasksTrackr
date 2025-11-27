# Testing & Validation Plan

This document outlines manual checks to satisfy functionality, usability, responsiveness, accessibility, and data integrity requirements.

## Functional Flows
- **Auth**: Register → login → logout; attempt 3 bad passwords (account freezes); verify frozen login blocked; reset password via reset link; login succeeds and clears freeze.
- **Tasks (user)**: Add task (with/without urgent flag), edit task, delete task (confirm prompt), filter by category; RAG colors reflect due dates (overdue/on 0 = red, ≤2 days = amber, otherwise green).
- **Admin**: Freeze/unfreeze user (not superadmins/self), view all tasks, filter by owner, delete any task, add category, block deletion of in-use category.
- **Superadmin**: All admin checks plus promote/demote users and delete users (not self/other superadmins) along with their tasks.
- **Session guardrails**: Add/edit/delete require login; admin pages blocked to non-admin; superadmin-only actions blocked to admin (403).

## Responsiveness
- Resize to mobile (<768px), tablet, desktop:
  - Navbar toggle works without covering content.
  - Forms and tables remain usable (Admin Users buttons hidden on mobile except delete).
  - Dropdowns and accordions fit the viewport.

## Accessibility
- Labels: Ensure every input/select has a visible label (current forms use floating labels).
- Contrast: Check primary text and buttons against WCAG AA using a contrast checker.
- Screen reader hints: Verify meaningful link/button text (icons paired with text); flash alerts announce content.
- Motion: Flash blink is brief; confirm it’s not distracting—disable if necessary.

## Validation
- **HTML/CSS**: Run W3C HTML and CSS validators on rendered pages; resolve any errors/warnings.
- **PEP 8**: `python3 -m py_compile app.py` (syntax) and `flake8 app.py` or similar for style if available.
- **Dependencies**: Install from `requirements.txt` to ensure `bson/pymongo` present.

## Data Integrity
- Confirm tasks respect ownership: non-superadmin cannot delete another user’s task.
- Password reset clears `failed_logins` and `is_frozen`, removes `reset_token`/`reset_expires`.
- Category deletion blocked when tasks reference it.

## Known Considerations
- Password reset link is flashed on the page (no email delivery). Production should send email.
- Edit task does not enforce ownership (delete does). 
