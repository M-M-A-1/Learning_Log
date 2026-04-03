from django.test import TestCase, RequestFactory
from django.urls import reverse
from learning_logs.models import Topic, Entry
from django.contrib.auth.models import User

class NavbarActiveStateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')

    def test_topics_link_active_on_topics_page(self):
        """Verify that 'Topics' link is active on the topics page."""
        response = self.client.get(reverse('learning_logs:topics'))
        self.assertEqual(response.status_code, 200)
        # Check for the active class and aria-current="page"
        self.assertContains(response, 'class="nav-link active"')
        self.assertContains(response, 'aria-current="page"')

    def test_topics_link_not_active_on_index_page(self):
        """Verify that 'Topics' link is not active on the home page."""
        response = self.client.get(reverse('learning_logs:index'))
        self.assertEqual(response.status_code, 200)
        # Check that it doesn't have the active class or aria-current="page"
        self.assertNotContains(response, 'class="nav-link active"')
        self.assertNotContains(response, 'aria-current="page"')
