from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Topic, Entry

class SecurityTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')
        self.topic1 = Topic.objects.create(text='Topic 1', owner=self.user1)

    def test_new_entry_idor(self):
        """Test that a user cannot add an entry to another user's topic."""
        self.client.login(username='user2', password='password123')

        # User 2 tries to add an entry to User 1's topic
        response = self.client.post(reverse('learning_logs:new_entry', args=[self.topic1.id]), {
            'text': 'Malicious entry'
        })

        # Should be 404 or forbidden
        self.assertEqual(response.status_code, 404)

        # Verify no entry was added
        self.assertEqual(Entry.objects.filter(topic=self.topic1).count(), 0)

    def test_topic_access_idor(self):
        """Verify that topic view already has protection."""
        self.client.login(username='user2', password='password123')
        response = self.client.get(reverse('learning_logs:topic', args=[self.topic1.id]))
        self.assertEqual(response.status_code, 404)
