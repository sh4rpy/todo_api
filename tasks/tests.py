from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from users.models import User
from .models import Task, TaskHistory


class TestTasks(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')
        self.api_client = APIClient()
        self.api_client.force_authenticate(user=self.user)
        self.url = '/api/v1/tasks/'
        self.data = {
            'title': 'title',
            'description': 'description',
            'status': 'new',
            'deadline': '2030-10-10',
        }
        self.patch_data = {
            'title': 'changed title',
            'description': 'changed description',
            'status': 'planned',
            'deadline': '2030-10-20',
        }

    def test_creating_task(self):
        response = self.api_client.post(self.url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, self.data['title'])

    def test_changing_task(self):
        new_task = Task.objects.create(**self.data, user=self.user)
        response = self.api_client.patch(self.url + f'{new_task.pk}/', self.patch_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get().title, self.patch_data['title'])

    def test_change_history(self):
        new_task = Task.objects.create(**self.data, user=self.user)
        self.assertEqual(TaskHistory.objects.count(), 1)
        self.assertEqual(TaskHistory.objects.first().title, self.data['title'])
        self.api_client.patch(self.url + f'{new_task.pk}/', self.patch_data, format='json')
        self.assertEqual(TaskHistory.objects.count(), 2)
        self.assertEqual(TaskHistory.objects.first().title, self.patch_data['title'])

    def test_filtering(self):
        Task.objects.create(**self.data, user=self.user)
        Task.objects.create(**self.patch_data, user=self.user)
        response = self.api_client.get(self.url, format='json')
        self.assertEqual(len(response.json()), 2)
        response = self.api_client.get(self.url, {'status': 'new'}, format='json')
        self.assertEqual(len(response.json()), 1)
        response = self.api_client.get(self.url, {'deadline': '2030-10-20'}, format='json')
        self.assertEqual(len(response.json()), 1)

    def test_task_validation(self):
        incorrect_data = {
            'title': 'changed title',
            'description': 'changed description',
            'status': 'planned',
            'deadline': '2010-10-10',
        }
        response = self.api_client.post(self.url, incorrect_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['non_field_errors'][0], 'Дата завершения меньше сегодняшней')
