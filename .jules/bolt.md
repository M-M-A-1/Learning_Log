## 2025-01-24 - Django View & Query Consolidation
**Learning:** In Django views with hierarchical ownership (User -> Topic -> Entry), query counts can be significantly reduced by combining object retrieval and ownership checks into a single `get_object_or_404` call using relationship lookups (e.g., `topic__owner=request.user`). Eagerly loading related models with `select_related()` further minimizes database trips.
**Action:** Always prefer `get_object_or_404(Model.objects.select_related('parent'), id=id, parent__owner=request.user)` for authorized child resource access.
