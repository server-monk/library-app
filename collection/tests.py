from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from collection.models import Book, Author


class BookTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = self.client.post(reverse('register'), data={
            'first_name': 'admin',
            'last_name': '',
            'phone_number': '',
            'password': 'passworddd1234',
            'confirm_password': 'passworddd1234',
            'email': 'admin@gmail.com',
            'is_staff': True,
        })
        self.book = self.client.post(reverse('add'), data={
            'book_id': '1',
            'book_title': 'Harry Potter',
            'author': 'J. K. Rowling',
            'description': 'and the sorcerer\'s stone',
            'genre': 'Fantasy',
            'isbn': '978-25-456-5457',
            'publisher': 'ABC',
            'publish_year': '2004',
            'edition': 'Second',
            'book_format': 'pdf',
            'language': 'en',
        })
        response = self.client.post('/login/', data={
            'email': 'admin@gmail.com',
            'password': 'passworddd1234',
        })
        # print(self.admin)
        # print(self.book)
        # print(response)
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer' + self.token)

    def test_addbook_view(self):
        response = self.client.get(reverse('all-books'))
        # print(self.book)
        # print(response)
        # self.client.credentials()
        # response = self.client.post(reverse('add'))
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_booklist_view(self):
        response = self.client.get(reverse('all-books'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_update_view(self):
        data = {
            'book_id': '1',
            'book_title': 'Harry Potter',
            'author': 'J. K. Rowling',
            'description': 'and the sorcerer\'s stone',
            'genre': 'Fantasy',
            'isbn': '978-25-456-5457',
            'publisher': 'ABC',
            'publish_year': '2004',
            'edition': 'Second',
            'book_format': 'pdf',
            'language': 'en',
        }
        response = self.client.get(reverse('update'), data=data)
        print(response)
        # self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

