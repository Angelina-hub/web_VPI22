# Generated by Django 4.1.4 on 2024-11-14 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EstablishmentsWeb', '0002_remove_establishment_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='establishment',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
