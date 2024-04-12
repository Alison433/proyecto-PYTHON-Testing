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
from registroUsuario.models import Identification_type  

class TestCreateIdentificationType(TestCase):
    def test_create_identification_type(self):
      
        identification_type = Identification_type.objects.create(
            identification_type="Cédula de ciudadanía",
            description_type_identification="Documento de identificación nacional en Colombia."
        )


        self.assertIsNotNone(identification_type)
        self.assertEqual(identification_type.identification_type, "Cédula de ciudadanía")
        self.assertEqual(identification_type.description_type_identification, "Documento de identificación nacional en Colombia.")


