from django.db import models
from venta.models import Product
from registroUsuario.models import Availability_Status, Position_Specialty, Employee
from registroUsuario.models import CustomUser


class Status_News_Order(models.Model):
    status_news_order_name = models.CharField(max_length=50, verbose_name="Nombre Estado Novedades Pedido")
    status_news_order_description = models.TextField(max_length=50, verbose_name="Descripción Tipo Novedad Pedido", null=True)
    
    def __str__(self):
        return self.status_news_order_name
    
    class Meta:
        verbose_name = "Estado Novedad Pedido"
        verbose_name_plural = "Estado Novedades Pedidos"
        db_table = "estnovedadespedidoprov"
        ordering = ['id']

        
class Supplier_Order_Status(models.Model):
    supplier_order_status_name = models.CharField(verbose_name="Nombre Estado Pedido Proveedor", max_length=255)
    supplier_order_status_description = models.TextField(max_length=50, verbose_name="Descripción Tipo Estado Pedido Proveedor", null=True)
    
    def __str__(self):
        return self.supplier_order_status_name
    
    class Meta:
        verbose_name = "Estado Pedido Proveedor"
        verbose_name_plural = "Estado Pedidos Proveedores"
        db_table = "estadopedidoprov"
        ordering = ['id']
        
class Suppliers(models.Model):
    supplier_name = models.CharField(max_length=50, verbose_name="Nombre Proveedor")
    supplier_address = models.CharField(max_length=255, verbose_name="Dirección Proveedor")
    supplier_email = models.CharField(max_length=255, verbose_name="Email Proveedor")
    supplier_nit = models.CharField(max_length=20, verbose_name="Nit Proveedor")
    supplier_cellphone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Celular Proveedor")

    def __str__(self):
        return self.supplier_name 
    
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        db_table = "proveedores"
        ordering = ['id']
    
class Supplier_Order(models.Model):
    date_order = models.DateTimeField(verbose_name="Fecha Pedido")
    product_quantity = models.IntegerField(verbose_name="Cantidad Producto")
    order_price = models.PositiveIntegerField(verbose_name="Precio Pedido")
    deliver_date = models.DateField(verbose_name="Fecha Entrega")
    address = models.CharField(verbose_name="Dirección", max_length=255)
    supplier_order_status = models.ForeignKey(Supplier_Order_Status, on_delete=models.CASCADE, verbose_name="Estado Orden Proveedor")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Empleado", null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None, verbose_name="Producto")
    suppliers = models.ForeignKey(Suppliers, on_delete=models.CASCADE, verbose_name="Proveedor", null=True) 
    

    def __str__(self):
        return f"{self.supplier_order_status} - {self.product} - {self.suppliers}"
    
    
    class Meta:
        verbose_name = "Pedido Proveedor"
        verbose_name_plural = "Pedido Proveedores"
        db_table = "pedido_proveedores"
        ordering = ['id']
        
class Supplier_Order_News(models.Model):
    date_new_order_supplier = models.DateTimeField(verbose_name="Fecha Novedades Pedido Proveedor")
    status_news_order = models.ForeignKey(Status_News_Order, on_delete = models.CASCADE, verbose_name="Estado Novedades Pedido")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Empleado", null=True)
    supplier_order = models.ForeignKey(Supplier_Order, on_delete=models.CASCADE, verbose_name="Orden Pedido Proveedor")
    
    def __str__(self):
        return f"{self.status_news_order} - {self.employee} - {self.supplier_order}"
    
    class Meta:
        verbose_name = "Novedades Pedido Proveedor"
        verbose_name_plural = "Novedades Pedido Proveedores"
        db_table = "novedadespedidoproveedor"
        ordering = ['id']