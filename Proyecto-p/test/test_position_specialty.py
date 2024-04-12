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
from registroUsuario.models import Position_Specialty, Position

class PositionSpecialtyTestCase(TestCase):
    def setUp(self):
        self.position_data = {
            'name_position': 'Manager'
        }
        self.position = Position.objects.create(**self.position_data)

        self.position_specialty_data = {
            'name_specialty_position': 'Specialty 1',
            'description_specialty_position': 'Specialty 1 Description',
            'position': self.position
        }

    def test_create_position_specialty(self):
        position_specialty = Position_Specialty.objects.create(**self.position_specialty_data)
        self.assertEqual(position_specialty.name_specialty_position, self.position_specialty_data['name_specialty_position'])
        self.assertEqual(position_specialty.description_specialty_position, self.position_specialty_data['description_specialty_position'])
        self.assertEqual(position_specialty.position, self.position)

    def test_edit_position_specialty(self):
        position_specialty = Position_Specialty.objects.create(**self.position_specialty_data)
        new_name = 'Specialty 2'
        new_description = 'Specialty 2 Description'
        position_specialty.name_specialty_position = new_name
        position_specialty.description_specialty_position = new_description
        position_specialty.save()
        self.assertEqual(position_specialty.name_specialty_position, new_name)
        self.assertEqual(position_specialty.description_specialty_position, new_description)

    def test_delete_position_specialty(self):
        position_specialty = Position_Specialty.objects.create(**self.position_specialty_data)
        position_specialty.delete()
        self.assertFalse(Position_Specialty.objects.filter(name_specialty_position=self.position_specialty_data['name_specialty_position']).exists())


