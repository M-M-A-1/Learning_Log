## 2025-05-15 - [IDOR in new_entry view]
**Vulnerability:** Authenticated users could add entries to topics owned by other users by crafting a POST request to `learning_logs:new_entry` with a `topic_id` that they did not own.
**Learning:** While the `topic` and `edit_entry` views had ownership checks, the `new_entry` view was missing this verification after fetching the `Topic` object. This highlight the importance of consistent ownership validation across all views that interact with user-specific resources.
**Prevention:** Always verify that the current user (`request.user`) is the owner of any related resource before allowing modifications or additions. Use `get_object_or_404` to handle non-existent resources gracefully.
