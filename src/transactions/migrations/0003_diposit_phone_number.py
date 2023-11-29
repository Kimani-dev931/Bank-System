# Generated by Django 4.2.7 on 2023-11-28 19:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20190504_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='diposit',
            name='phone_number',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(100000000000000), django.core.validators.MaxValueValidator(999999999999999)]),
        ),
    ]
