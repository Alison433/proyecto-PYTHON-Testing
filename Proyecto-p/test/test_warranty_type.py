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
from venta.models import Warranty_Type

class WarrantyTypeTestCase(TestCase):
    def test_crear_tipo_garantia(self):
       
        nuevo_tipo_garantia = Warranty_Type.objects.create(
            warranty_type_name='Garantía Extendida'
        )

    
        self.assertIsNotNone(nuevo_tipo_garantia)
        self.assertEqual(nuevo_tipo_garantia.warranty_type_name, 'Garantía Extendida')

if __name__ == '__main__':
    unittest.main()
