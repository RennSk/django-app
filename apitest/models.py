from enum import Flag
from pyexpat import model
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    descrizione = models.TextField(max_length=255)
    prezzo = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
