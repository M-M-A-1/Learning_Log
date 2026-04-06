## 2025-05-15 - [Hierarchical IDOR Vulnerability]
**Vulnerability:** Insecure Direct Object Reference (IDOR) in entry creation.
**Learning:** Creation views for child resources (e.g., `Entry`) often forget to verify the user's permission on the parent resource (e.g., `Topic`), especially when the parent ID is passed via URL.
**Prevention:** Always use `get_object_or_404` with an ownership filter (e.g., `owner=request.user`) for the parent resource in creation views. For existing resources, use relationship traversal (e.g., `topic__owner=request.user`) to ensure the user owns the parent.
