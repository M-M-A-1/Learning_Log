## 2025-05-22 - Missing Ownership Check in Nested Resource Creation
**Vulnerability:** Insecure Direct Object Reference (IDOR) in `new_entry` view.
**Learning:** Even if a view retrieves a parent resource (Topic), it must explicitly check if the current user owns that resource before allowing the creation of related child resources (Entry).
**Prevention:** Always verify ownership of parent resources in creation views for nested objects. Use `get_object_or_404` for resource retrieval to avoid internal server errors on missing IDs.
