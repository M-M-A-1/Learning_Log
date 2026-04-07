## 2025-02-11 - Django Query Optimization via get_object_or_404 and select_related
**Learning:** Combining object retrieval, ownership verification, and related object loading using `get_object_or_404` and `select_related` significantly reduces database roundtrips. For example, `get_object_or_404(Entry.objects.select_related('topic'), id=entry_id, topic__owner=request.user)` reduces 3 queries to 1.
**Action:** Always prefer `get_object_or_404` with ownership filters and `select_related` for fetching single objects and their context in Django views.
