from datetime import datetime, date
from django.utils import timezone
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
from ordencompra.models import Supplier_Order, Supplier_Order_Status, Suppliers
from registroUsuario.models import Employee, Time_Work, CustomUser, Availability_Status, Position
from venta.models import Product

class SupplierOrderTestCase(TestCase):
    date_time_with_timezone = timezone.now()
    def test_supplier_order_creation(self):
       
        supplier_order_status = Supplier_Order_Status.objects.create(supplier_order_status_name="Estado de Prueba")
        time_work = Time_Work.objects.create()  
        custom_user = CustomUser.objects.create()  
        position = Position.objects.create()  
        availability_status = Availability_Status.objects.create()  


        employee = Employee.objects.create(
            work_time=time_work,
            user=custom_user,
            position=position,
            availability_status=availability_status
        )

        
        product = Product.objects.create(product_name="Nombre del Producto", product_description="Descripción del Producto", product_reference="Referencia del Producto", product_value=10, product_quantity=100, category=None, brand=None, image=None)

       
        order = Supplier_Order.objects.create(
            date_order=datetime.now(),
            product_quantity=10,
            order_price=100,
            deliver_date=date.today(),
            address="Dirección de Prueba",
            supplier_order_status=supplier_order_status,
            employee=employee,
            product=product,
            suppliers=None 
        )

 
        self.assertIsNotNone(order)
        self.assertEqual(order.product_quantity, 10)
        self.assertEqual(order.order_price, 100)
        self.assertEqual(order.address, "Dirección de Prueba")
        self.assertEqual(order.supplier_order_status, supplier_order_status)
        self.assertEqual(order.employee, employee)
        self.assertEqual(order.product, product) 
