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
from registroUsuario.models import City  

class CityCreationTestCase(TestCase):
    def test_create_city(self):
       
        city = City.objects.create(
            city_name='New York'
        )
        
        
        self.assertIsNotNone(city)
        self.assertEqual(city.city_name, 'New York')

