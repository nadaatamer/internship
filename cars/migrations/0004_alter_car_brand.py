# Generated by Django 5.1 on 2024-08-26 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_car_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]
