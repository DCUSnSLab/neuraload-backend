from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from vehicle.models import Device, UserDeviceLink

User = get_user_model()


class UserAPITestCase(APITestCase):
    def test_user_registration(self):
        data = {
            'userName': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123',
            'phone_number': '01012345678'
        }
        response = self.client.post('/api/account/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email='test@example.com').exists())

    def test_user_login(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        data = {
            'email': 'test@example.com',
            'password': 'testpass123'
        }
        response = self.client.post('/api/account/login/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('tokens', response.data)


class DeviceAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)

    def test_vehicle_registration(self):
        data = {
            'vehicles_model_name': 'Hyundai Porter Electric',
            'max_load_capacity': 1.0,
            'device_unique_id': '#test123456789'
        }
        response = self.client.post('/api/vehicles/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Device.objects.filter(device_unique_id='#test123456789').exists())
