# Generated by Django 5.1.3 on 2024-12-19 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_confirmacion_padrinos'),
    ]

    operations = [
        migrations.AddField(
            model_name='comunion',
            name='padrinos',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
