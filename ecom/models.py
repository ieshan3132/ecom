from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Products(models.Model):
    pname = models.CharField(max_length=200)
    pimage = models.CharField(max_length=1000)
    type = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.pname

class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.item.pname