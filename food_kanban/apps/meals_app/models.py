from django.db import models


class Product(models.Model):
    """Model representing food products or distinct components of a meal."""

    name = models.TextField()
    brand = models.TextField(default=None, null=True)
    kcal_density = models.IntegerField(null=True)
    kcal_density_unit = models.CharField(max_length=20, default="g")


class Meal(models.Model):
    """Model representing complete meals or dishes comprising of a group of products."""

    name = models.TextField()
    brand = models.TextField(default=None, null=True)
    kcal_density = models.IntegerField(null=True)
    kcal_density_unit = models.CharField(max_length=20, default="g")
    products = models.ManyToManyField(Product)
