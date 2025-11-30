from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import CustomUser, Category, Product

class ProductTests(APITestCase):
    def setUp(self):
        
        self.admin_user = CustomUser.objects.create_user(
            email='admin@test.com', username='admin', password='password123', is_staff=True
        )
        
        self.normal_user = CustomUser.objects.create_user(
            email='user@test.com', username='user', password='password123', is_staff=False
        )
        
        self.category = Category.objects.create(name='Electronics')
        self.url = '/api/products/'

    def test_create_product_as_admin(self):
       
        self.client.force_authenticate(user=self.admin_user)
        data = {
            "name": "iPhone 15",
            "price": 999.99,
            "description": "New phone",
            "stock": 10,
            "category": self.category.id
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_product_as_user(self):
      
        self.client.force_authenticate(user=self.normal_user)
        data = {
            "name": "Hacked Phone",
            "price": 100.00,
            "description": "Bad phone",
            "stock": 5,
            "category": self.category.id
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

