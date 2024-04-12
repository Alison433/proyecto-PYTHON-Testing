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
from registroUsuario.models import Client_Type  

class TestCreateClientType(TestCase):
    def test_create_client_type(self):
      
        client_type = Client_Type.objects.create(
            client_type_name="Frecuente",
            client_type_description="Clientes habituales que realizan compras con regularidad."
        )

       
        self.assertIsNotNone(client_type)
        self.assertEqual(client_type.client_type_name, "Frecuente")
        self.assertEqual(client_type.client_type_description, "Clientes habituales que realizan compras con regularidad.")

class TestEditClientType(TestCase):
    def test_edit_client_type(self):
       
        client_type = Client_Type.objects.create(
            client_type_name="Frecuente",
            client_type_description="Clientes habituales que realizan compras con regularidad."
        )

       
        client_type.client_type_name = "VIP"
        client_type.client_type_description = "Clientes muy importantes con beneficios exclusivos."
        client_type.save()

        
        updated_client_type = Client_Type.objects.get(pk=client_type.pk)

        
        self.assertEqual(updated_client_type.client_type_name, "VIP")
        self.assertEqual(updated_client_type.client_type_description, "Clientes muy importantes con beneficios exclusivos.")

class TestDeleteClientType(TestCase):
    def test_delete_client_type(self):
       
        client_type = Client_Type.objects.create(
            client_type_name="Frecuente",
            client_type_description="Clientes habituales que realizan compras con regularidad."
        )

       
        client_type.delete()

      
        with self.assertRaises(Client_Type.DoesNotExist):
            Client_Type.objects.get(pk=client_type.pk)


