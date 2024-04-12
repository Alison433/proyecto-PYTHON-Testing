from django.db import models
from django.contrib.auth import get_user_model
from registroUsuario.models import CustomUser
from registroUsuario.models import Availability_Status, Employee, Client

User = get_user_model()


    
class Service_Status(models.Model):
    service_status_name = models.CharField(max_length=50, verbose_name="Nombre Estado Servicio", null=True)
    service_status_description = models.TextField(max_length=50, verbose_name="Descripción Estado Servicio", null=True)

    def __str__(self):
        return self.service_status_name
    
    class Meta:
        verbose_name = "Estado Servicio"
        verbose_name_plural = "Estado Servicios"
        db_table = "estadoservicio"
        ordering = ['id']


class Service_Type(models.Model):
    service_type_name = models.CharField(max_length=50, verbose_name="Nombre Tipo Servicio")
    service_type_description = models.TextField(max_length=50, verbose_name="Descripción Tipo Servicio", null=True)

    def __str__(self):
        return self.service_type_name
    
    class Meta:
        verbose_name = "Tipo Servicio"
        verbose_name_plural = "Tipo Servicios"
        db_table = "tiposervicio"
        ordering = ['id']
        

class Service(models.Model):
    service_description = models.TextField(max_length=50, verbose_name="Descripción Servicio")
    service_price = models.PositiveIntegerField(verbose_name="Precio Servicio")
    service_type = models.ForeignKey(Service_Type, on_delete=models.CASCADE, verbose_name="Tipo Servicio")
    service_status = models.ForeignKey(Service_Status, on_delete=models.CASCADE, verbose_name="Estado Servicio")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Cliente", related_name="servicios_cliente", null=True)
    
    def __str__(self):
        return f"{self.service_description} - {self.client}"
    
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        db_table = "servicio"
        ordering = ['id']
        
        
class Scheduling(models.Model):
    scheduling_description = models.TextField(max_length=50, verbose_name="Descripción Agendamiento")
    scheduling_time = models.TimeField(verbose_name="Hora Agendamiento")
    scheduling_date = models.DateField(verbose_name="Fecha Agendamiento")
    availability_status = models.ForeignKey(Availability_Status, on_delete=models.CASCADE, null=True, verbose_name="Estado Disponibilidad")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Empleado", null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Servicio")
    
    def __str__(self):
        return f"{self.scheduling_description} - {self.scheduling_date} - {self.scheduling_time}"
    
    class Meta:
        verbose_name = "Agendamiento"
        verbose_name_plural = "Agendamientos"
        db_table = "agendamiento"
        ordering = ['id']


