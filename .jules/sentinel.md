## 2025-05-14 - IDOR in Hierarchical Resource Creation
**Vulnerability:** Insecure Direct Object Reference (IDOR) in the `new_entry` view.
**Learning:** While `topic` and `edit_entry` views had manual ownership checks, the `new_entry` view lacked any validation that the `topic_id` provided in the URL belonged to the currently authenticated user. This allowed any logged-in user to add entries to any topic by guessing or iterating topic IDs.
**Prevention:** Always verify ownership of the parent resource when creating a child resource. Using `get_object_or_404(ParentModel, id=parent_id, owner=request.user)` is a concise and safe pattern in Django to combine retrieval, existence check, and authorization in a single database query.
