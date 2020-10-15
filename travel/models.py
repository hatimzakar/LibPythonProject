from django.db import models

# Create your models here.
from django.db.models import CharField, options


class Destination(models.Model):
    desc =  models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    city = models.CharField(max_length=100)
