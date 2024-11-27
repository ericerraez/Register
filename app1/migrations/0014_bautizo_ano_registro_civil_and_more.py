# Generated by Django 5.1.3 on 2024-11-26 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_rename_fecha_emision_certificado_bautizo_comunion_fecha_emision'),
    ]

    operations = [
        migrations.AddField(
            model_name='bautizo',
            name='ano_registro_civil',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='comunion',
            name='ano_registro_civil',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
