
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Item

class ItemTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item_data = {'name': 'Test Item', 'description': 'Test Description'}
        self.item = Item.objects.create(**self.item_data)

    def test_create_item(self):
        response = self.client.post(reverse('create_item'), self.item_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    