# Generated by Django 3.0.3 on 2020-03-04 18:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200304_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
    ]
