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

from venta.models import Category

class CrearCategoriaTestCase(TestCase):
    def test_creacion_categoria(self):
        nueva_categoria = Category.objects.create(
            category_name='DVR',
            description_category='Categorizar DVR'
        )

        self.assertIsNotNone(nueva_categoria)
        self.assertEqual(nueva_categoria.category_name, 'DVR')
        self.assertEqual(nueva_categoria.description_category, 'Categorizar DVR')

class EliminarCategoriaTestCase(TestCase):
    def test_eliminacion_categoria(self):
        categoria_a_eliminar = Category.objects.create(
            category_name='Eliminar',
            description_category='Categoría a eliminar'
        )

        categoria_a_eliminar.delete()

        categorias = Category.objects.filter(category_name='Eliminar')
        self.assertEqual(categorias.count(), 0)

if __name__ == '__main__':
    unittest.main()
