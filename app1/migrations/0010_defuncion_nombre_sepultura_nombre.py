# Generated by Django 5.1.3 on 2024-11-26 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_alter_bautizo_acta_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='defuncion',
            name='nombre',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sepultura',
            name='nombre',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
