from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Topic, Entry

class SecurityTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')
        self.topic1 = Topic.objects.create(text='Topic 1', owner=self.user1)
        self.entry1 = Entry.objects.create(topic=self.topic1, text='Entry 1')

    def test_new_entry_idor(self):
        """Test that user2 cannot add an entry to user1's topic."""
        self.client.login(username='user2', password='password123')
        url = reverse('learning_logs:new_entry', kwargs={'topic_id': self.topic1.id})

        response = self.client.post(url, {'text': 'Malicious entry'})
        self.assertEqual(response.status_code, 404)

        # Verify entry was not created
        self.assertFalse(Entry.objects.filter(topic=self.topic1, text='Malicious entry').exists())

    def test_edit_entry_idor(self):
        """Test that user2 cannot edit user1's entry."""
        self.client.login(username='user2', password='password123')
        url = reverse('learning_logs:edit_entry', kwargs={'entry_id': self.entry1.id})

        response = self.client.post(url, {'text': 'Edited by user2'})
        self.assertEqual(response.status_code, 404)

        # Verify entry was not edited
        self.entry1.refresh_from_db()
        self.assertEqual(self.entry1.text, 'Entry 1')

    def test_topic_view_idor(self):
        """Test that user2 cannot view user1's topic."""
        self.client.login(username='user2', password='password123')
        url = reverse('learning_logs:topic', kwargs={'topic_id': self.topic1.id})

        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
