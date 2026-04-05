from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Topic, Entry

class LearningLogsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.other_user = User.objects.create_user(username='otheruser', password='password')
        self.topic = Topic.objects.create(text='Test Topic', owner=self.user)
        self.entry = Entry.objects.create(topic=self.topic, text='Test Entry')
        self.client = Client()
        self.client.login(username='testuser', password='password')

    def test_topics_view(self):
        response = self.client.get(reverse('learning_logs:topics'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Topic')

    def test_topic_detail_view(self):
        response = self.client.get(reverse('learning_logs:topic', args=[self.topic.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Entry')

    def test_topic_detail_view_denied_for_other_user(self):
        self.client.login(username='otheruser', password='password')
        response = self.client.get(reverse('learning_logs:topic', args=[self.topic.id]))
        self.assertEqual(response.status_code, 404)

    def test_edit_entry_view(self):
        response = self.client.get(reverse('learning_logs:edit_entry', args=[self.entry.id]))
        self.assertEqual(response.status_code, 200)

    def test_edit_entry_view_denied_for_other_user(self):
        self.client.login(username='otheruser', password='password')
        response = self.client.get(reverse('learning_logs:edit_entry', args=[self.entry.id]))
        self.assertEqual(response.status_code, 404)

    def test_new_entry_view_denied_for_other_user(self):
        self.client.login(username='otheruser', password='password')
        response = self.client.get(reverse('learning_logs:new_entry', args=[self.topic.id]))
        self.assertEqual(response.status_code, 404)
