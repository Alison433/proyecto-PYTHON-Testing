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
from inventario.models import Flow_Type

class FlowTypeTestCase(TestCase):
    def test_create_flow_type(self):
        flow_type = Flow_Type.objects.create(
            flow_type_name='Flow Type 1',
            flow_type_description='Description of flow type 1'
        )
        

        self.assertIsNotNone(flow_type)
        self.assertEqual(flow_type.flow_type_name, 'Flow Type 1')
        self.assertEqual(flow_type.flow_type_description, 'Description of flow type 1')
        
    def test_edit_flow_type(self):

        flow_type = Flow_Type.objects.create(
            flow_type_name='Flow Type 2',
            flow_type_description='Description of flow type 2'
        )
        

        flow_type.flow_type_name = 'Modified Flow Type'
        flow_type.flow_type_description = 'Modified description of flow type'
        flow_type.save()
        

        updated_flow_type = Flow_Type.objects.get(pk=flow_type.pk)
        

        self.assertEqual(updated_flow_type.flow_type_name, 'Modified Flow Type')
        self.assertEqual(updated_flow_type.flow_type_description, 'Modified description of flow type')
