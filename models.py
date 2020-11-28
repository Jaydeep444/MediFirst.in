from django.db import models
from django.core.validators import MinLengthValidator

class Register(models.Model):
    Uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    password = models.CharField('password', max_length=50, validators=[MinLengthValidator(8)])
