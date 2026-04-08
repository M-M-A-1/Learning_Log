## 2025-05-15 - [IDOR in Hierarchical Resources]
**Vulnerability:** Insecure Direct Object Reference (IDOR) in `new_entry` view.
**Learning:** Even when a parent resource (Topic) is correctly protected in its own view, child resource creation views (Entry) must also verify that the current user owns the parent resource to prevent cross-user data injection.
**Prevention:** Use `get_object_or_404` with an ownership filter (e.g., `owner=request.user` or `topic__owner=request.user`) in every view that retrieves or modifies user-specific data.
