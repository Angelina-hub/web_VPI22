# Generated by Django 4.1.4 on 2024-11-14 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EstablishmentsWeb', '0003_alter_establishment_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('feedback', models.CharField(max_length=500)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
