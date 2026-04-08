from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Topic, Entry

class SecurityTests(TestCase):
    """Security tests for the learning_logs application."""

    def setUp(self):
        """Create two users and a topic for User B."""
        self.user_a = User.objects.create_user(username='user_a', password='password123')
        self.user_b = User.objects.create_user(username='user_b', password='password123')
        self.topic_b = Topic.objects.create(text="User B's Private Topic", owner=self.user_b)

    def test_idor_new_entry(self):
        """Verify that User A cannot add an entry to User B's topic."""
        self.client.login(username='user_a', password='password123')

        # User A tries to add an entry to User B's topic
        response = self.client.post(f'/new_entry/{self.topic_b.id}/', {'text': 'Exploit attempt'})

        # Should return a 404 because of get_object_or_404(Topic, id=topic_id, owner=request.user)
        self.assertEqual(response.status_code, 404)

        # Check that no entry was actually added to Topic B
        self.assertFalse(Entry.objects.filter(topic=self.topic_b, text='Exploit attempt').exists())

    def test_idor_view_topic(self):
        """Verify that User A cannot view User B's topic."""
        self.client.login(username='user_a', password='password123')
        response = self.client.get(f'/topic/{self.topic_b.id}/')
        self.assertEqual(response.status_code, 404)

    def test_idor_edit_entry(self):
        """Verify that User A cannot edit User B's entry."""
        entry_b = Entry.objects.create(topic=self.topic_b, text="User B's Entry")

        self.client.login(username='user_a', password='password123')
        response = self.client.post(f'/edit_entry/{entry_b.id}/', {'text': 'Exploit attempt'})
        self.assertEqual(response.status_code, 404)

        # Verify text hasn't changed
        entry_b.refresh_from_db()
        self.assertEqual(entry_b.text, "User B's Entry")
