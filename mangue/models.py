from operator import mod
from django.db import models

# Create your models here.
class Mangue(models.Model):
    name = models.CharField(max_length=100)