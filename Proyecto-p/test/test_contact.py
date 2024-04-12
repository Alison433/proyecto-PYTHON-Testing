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
from registroUsuario.models import Contact, City 
class TestCreateContact(TestCase):
    def setUp(self):
        self.city = City.objects.create(city_name='Bogotá')

    def test_create_contact(self):
       
        contact = Contact.objects.create(
            address='Calle 123',
            city=self.city
        )

      
        self.assertIsNotNone(contact)
        self.assertEqual(contact.address, 'Calle 123')
        self.assertEqual(contact.city, self.city)

class TestEditContact(TestCase):
    def setUp(self):
        self.city = City.objects.create(city_name='Bogotá')

    def test_edit_contact(self):
       
        contact = Contact.objects.create(
            address='Calle 123',
            city=self.city
        )

     
        new_address = 'Calle 123'
        contact.address = new_address
        contact.save()

    
        updated_contact = Contact.objects.get(pk=contact.pk)

       
        self.assertEqual(updated_contact.address, new_address)

class TestDeleteContact(TestCase):
    def setUp(self):
        self.city = City.objects.create(city_name='Bogotá')

    def test_delete_contact(self):
        
        contact = Contact.objects.create(
            address='Calle 123',
            city=self.city
        )

    
        contact.delete()

      
        with self.assertRaises(Contact.DoesNotExist):
            Contact.objects.get(pk=contact.pk)


