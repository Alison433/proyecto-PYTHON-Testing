# Generated by Django 5.0.2 on 2024-03-15 19:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0017_alter_invoicedetail_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name_brand',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nombre Marca'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='venta.brand', verbose_name='Marca'),
        ),
    ]
