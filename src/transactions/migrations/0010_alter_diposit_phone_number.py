# Generated by Django 4.2.7 on 2023-11-28 23:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0009_alter_diposit_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diposit',
            name='phone_number',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(100000000)]),
        ),
    ]
