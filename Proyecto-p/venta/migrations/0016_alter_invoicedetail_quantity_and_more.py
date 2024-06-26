# Generated by Django 5.0.2 on 2024-03-07 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0015_remove_invoice_numberinvoice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicedetail',
            name='quantity',
            field=models.PositiveIntegerField(null=True, verbose_name='Unidades'),
        ),
        migrations.AlterField(
            model_name='invoicedetail',
            name='subTotal',
            field=models.PositiveIntegerField(null=True, verbose_name='Subtotal'),
        ),
    ]
