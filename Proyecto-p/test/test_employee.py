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
from registroUsuario.models import Employee, CustomUser, Position, Time_Work, Availability_Status

class EmployeeTestCase(TestCase):
    def setUp(self):
        self.work_time = Time_Work.objects.create(work_time_type='Full-time', work_time_description='Full-time work description')
        self.user = CustomUser.objects.create(username='testuser', email='test@example.com', password='testpassword')
        self.position = Position.objects.create(name_position='Manager')
        self.availability_status = Availability_Status.objects.create(availability_type='Available', description_type_availability='Available status description')  

        self.employee_data = {
            'work_time': self.work_time,
            'user': self.user,
            'position': self.position,
            'availability_status': self.availability_status
        }

    def test_create_employee(self):
        employee = Employee.objects.create(**self.employee_data)
        self.assertEqual(employee.work_time, self.work_time)
        self.assertEqual(employee.user, self.user)
        self.assertEqual(employee.position, self.position)
        self.assertEqual(employee.availability_status, self.availability_status)

    def test_edit_employee(self):
        employee = Employee.objects.create(**self.employee_data)
        new_position = Position.objects.create(name_position='Supervisor')
        employee.position = new_position
        employee.save()
        self.assertEqual(employee.position, new_position)

    def test_delete_employee(self):
        employee = Employee.objects.create(**self.employee_data)
        employee.delete()
        self.assertFalse(Employee.objects.filter(user=self.user).exists())






