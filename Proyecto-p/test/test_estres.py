from django.test import TestCase
from registroUsuario.models import CustomUser, City, Role, Contact, Client_Type, Time_Work, Availability_Status, Identification_type, Position, Position_Specialty, Employee,Client

class StressTestCase(TestCase):
    def setUp(self):
        # Limpiar la base de datos antes de cada prueba
        CustomUser.objects.all().delete()
        City.objects.all().delete()
        Role.objects.all().delete()
        Contact.objects.all().delete()
        Client_Type.objects.all().delete()
        Time_Work.objects.all().delete()
        Availability_Status.objects.all().delete()
        Identification_type.objects.all().delete()
        Position.objects.all().delete()
        Position_Specialty.objects.all().delete()
        Employee.objects.all().delete()
    def test_create_users(self):
        # Crear datos necesarios para la creación de usuarios
        city = City.objects.create(city_name="Ciudad Ejemplo")
        role = Role.objects.create(name_role="Rol Ejemplo", role_description="Descripción del Rol")
        contact = Contact.objects.create(address="Dirección Ejemplo", city=city)
        client_type = Client_Type.objects.create(client_type_name="Tipo de Cliente Ejemplo", client_type_description="Descripción del Tipo de Cliente")
        time_work = Time_Work.objects.create(work_time_type="Tipo de Tiempo de Trabajo Ejemplo", work_time_description="Descripción del Tipo de Tiempo de Trabajo")
        availability_status = Availability_Status.objects.create(availability_type="Tipo de Disponibilidad Ejemplo", description_type_availability="Descripción del Tipo de Disponibilidad")
        identification_type = Identification_type.objects.create(identification_type="Tipo de Identificación Ejemplo", description_type_identification="Descripción del Tipo de Identificación")
        position = Position.objects.create(name_position="Cargo Ejemplo")
        position_specialty = Position_Specialty.objects.create(name_specialty_position="Especialidad del Cargo Ejemplo", description_specialty_position="Descripción de la Especialidad del Cargo")
 # Crear 100 usuarios de prueba
        for i in range(100):
            user = CustomUser.objects.create(
                username=f"usuario{i}",
                second_name="Segundo Nombre",
                second_last_name="Apellido",
                password="password",  # Se almacenará de manera segura automáticamente
                password2="password",  # Se almacenará de manera segura automáticamente
                email=f"usuario{i}@example.com",
                phone="1234567890",
                birth_date="1990-01-01",
                identification_type=identification_type,
                role=role,
                contact=contact
            )
            Client.objects.create(client_type=client_type, user=user)
            Employee.objects.create(work_time=time_work, user=user, position=position, availability_status=availability_status)
        # Verificar que se crearon 100 usuarios
        self.assertEqual(CustomUser.objects.count(), 100)