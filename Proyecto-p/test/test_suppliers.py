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
from ordencompra.models import Suppliers

class SuppliersDeleteTestCase(TestCase):
    def setUp(self):
    
        self.supplier = Suppliers.objects.create(
            supplier_name="Electrycams",
            supplier_address="Calle 18 # 10-63",
            supplier_email="electrycams@gmail.com",
            supplier_nit="987654321",
            supplier_cellphone="3102187865"
        )
    
    def test_supplier_deletion(self):
       
        self.assertEqual(Suppliers.objects.count(), 1)
        self.supplier.delete()
        self.assertEqual(Suppliers.objects.count(), 0)
