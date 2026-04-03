from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Topic, Entry

class LearningLogTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.topic = Topic.objects.create(text='Test Topic', owner=self.user)
        self.entry = Entry.objects.create(topic=self.topic, text='Test Entry')

    def test_topics_page(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('learning_logs:topics'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Topic')

    def test_topic_page(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('learning_logs:topic', args=[self.topic.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Topic')
        self.assertContains(response, 'Test Entry')
