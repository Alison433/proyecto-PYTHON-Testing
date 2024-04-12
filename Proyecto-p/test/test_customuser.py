import django
import os
import pytest
import unittest
from django.test import TestCase
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

    
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fifa.settings')

django.setup()

from registroUsuario.models import Role, Contact, Identification_type, City


CustomUser = get_user_model()


class CustomUserTestCase(TestCase):
    def setUp(self):
        self.role = Role.objects.create(name_role='Admin', role_description='Administrator')
        
       
        self.bogota = City.objects.create(city_name='Bogotá')
        self.medellin = City.objects.create(city_name='Medellín')
        self.cali = City.objects.create(city_name='Cali')
        
       
        self.contact = Contact.objects.create(address='123 Main St', city=self.bogota)
        
        self.identification_type = Identification_type.objects.create(identification_type='ID', description_type_identification='Identity Card')
        
        self.user_data = {
            'username': 'testuser',
            'second_name': 'Second',
            'second_last_name': 'Last',
            'password': 'testpassword',
            'password2': 'testpassword',
            'email': 'test@example.com',
            'phone': '1234567890',
            'birth_date': '1990-01-01',
            'role': self.role,
            'contact': self.contact,
            'identification_type': self.identification_type,
           
        }

    def test_create_custom_user(self):
        user = CustomUser.objects.create_user(**self.user_data)
        self.assertEqual(user.username, self.user_data['username'])
        self.assertEqual(user.role, self.role)
        self.assertEqual(user.contact, self.contact)
        self.assertEqual(user.identification_type, self.identification_type)
        

    def test_edit_custom_user(self):
        user = CustomUser.objects.create_user(**self.user_data)
        new_username = 'newusername'
        user.username = new_username
        user.save()
        self.assertEqual(user.username, new_username)
       

    def test_delete_custom_user(self):
        user = CustomUser.objects.create_user(**self.user_data)
        user.delete()
        self.assertFalse(CustomUser.objects.filter(username=self.user_data['username']).exists())

    



