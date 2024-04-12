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
from servicioTecnico.models import Service_Status

class ServiceStatusTestCase(TestCase):
    def setUp(self):
        self.status_data = {
            'service_status_name': 'Activo',
            'service_status_description': 'Este servicio está activo',
        }

    def test_create_service_status(self):
        status = Service_Status.objects.create(**self.status_data)
        self.assertEqual(status.service_status_name, 'Activo')
        self.assertEqual(status.service_status_description, 'Este servicio está activo')

    def test_edit_service_status(self):
        status = Service_Status.objects.create(**self.status_data)
        new_status_data = {
            'service_status_name': 'Inactivo',
            'service_status_description': 'Este servicio está inactivo',
        }
        status.service_status_name = new_status_data['service_status_name']
        status.service_status_description = new_status_data['service_status_description']
        status.save()

        updated_status = Service_Status.objects.get(pk=status.pk)
        self.assertEqual(updated_status.service_status_name, 'Inactivo')
        self.assertEqual(updated_status.service_status_description, 'Este servicio está inactivo')
