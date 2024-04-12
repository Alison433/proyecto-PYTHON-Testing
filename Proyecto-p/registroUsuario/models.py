from django.contrib.auth.models import AbstractUser
from django.db import models

class City(models.Model):
    city_name = models.CharField(max_length=100, verbose_name="Nombre Ciudad")
    
    def __str__(self):
        return f"{self.city_name}"
    
    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        db_table = "registrousuario_city"
        ordering = ['id']
    
class Role(models.Model):
    name_role = models.CharField(max_length=100, verbose_name="Nombre Rol")
    role_description = models.TextField(max_length=100, verbose_name="Rol Descripción")
    
    def __str__(self):
        return self.name_role
    
    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"
        db_table = "registrousuario_role"
        ordering = ['id']

class Contact(models.Model):
    address = models.CharField(max_length=255, verbose_name="Dirección")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="Ciudad")
    
    def __str__(self):
        return f"{self.address}, {self.city}"
    
    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        db_table = "registrousuario_contact"
        ordering = ['id']

class Client_Type(models.Model):
    client_type_name = models.CharField(max_length=100, verbose_name="Nombre Tipo Cliente")
    client_type_description = models.TextField(max_length=100, verbose_name="Descripción Tipo Cliente")
    
    def __str__(self):
        return self.client_type_name
    
    class Meta:
        verbose_name = "Tipo Cliente"
        verbose_name_plural = "Tipos Clientes"
        db_table = "registrousuario_client_type"
        ordering = ['id']



class Time_Work(models.Model):
    work_time_type = models.CharField(max_length=100, verbose_name="Tipo Tiempo Trabajo")
    work_time_description = models.TextField(max_length=100, verbose_name="Descripción Tiempo Trabajo")
    
    def __str__(self):
        return self.work_time_type
    
    class Meta:
        verbose_name = "Tiempo Trabajo"
        verbose_name_plural = "Tiempos Trabajos"
        db_table = "registrousuario_time_work"
        ordering = ['id']

class Availability_Status(models.Model):
    availability_type = models.CharField(max_length=100, verbose_name="Tipo Disponibilidad")
    description_type_availability = models.TextField(max_length=100, verbose_name="Descripción Tipo Disponibilidad")
    
    def __str__(self):
        return self.availability_type
    
    class Meta:
        verbose_name = "Estado Disponibilidad"
        verbose_name_plural = "Estado Disponibilidades"
        db_table = "registrousuario_availability_status"
        ordering = ['id']

class Identification_type(models.Model):
    identification_type = models.CharField(max_length=100, verbose_name="Tipo Identificación")
    description_type_identification = models.TextField(max_length=100, verbose_name="Descripción Tipo Identificación")
    
    def __str__(self):
        return self.identification_type
    
    class Meta:
        verbose_name = "Tipo Identificación"
        verbose_name_plural = "Tipos Identificaciones"
        db_table = "registrousuario_identification_type"
        ordering = ['id']

    
class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True, verbose_name="Usuario")
    second_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Segundo Nombre (Opcional)")
    second_last_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Apellido")
    password = models.CharField(max_length=128, verbose_name="Contraseña")  # Almacena la contraseña de manera segura
    password2 = models.CharField(max_length=128, verbose_name="Confirmar Contraseña")
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=10, blank=True, null=True, verbose_name="Teléfono")
    birth_date = models.DateField(null=True, verbose_name="Fecha Nacimiento")
    identification_type = models.ForeignKey(Identification_type, max_length=12, on_delete=models.CASCADE, verbose_name="Tipo Identifiacion", null=True)
    role = models.ForeignKey(Role, max_length=30, on_delete=models.CASCADE, verbose_name="Rol", null=True)
    contact = models.ForeignKey(Contact, max_length=12, on_delete=models.CASCADE, verbose_name="Contacto", null=True)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        related_query_name='customuser',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        related_query_name='customuser',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    def save(self, *args, **kwargs):
        if self.password:
            self.set_password(self.password)
            print(self)
        if self.password2:
            self.set_password(self.password2)
            print(self)  
        super().save(*args, **kwargs)
        
    def __str__(self):
      return self.username

class Client(models.Model):
    client_type = models.ForeignKey(Client_Type, on_delete=models.CASCADE, verbose_name="Tipo Cliente")
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name="Usuario")
    
    def __str__(self):
        return f"{self.user.username} - {self.client_type}"
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        db_table = "registrousuario_client"
        ordering = ['id']

class Position(models.Model):
    name_position = models.CharField(max_length=100, verbose_name="Nombre Cargo")
    
    def __str__(self):
        return f"{self.name_position} "
    
    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
        db_table = "registrousuario_position"
        ordering = ['id']
        
class Position_Specialty(models.Model):
    name_specialty_position = models.CharField(max_length=100, null=True, verbose_name="Nombre Especialidad Cargo")
    description_specialty_position = models.TextField(max_length=100, verbose_name="Descripción Especialidad Cargo")
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name="Cargo", null=True)
    
    def __str__(self):
        return self.name_specialty_position
    
    class Meta:
        verbose_name = "Especialidad Cargo"
        verbose_name_plural = "Especialidades Cargos"
        db_table = "registrousuario_position_specialty"
        ordering = ['id']
        
class Employee(models.Model):
    
    work_time = models.ForeignKey(Time_Work, on_delete=models.CASCADE, verbose_name="Tiempo Trabajo")
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name="Usuario")
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name="Cargo")
    availability_status = models.ForeignKey(Availability_Status, on_delete=models.CASCADE, verbose_name="Estado Disponibilidad")
    
    def __str__(self):
        return f"{self.user.username} - {self.position}"
    
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        db_table = "registrousuario_employee"
        ordering = ['id']


       


