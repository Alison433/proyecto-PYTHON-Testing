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

from venta.models import Brand, PREDEFINED_BRANDS


@pytest.mark.django_db
def test_existing_brand_exists():
    existing_brand_name = "Canon"  
    assert Brand.objects.filter(name_brand=existing_brand_name).exists() or existing_brand_name in PREDEFINED_BRANDS

@pytest.mark.django_db
def test_non_existing_brand_does_not_exist():
    non_existing_brand_name = "XYZBrand"  
    assert not Brand.objects.filter(name_brand=non_existing_brand_name).exists() and non_existing_brand_name not in PREDEFINED_BRANDS














