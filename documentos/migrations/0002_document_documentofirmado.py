# Generated by Django 4.2.6 on 2024-07-04 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='documentoFirmado',
            field=models.BooleanField(default=False),
        ),
    ]
