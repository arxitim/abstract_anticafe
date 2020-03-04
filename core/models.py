from django.db import models
from django.core import validators


class User(models.Model):
    user_id = models.IntegerField(primary_key=True, unique=True, db_index=True)
    password = models.CharField(max_length=128, validators=[validators.MinLengthValidator(1)])
    name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    tg_nick = models.CharField(max_length=128)

