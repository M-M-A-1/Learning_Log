from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Topic

class SuccessMessageTest(TestCase):
    """Tests for success messages."""

    def setUp(self):
        """Set up a test user and log them in."""
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_new_topic_success_message(self):
        """Test that adding a new topic displays a success message."""
        url = reverse('learning_logs:new_topic')
        response = self.client.post(url, {'text': 'Test Topic'}, follow=True)
        self.assertContains(response, "New topic added successfully!")

    def test_new_entry_success_message(self):
        """Test that adding a new entry displays a success message."""
        topic = Topic.objects.create(text='Test Topic', owner=self.user)
        url = reverse('learning_logs:new_entry', args=[topic.id])
        response = self.client.post(url, {'text': 'Test Entry'}, follow=True)
        self.assertContains(response, "New entry added successfully!")

    def test_edit_entry_success_message(self):
        """Test that editing an entry displays a success message."""
        topic = Topic.objects.create(text='Test Topic', owner=self.user)
        entry = topic.entry_set.create(text='Original Entry')
        url = reverse('learning_logs:edit_entry', args=[entry.id])
        response = self.client.post(url, {'text': 'Edited Entry'}, follow=True)
        self.assertContains(response, "Entry updated successfully!")
