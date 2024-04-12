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
from servicioTecnico.models import Service, Service_Status, Service_Type
from registroUsuario.models import Identification_type, Contact, Role, Client_Type, City, CustomUser, Client
class ServiceTestCase(TestCase):
    def setUp(self):
        status = Service_Status.objects.create(service_status_name="Activo", service_status_description="Estado activo del servicio")
        type = Service_Type.objects.create(service_type_name="Tecnico", service_type_description="Revision Camara")
        identification_type = Identification_type.objects.create(identification_type="Cédula", description_type_identification="Documento de identidad")
        contact = Contact.objects.create(address="Calle 123", city=City.objects.create(city_name="Ciudad Test"))
        role = Role.objects.create(name_role="Admin", role_description="Administrador del sistema")
        user = CustomUser.objects.create(username="testuser", email="test@example.com", identification_type=identification_type, role=role, contact=contact)
        client = Client.objects.create(client_type=Client_Type.objects.create(client_type_name="Empresa", client_type_description="Cliente tipo empresa"), user=user)
        
    def test_crear_service(self):
        service = Service.objects.create(
            service_description="Revision Camara",
            service_price=100,
            service_type=Service_Type.objects.get(service_type_name="Tecnico"),
            service_status=Service_Status.objects.get(service_status_name="Activo"),
            client=Client.objects.get(user__username="testuser")
        )
        self.assertIsNotNone(service)
        
    def test_editar_service(self):
        status = Service_Status.objects.get(service_status_name="Activo")
        type = Service_Type.objects.get(service_type_name="Tecnico")
        user = CustomUser.objects.get(username="testuser")
        client = Client.objects.get(user=user)
        service = Service.objects.create(
            service_description="Revision Camara",
            service_price=100,
            service_type=type,
            service_status=status,
            client=client
        )
        service.service_price = 150
        service.save()
        edited_service = Service.objects.get(service_description="Revision Camara")
        self.assertEqual(edited_service.service_price, 150)
        
    def test_eliminar_service(self):
        status = Service_Status.objects.get(service_status_name="Activo")
        type = Service_Type.objects.get(service_type_name="Tecnico")
        user = CustomUser.objects.get(username="testuser")
        client = Client.objects.get(user=user)
        service = Service.objects.create(
            service_description="Revision Camara",
            service_price=100,
            service_type=type,
            service_status=status,
            client=client
        )
        service.delete()
        self.assertEqual(Service.objects.filter(service_description="Revision Camara").count(), 0)


