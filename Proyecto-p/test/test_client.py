import django
import os
import pytest
import unittest
from django.test import TestCase
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError

    
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fifa.settings')

django.setup()
from registroUsuario.models import Client, CustomUser, Client_Type

class ClientTestCase(TestCase):
    def setUp(self):
        self.client_type = Client_Type.objects.create(client_type_name='Regular', client_type_description='Regular Client')
        self.user = CustomUser.objects.create(username='testuser', email='test@example.com', password='testpassword')

    def test_create_client(self):
        client = Client.objects.create(client_type=self.client_type, user=self.user)
        self.assertEqual(client.client_type, self.client_type)
        self.assertEqual(client.user, self.user)

    def test_edit_client(self):
        client = Client.objects.create(client_type=self.client_type, user=self.user)
        new_client_type = Client_Type.objects.create(client_type_name='VIP', client_type_description='VIP Client')
        client.client_type = new_client_type
        client.save()
        self.assertEqual(client.client_type, new_client_type)

    def test_delete_client(self):
        client = Client.objects.create(client_type=self.client_type, user=self.user)
        client.delete()
        self.assertFalse(Client.objects.filter(user=self.user).exists())



