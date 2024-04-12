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
from registroUsuario.models import Time_Work  

class TestCreateTimeWork(TestCase):
    def test_create_time_work(self):
        
        time_work = Time_Work.objects.create(
            work_time_type="Tiempo Completo",
            work_time_description="Trabajo a tiempo completo, 40 horas a la semana."
        )

    
        self.assertIsNotNone(time_work)
        self.assertEqual(time_work.work_time_type, "Tiempo Completo")
        self.assertEqual(time_work.work_time_description, "Trabajo a tiempo completo, 40 horas a la semana.")

class TestEditTimeWork(TestCase):
    def test_edit_time_work(self):
        
        time_work = Time_Work.objects.create(
            work_time_type="Tiempo Completo",
            work_time_description="Trabajo a tiempo completo, 40 horas a la semana."
        )

        
        time_work.work_time_type = "Medio Tiempo"
        time_work.work_time_description = "Trabajo a medio tiempo, 20 horas a la semana."
        time_work.save()

        
        updated_time_work = Time_Work.objects.get(pk=time_work.pk)

        
        self.assertEqual(updated_time_work.work_time_type, "Medio Tiempo")
        self.assertEqual(updated_time_work.work_time_description, "Trabajo a medio tiempo, 20 horas a la semana.")

class TestDeleteTimeWork(TestCase):
    def test_delete_time_work(self):
        
        time_work = Time_Work.objects.create(
            work_time_type="Tiempo Completo",
            work_time_description="Trabajo a tiempo completo, 40 horas a la semana."
        )

       
        time_work.delete()

      
        with self.assertRaises(Time_Work.DoesNotExist):
            Time_Work.objects.get(pk=time_work.pk)



