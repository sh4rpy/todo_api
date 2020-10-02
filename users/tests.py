from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import User


class TestAuth(APITestCase):
    def setUp(self):
        self.data = {'username': 'test', 'password': 'test'}

    def test_registration(self):
        url = '/api/v1/users/register/'
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'test')

    def test_token(self):
        url = '/api/v1/users/token/'
        user = User.objects.create_user(**self.data)
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Token.objects.count(), 1)
        self.assertEqual(Token.objects.get().user, user)
