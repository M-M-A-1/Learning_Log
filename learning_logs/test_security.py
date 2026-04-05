from django.test import TestCase, Client
from django.contrib.auth.models import User
from learning_logs.models import Topic, Entry
from django.urls import reverse

class SecurityTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')
        self.topic1 = Topic.objects.create(text='Topic 1', owner=self.user1)

    def test_new_entry_idor(self):
        """Test that user2 cannot add an entry to user1's topic."""
        self.client.login(username='user2', password='password')
        url = reverse('learning_logs:new_entry', args=[self.topic1.id])

        # Try to GET the page
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404, "User2 should not be able to access user1's new_entry page")

        # Try to POST an entry
        response = self.client.post(url, {'text': 'Hacked entry'})
        self.assertEqual(response.status_code, 404, "User2 should not be able to add an entry to user1's topic")

        # Verify entry was NOT created
        self.assertFalse(Entry.objects.filter(text='Hacked entry').exists())

    def test_topic_idor(self):
        """Test that user2 cannot view user1's topic."""
        self.client.login(username='user2', password='password')
        url = reverse('learning_logs:topic', args=[self.topic1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_edit_entry_idor(self):
        """Test that user2 cannot edit user1's entry."""
        entry = Entry.objects.create(topic=self.topic1, text='Entry 1')
        self.client.login(username='user2', password='password')
        url = reverse('learning_logs:edit_entry', args=[entry.id])

        # Try to GET
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

        # Try to POST
        response = self.client.post(url, {'text': 'Hacked edit'})
        self.assertEqual(response.status_code, 404)
        entry.refresh_from_db()
        self.assertNotEqual(entry.text, 'Hacked edit')
