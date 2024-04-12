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
from venta.models import Customer_Order_Status

class CustomerOrderStatusCreation(TestCase):
    def test_create_customer_order_status(self):
        order_status = Customer_Order_Status.objects.create(
            state_requested="Pending",
            description_state_requested="Waiting for processing"
        )

        self.assertIsNotNone(order_status.pk)
        self.assertEqual(order_status.state_requested, "Pending")
        self.assertEqual(order_status.description_state_requested, "Waiting for processing")

class CustomerOrderStatusEditing(TestCase):
    def test_edit_customer_order_status(self):
        order_status = Customer_Order_Status.objects.create(
            state_requested="Pending",
            description_state_requested="Waiting for processing"
        )

        order_status.state_requested = "Processing"
        order_status.description_state_requested = "Currently in progress"
        order_status.save()

        updated_order_status = Customer_Order_Status.objects.get(pk=order_status.pk)
        self.assertEqual(updated_order_status.state_requested, "Processing")
        self.assertEqual(updated_order_status.description_state_requested, "Currently in progress")


