# Generated by Django 5.1.3 on 2024-11-27 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_remove_confirmacion_cedula_registro_civil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matrimonio',
            name='cedula_registro_civil',
        ),
    ]