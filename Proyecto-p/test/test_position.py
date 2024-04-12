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
from registroUsuario.models import Position

class PositionTestCase(TestCase):
    def setUp(self):
        self.positions = [
            'Tecnico',
            'Mensajero',
            'Administrador',
            'Vendedor',
            'Gerente'
        ]

    def test_create_positions(self):
        for position_name in self.positions:
            position = Position.objects.create(name_position=position_name)
            self.assertEqual(position.name_position, position_name)

    def test_edit_position(self):
        position = Position.objects.create(name_position='Tecnico')
        new_name = 'Supervisor'
        position.name_position = new_name
        position.save()
        self.assertEqual(position.name_position, new_name)

    def test_delete_position(self):
        position = Position.objects.create(name_position='Tecnico')
        position.delete()
        self.assertFalse(Position.objects.filter(name_position='Tecnico').exists())


