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
from ordencompra.models import Status_News_Order


class StatusNewsOrderTestCase(TestCase):
    def setUp(self):
        self.status = Status_News_Order.objects.create(
            status_news_order_name='Enviado',
            status_news_order_description='Novedad enviada'
        )

    def test_estado_novedad_pedido(self):
        estado_novedad_pedido = Status_News_Order.objects.get(status_news_order_name='Enviado')
        self.assertEqual(estado_novedad_pedido.status_news_order_name, 'Enviado')

