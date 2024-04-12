from django.test import TestCase
from inventario.models import Inventory_Flow, Flow_Type
from venta.models import Product, Brand

class InventoryFlowTestCase(TestCase):
    def setUp(self):
        brand = Brand.objects.create(name_brand="Marksovision")
        flow_type = Flow_Type.objects.create(flow_type_name="Salida", flow_type_description="Salida de producto")
        product = Product.objects.create(product_name="Producto test", product_description="descripcion test producto", product_reference="REF123", product_value=25000, product_quantity=365, brand=brand)
        
    def test_crear_inventory_flow(self):
      
        flow_type = Flow_Type.objects.get(flow_type_name="Salida")
        product = Product.objects.get(product_name="Producto test")
        
        
        new_inventory_flow = Inventory_Flow.objects.create(flow_type=flow_type, product=product)
        

        self.assertIsNotNone(new_inventory_flow)
