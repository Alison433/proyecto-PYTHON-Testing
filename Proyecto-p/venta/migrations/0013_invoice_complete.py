# Generated by Django 5.0.2 on 2024-03-05 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0012_alter_invoice_numberinvoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='complete',
            field=models.BooleanField(default=False, verbose_name='Completa'),
        ),
    ]
