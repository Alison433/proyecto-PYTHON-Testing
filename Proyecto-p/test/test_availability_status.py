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


from registroUsuario.models import Availability_Status


class AvailabilityStatusTest(unittest.TestCase):
    def setUp(self):
        self.availability_status = Availability_Status.objects.create(
            availability_type='Tipo de Disponibilidad',
            description_type_availability='Descripción del Tipo de Disponibilidad'
        )

    def test_availability_status_creation(self):
        self.assertEqual(self.availability_status.availability_type, 'Tipo de Disponibilidad')
        self.assertEqual(self.availability_status.description_type_availability, 'Descripción del Tipo de Disponibilidad')

    def tearDown(self):
        # No necesitas cerrar la conexión de la base de datos en este caso
        pass

if __name__ == '__main__':
    unittest.main()



