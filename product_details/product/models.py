from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Meta:
        managed = True
        db_table = 'users'

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_stock = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'product'