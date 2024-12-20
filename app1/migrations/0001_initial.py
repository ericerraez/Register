# Generated by Django 5.1.3 on 2024-11-12 02:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('fecha_nacimiento', models.DateField()),
                ('lugar_nacimiento', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroBautizo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_bautizo', models.DateField()),
                ('celebrante', models.CharField(max_length=255)),
                ('registro_eclesiastico_ano', models.IntegerField()),
                ('registro_eclesiastico_tomo', models.IntegerField()),
                ('registro_eclesiastico_pagina', models.IntegerField()),
                ('registro_eclesiastico_acta', models.CharField(max_length=255)),
                ('parroco', models.CharField(max_length=255)),
                ('nota', models.TextField(blank=True, null=True)),
                ('fecha_expedicion', models.DateTimeField(auto_now_add=True)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.persona')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroComunion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_sacramento', models.DateField()),
                ('celebrante', models.CharField(max_length=255)),
                ('registro_eclesiastico_ano', models.IntegerField()),
                ('registro_eclesiastico_tomo', models.IntegerField()),
                ('registro_eclesiastico_pagina', models.IntegerField()),
                ('registro_eclesiastico_acta', models.CharField(max_length=255)),
                ('parroco', models.CharField(max_length=255)),
                ('nota', models.TextField(blank=True, null=True)),
                ('fecha_emision_certificado', models.DateField()),
                ('fecha_expedicion', models.DateTimeField(auto_now_add=True)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.persona')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroConfirmacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_confirmacion', models.DateField()),
                ('celebrante', models.CharField(max_length=255)),
                ('registro_eclesiastico_ano', models.IntegerField()),
                ('registro_eclesiastico_tomo', models.IntegerField()),
                ('registro_eclesiastico_pagina', models.IntegerField()),
                ('registro_eclesiastico_acta', models.CharField(max_length=255)),
                ('parroco', models.CharField(max_length=255)),
                ('nota', models.TextField(blank=True, null=True)),
                ('fecha_expedicion', models.DateTimeField(auto_now_add=True)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.persona')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroMatrimonio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_matrimonio', models.DateField()),
                ('celebrante', models.CharField(max_length=255)),
                ('registro_eclesiastico_ano', models.IntegerField()),
                ('registro_eclesiastico_tomo', models.IntegerField()),
                ('registro_eclesiastico_pagina', models.IntegerField()),
                ('registro_eclesiastico_acta', models.CharField(max_length=255)),
                ('parroco', models.CharField(max_length=255)),
                ('nota', models.TextField(blank=True, null=True)),
                ('fecha_expedicion', models.DateTimeField(auto_now_add=True)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.persona')),
            ],
        ),
    ]
