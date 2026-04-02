## 2025-05-15 - [IDOR in new_entry]
**Vulnerability:** Insecure Direct Object Reference (IDOR) in `new_entry` view.
**Learning:** While `topic` and `edit_entry` views had ownership checks, `new_entry` only fetched the topic by ID without verifying the owner, allowing unauthorized data injection.
**Prevention:** Always verify ownership of parent objects (like `Topic`) before allowing creation of child objects (like `Entry`) that reference them. Use `get_object_or_404` for all object lookups in views.
