# Generated by Django 5.2.1 on 2025-05-13 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_myuser_city_myuser_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='display_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
