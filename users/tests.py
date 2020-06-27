from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from users.models import CustomUser


class UserTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = self.client.post('/users/register/', data={
            'first_name': 'test',
            'last_name': 'case',
            'password': 'passworddd1234',
            'confirm_password': 'passworddd1234',
            'phone_number': '+2347000000061',
            'email': 'testuser@gmail.com',
            'is_staff': False,
        })

        self.admin = self.client.post('/users/register/', data={
            'first_name': 'admin',
            'last_name': '',
            'phone_number': '',
            'password': 'passworddd1234',
            'confirm_password': 'passworddd1234',
            'email': 'admin@gmail.com',
            'is_staff': True,
        })

        response = self.client.post('/login/', data={
            'email': 'testuser@gmail.com',
            'password': 'passworddd1234',
        })
        self.token = response.data['access']
        
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
    
    def test_user_profile_detail_retrieve(self):
        '''view personal profile as profile owner'''

        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_profile_retrieve_fails_for_invalid_user(self):
        self.client.credentials()
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_user_change_password(self):
        data = {
            'password': 'passworddd1234',
            'new_password': 'mypassword1234',
            'confirm_password': 'mypassword1234'
        }
        response = self.client.post(reverse('password_change'), data=data)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
    
    def test_user_change_password_fails_for_incorrect_oldpassword(self):
        data = {
            'password' : 'passworddd12',
            'new_password': 'mypassword1234',
            'confirm_password': 'mypassword1234'
        }
        response = self.client.post(reverse('password_change'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_change_password_fails_for_mismatched_newpassword(self):
        data = {
            'password' : 'passworddd1234',
            'new_password': 'mypassword12',
            'confirm_password': 'mypassword1234'
        }
        response = self.client.post(reverse('password_change'), data=data)
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)

    def test_user_change_password_fails_for_newpassword_validation(self):
        data = {
            'password' : 'passworddd1234',
            'new_password': 'password',
            'confirm_password': 'password'
        }
        response = self.client.post(reverse('password_change'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_as_admin(self):
        res = self.client.post('/login/', data={
            'email': 'admin@gmail.com',
            'password': 'passworddd1234',
        })
        self.token = res.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['is_superuser'], True)
