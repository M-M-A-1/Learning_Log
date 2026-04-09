## 2025-05-15 - Consolidating Retrieval and Authorization in Views
**Learning:** Combining object retrieval, ownership verification, and related object pre-fetching (using `select_related`) into a single `get_object_or_404` call significantly reduces query counts and improves application security by ensuring authorization is handled at the database level.
**Action:** Always prefer `get_object_or_404(Model.objects.select_related('related'), id=id, owner=request.user)` for user-specific resource access.
