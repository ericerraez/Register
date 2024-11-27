# Generated by Django 5.1.3 on 2024-11-26 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_rename_acta_bautizo_acta_registro_civil_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='confirmacion',
            old_name='acta',
            new_name='acta_registro_civil',
        ),
        migrations.RenameField(
            model_name='matrimonio',
            old_name='acta',
            new_name='acta_registro_civil',
        ),
        migrations.RemoveField(
            model_name='confirmacion',
            name='datos_registro_civil_acta',
        ),
        migrations.RemoveField(
            model_name='confirmacion',
            name='datos_registro_civil_ano',
        ),
        migrations.RemoveField(
            model_name='confirmacion',
            name='datos_registro_civil_pagina',
        ),
        migrations.RemoveField(
            model_name='confirmacion',
            name='datos_registro_civil_tomo',
        ),
        migrations.RemoveField(
            model_name='confirmacion',
            name='fecha_emision_certificado_confirmacion',
        ),
        migrations.RemoveField(
            model_name='confirmacion',
            name='pagina',
        ),
        migrations.RemoveField(
            model_name='confirmacion',
            name='parroco',
        ),
        migrations.RemoveField(
            model_name='confirmacion',
            name='tomo',
        ),
        migrations.RemoveField(
            model_name='matrimonio',
            name='datos_registro_civil_acta',
        ),
        migrations.RemoveField(
            model_name='matrimonio',
            name='datos_registro_civil_ano',
        ),
        migrations.RemoveField(
            model_name='matrimonio',
            name='datos_registro_civil_pagina',
        ),
        migrations.RemoveField(
            model_name='matrimonio',
            name='datos_registro_civil_tomo',
        ),
        migrations.RemoveField(
            model_name='matrimonio',
            name='fecha_emision_certificado_matrimonio',
        ),
        migrations.RemoveField(
            model_name='matrimonio',
            name='pagina',
        ),
        migrations.RemoveField(
            model_name='matrimonio',
            name='parroco',
        ),
        migrations.RemoveField(
            model_name='matrimonio',
            name='tomo',
        ),
        migrations.AddField(
            model_name='confirmacion',
            name='acta_registro_eclesiastico',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='confirmacion',
            name='ano_registro_civil',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='confirmacion',
            name='cedula_registro_civil',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='confirmacion',
            name='pagina_registro_civil',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='confirmacion',
            name='pagina_registro_eclesiastico',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='confirmacion',
            name='tomo_registro_civil',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='confirmacion',
            name='tomo_registro_eclesiastico',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='matrimonio',
            name='acta_registro_eclesiastico',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='matrimonio',
            name='ano_registro_civil',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='matrimonio',
            name='cedula_registro_civil',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='matrimonio',
            name='pagina_registro_civil',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='matrimonio',
            name='pagina_registro_eclesiastico',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='matrimonio',
            name='tomo_registro_civil',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='matrimonio',
            name='tomo_registro_eclesiastico',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
