## 2025-05-14 - Namespaced Navbar Active States
**Learning:** In namespaced Django apps, `request.resolver_match.url_name` only returns the local name. Using `request.resolver_match.view_name` provides the full namespaced path (e.g., 'learning_logs:index'), which is required for reliable active state highlighting in the navigation bar.
**Action:** Always check the app namespace and use `view_name` for conditional navbar styling to ensure accurate visual feedback.
