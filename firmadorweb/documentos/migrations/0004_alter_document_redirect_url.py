# Generated by Django 4.2.6 on 2024-07-04 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0003_document_redirect_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='redirect_url',
            field=models.URLField(default='https://example.com='),
        ),
    ]
