from email.policy import default
from django.db import models

class Product(models.Model):
    name = models.TextField()
    brand = models.TextField(default=None, null=True)
    kcal_density = models.IntegerField(null=True)
    kcal_density_unit = models.CharField(max_length=20, default="g")


class Meal(models.Model):
    name = models.TextField()
    brand = models.TextField(default=None, null=True)
    kcal_density = models.IntegerField(null=True)
    kcal_density_unit = models.CharField(max_length=20, default="g")
    