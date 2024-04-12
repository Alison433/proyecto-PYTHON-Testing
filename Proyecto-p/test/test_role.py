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
from registroUsuario.models import Role  

class RoleCreationTestCase(TestCase):
    def test_create_role(self):
        # Crear un nuevo rol
        role = Role.objects.create(
            name_role='Admin',
            role_description='Administrator role'
        )
        

        self.assertIsNotNone(role)
        self.assertEqual(role.name_role, 'Admin')
        self.assertEqual(role.role_description, 'Administrator role')

