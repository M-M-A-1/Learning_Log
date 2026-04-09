## 2025-05-14 - IDOR in Hierarchical Resource Creation
**Vulnerability:** Insecure Direct Object Reference (IDOR) in `new_entry` view.
**Learning:** Even if detail and edit views have ownership checks, creation views for child resources (like `Entry` belonging to `Topic`) can be overlooked. If the parent resource is fetched by ID without an ownership check, any authenticated user can inject data into another user's parent resource.
**Prevention:** Always use `get_object_or_404` with an ownership filter for the parent resource when creating child resources.
