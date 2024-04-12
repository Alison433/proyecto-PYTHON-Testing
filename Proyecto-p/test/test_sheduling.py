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

from servicioTecnico.models import Scheduling, Service, CustomUser, Client, Service_Status, Service_Type

class ServiceTypeModelTestCase(TestCase):
    def test_service_type_creation(self):
   
        service_type = Service_Type.objects.create(
            service_type_name="Tipo Servicio",
            service_type_description="Verifica creacion de Servicio"
        )

     
        self.assertEqual(service_type.service_type_name, "Tipo Servicio")
        self.assertEqual(service_type.service_type_description, "Verifica creacion de Servicio")

