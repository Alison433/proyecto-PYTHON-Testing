# Generated by Django 4.2.7 on 2023-12-10 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicioTecnico', '0004_remove_scheduling_empleado_and_more'),
        ('registroUsuario', '0004_availability_status_city_client_client_type_contact_and_more'),
        ('venta', '0002_alter_warranty_options_alter_warranty_type_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Order_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_requested', models.CharField(max_length=50, verbose_name='Estado Pedido')),
                ('description_state_requested', models.CharField(max_length=50, verbose_name='Descripción Estado Pedido')),
            ],
            options={
                'verbose_name': 'Estado Pedido',
                'verbose_name_plural': 'Estados Pedidos',
                'db_table': 'estadopedido',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='sale',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registroUsuario.employee', verbose_name='Empleado'),
        ),
        migrations.CreateModel(
            name='Customer_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_order', models.DateTimeField(verbose_name='Fecha Venta')),
                ('order_quantity', models.IntegerField(verbose_name='Cantidad')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registroUsuario.client', verbose_name='Cliente')),
                ('customer_order_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.customer_order_status', verbose_name='Estado Pedido Cliente')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.product', verbose_name='Producto')),
                ('scheduling', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicioTecnico.scheduling', verbose_name='Agendamiento')),
            ],
            options={
                'verbose_name': 'Pedido Cliente',
                'verbose_name_plural': 'Pedidos Cliente',
                'db_table': 'pedidocliente',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='sale',
            name='custom_order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='venta.customer_order', verbose_name='Pedido Cliente'),
        ),
    ]