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
from datetime import date
from venta.models import Warranty, Warranty_Type

class WarrantyTestCase(TestCase):
    def setUp(self):
        tipo_garantia = Warranty_Type.objects.create(
            warranty_type_name='Garantía Extendida'
        )
        
        self.garantia = Warranty.objects.create(
            warranty_description='Garantía extendida por 2 años',
            warranty_time=date.today(), 
            warranty_type=tipo_garantia
        )

    def test_crear_garantia(self):
        self.assertIsNotNone(self.garantia)
        self.assertEqual(self.garantia.warranty_description, 'Garantía extendida por 2 años')
        self.assertEqual(self.garantia.warranty_time, date.today())

if __name__ == '__main__':
    unittest.main()
