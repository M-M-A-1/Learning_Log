from django.test import TestCase, Client
from django.contrib.auth.models import User
from learning_logs.models import Topic, Entry
from django.urls import reverse

class SecurityTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')
        self.topic1 = Topic.objects.create(text='Topic 1', owner=self.user1)

    def test_new_entry_idor(self):
        """Test that a user cannot add an entry to another user's topic."""
        self.client.login(username='user2', password='password123')
        url = reverse('learning_logs:new_entry', args=[self.topic1.id])

        # User 2 tries to add an entry to User 1's topic
        response = self.client.post(url, {'text': 'Malicious entry'})

        # It should return 404 or redirect with error, but currently it likely succeeds (302 redirect)
        # and adds the entry.

        # Check if entry was created
        self.assertEqual(Entry.objects.filter(topic=self.topic1).count(), 0)
        self.assertEqual(response.status_code, 404)
