from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class UserTests(APITestCase):

    def setUp(self):
        get_user_model().objects.create(username='zelda', password='123', email='zelda@mail.com')
        get_user_model().objects.create(username='link', password='456', email='link@mail.com')

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('account-register')
        data = {'username': 'evangilo', 'password': '123', 'email': 'evangilo@mail.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {'id': 3, 'username': 'evangilo', 'email': 'evangilo@mail.com'})

    def test_level_access_account_details(self):
        """
        Ensures that only the owner has access to account data.
        """
        user = get_user_model().objects.get(username='zelda')
        client = APIClient()
        client.force_authenticate(user=user)

        response200 = client.get('/api/account/1/')
        response403 = client.get('/api/account/2/')

        self.assertEqual(response200.status_code, status.HTTP_200_OK)
        self.assertEqual(response200.data, {'id': 1, 'username': 'zelda', 'email': 'zelda@mail.com'})
        self.assertEqual(response403.status_code, status.HTTP_403_FORBIDDEN)
