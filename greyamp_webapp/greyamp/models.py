from django.db import models

# Create your models here.
class GreyampData(models.Model):
    name = models.CharField(default='', max_length=10)
    test = models.CharField(default='', max_length=6)

