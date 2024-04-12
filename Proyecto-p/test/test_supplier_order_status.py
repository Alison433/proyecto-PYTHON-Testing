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
from ordencompra.models import Supplier_Order_Status


class SupplierOrderStatusTestCase(TestCase):
    def test_new_supplier_order_status_creation(self):
        # Creamos un nuevo estado de pedido de proveedor
        Supplier_Order_Status.objects.create(
            supplier_order_status_name="Despachado",
            supplier_order_status_description="Descripción de estado"
        )
        
        
        self.assertEqual(Supplier_Order_Status.objects.count(), 1)
        
        new_status = Supplier_Order_Status.objects.get(supplier_order_status_name="Despachado")
        self.assertEqual(new_status.supplier_order_status_name, "Despachado")
        self.assertEqual(new_status.supplier_order_status_description, "Descripción de estado")
