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
from servicioTecnico.models import Service_Type

class ServiceTypeTestCase(TestCase):
    def setUp(self):
        self.type_data = {
            'service_type_name': 'Instalacion',
            'service_type_description': 'Instalacion Camara',
        }

    def test_create_service_type(self):
        type = Service_Type.objects.create(**self.type_data)
        self.assertEqual(type.service_type_name, 'Instalacion')
        self.assertEqual(type.service_type_description, 'Instalacion Camara')
