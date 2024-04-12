from django.db import models
from venta.models import Product


class Flow_Type(models.Model):
    flow_type_name =  models.CharField(max_length=50, verbose_name="Nombre Tipo Flujo")
    flow_type_description = models.TextField(max_length=50, verbose_name="Descripción Tipo Flujo", null=True)
    
    def __str__(self):
        return self.flow_type_name
    
    class Meta:
        verbose_name = "Tipo_Flujo"
        verbose_name_plural = "Tipos Flujos"
        db_table = "tipoflujo"
        ordering = ['id']
      
class Inventory_Flow (models.Model):
    flow_type = models.ForeignKey(Flow_Type, on_delete=models.CASCADE, verbose_name="Tipo Flujo")
    product = models.ForeignKey(Product, on_delete= models.CASCADE, verbose_name="Producto")

    
    def __str__(self):
        return f"{self.flow_type} - {self.product}"
    
    class Meta:
        verbose_name = "Flujo Inventario"
        verbose_name_plural = "Flujos Inventarios"
        db_table = "flujoinventario"
        ordering = ['id']
  
 
    
    
        