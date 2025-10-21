from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task
from django.urls import reverse
from rest_framework.test import APIClient

class TaskUnitTests(TestCase):
    def setUp(self):
        # create user and client for API tests
        self.user = User.objects.create_user('tester', password='password123')
        self.client = APIClient()
        self.client.login(username='tester', password='password123')
        self.sample = Task.objects.create(user=self.user, title='Sample', description='for unit tests')

    def test_create_task_via_api(self):
        # POST a new task and assert it's created and attributed to the logged-in user
        url = reverse('task-list')
        data = {'title': 'API Task', 'description': 'created via API', 'priority': 'High'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['user'], self.user.id)
        self.assertEqual(response.data['title'], 'API Task')

    def test_task_str(self):
        self.assertIn('Sample', str(self.sample))
