# Bolt's Journal - Learning Log Performance

## 2025-05-14 - Initial Assessment
**Learning:** Found that common Django patterns in the views are causing redundant database queries. Specifically, checking ownership by accessing a ForeignKey attribute (`topic.owner`) triggers an additional query even if only the ID is needed. Also, the absence of indexes on `date_added` will lead to O(n log n) sorting overhead as the dataset grows.
**Action:** Prioritize database-level optimizations (indexes) and query efficiency (reducing query count) for the most frequent access patterns.
