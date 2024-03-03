from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Task

class TaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task_data = {'title': 'Test Task', 'description': 'This is a test task', 'status': False}
        self.task = Task.objects.create(**self.task_data)
        self.url = reverse('task-list')

    def test_get_tasks(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        response = self.client.post(self.url, self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_task_detail(self):
        response = self.client.get(reverse('task-detail', kwargs={'pk': self.task.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task(self):
        updated_data = {'title': 'Updated Task', 'description': 'This task has been updated', 'status': True}
        response = self.client.put(reverse('task-detail', kwargs={'pk': self.task.id}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        response = self.client.delete(reverse('task-detail', kwargs={'pk': self.task.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
