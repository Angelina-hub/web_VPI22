# Generated by Django 4.1.4 on 2024-11-13 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EstablishmentsWeb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='establishment',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='establishment',
            name='updated_at',
        ),
    ]
