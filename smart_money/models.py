from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=20)
    focus=models.CharField(max_length=20)
    product_postion=models.CharField(max_length=20)
    def __str__(self):
        return self.name
