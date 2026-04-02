## 2025-05-15 - [Added success messages for user actions]
**Learning:** Providing immediate feedback through success messages (e.g., Bootstrap alerts) is a key micro-UX enhancement that improves user confidence and makes the application feel more responsive.
**Action:** Always include success/error notifications using the Django messages framework when performing CRUD operations. Use `django-bootstrap5`'s `{% bootstrap_messages %}` tag for easy integration.
