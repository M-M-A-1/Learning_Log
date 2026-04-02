from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Topic, Entry

class TopicAuthorizationTest(TestCase):
    """Tests for authorization of topics and entries."""

    def setUp(self):
        """Create two users and a topic owned by the first user."""
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')
        self.topic1 = Topic.objects.create(text='Topic 1', owner=self.user1)

    def test_new_entry_access_denied_for_non_owner(self):
        """A user should not be able to add an entry to another user's topic."""
        self.client.login(username='user2', password='password123')

        url = reverse('learning_logs:new_entry', args=[self.topic1.id])
        data = {'text': 'This is an unauthorized entry.'}

        # This should fail with 404 if fixed. Currently it might 302 or 200.
        response = self.client.post(url, data)

        # Verify no entry was created for this topic
        self.assertEqual(Entry.objects.count(), 0)

        # Verify response is 404
        self.assertEqual(response.status_code, 404)
