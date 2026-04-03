## 2025-05-15 - Indexing Ordered Fields
**Learning:** Adding `db_index=True` to fields used in `order_by` (like `date_added`) is a critical optimization for Django applications as the dataset grows. While the impact on small datasets is minimal, it prevents linear scan performance degradation for sorting operations.
**Action:** Always check `views.py` for `order_by` calls and ensure the corresponding model fields are indexed.
