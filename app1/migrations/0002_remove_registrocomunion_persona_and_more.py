# Generated by Django 5.1.3 on 2024-11-12 17:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrocomunion',
            name='persona',
        ),
        migrations.RemoveField(
            model_name='registroconfirmacion',
            name='persona',
        ),
        migrations.RemoveField(
            model_name='registromatrimonio',
            name='persona',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='lugar_nacimiento',
        ),
        migrations.AddField(
            model_name='persona',
            name='apellido',
            field=models.CharField(default='Desconocido', max_length=100),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Bautizo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('iglesia', models.CharField(max_length=100)),
                ('padrinos', models.CharField(max_length=200)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Comunion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('iglesia', models.CharField(max_length=100)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Confirmacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('iglesia', models.CharField(max_length=100)),
                ('padrinos', models.CharField(max_length=200)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Matrimonio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('iglesia', models.CharField(max_length=100)),
                ('testigos', models.CharField(max_length=200)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.persona')),
            ],
        ),
        migrations.DeleteModel(
            name='RegistroBautizo',
        ),
        migrations.DeleteModel(
            name='RegistroComunion',
        ),
        migrations.DeleteModel(
            name='RegistroConfirmacion',
        ),
        migrations.DeleteModel(
            name='RegistroMatrimonio',
        ),
    ]
