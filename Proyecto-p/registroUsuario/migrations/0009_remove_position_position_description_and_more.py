# Generated by Django 4.2.7 on 2023-12-11 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registroUsuario', '0008_identification_type_alter_customuser_contact_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='position_description',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='Fecha Nacimiento'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='Contraseña'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password2',
            field=models.CharField(max_length=128, verbose_name='Confirmar Contraseña'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='second_last_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='second_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Segundo Nombre (Opcional)'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=150, unique=True, verbose_name='Usuario'),
        ),
    ]
