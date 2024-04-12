import pytest

from app.models import Suppliers

def test_suppliers_creation ():
    supplers = Suppliers.object.create(
        supplier_name = 'Celunet',
        supplier_address = 'cra 5 #5-02',
        supplier_email = 'celunet@gmail.com',
        supplier_nit = '12345678-0',
        supplier_cellphone = '1234567890' 
    )
    assert Suppliers.supplier_name == 'Celunet'