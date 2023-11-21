from django.db import models

import uuid
# Create your models here.

class Service(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    details = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    img = models.URLField()
    serviceTime = models.DateTimeField()
    serviceDate = models.DateField()
    status = models.CharField(max_length=50)
    categoryId = models.UUIDField()
    publisherId = models.UUIDField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    

class User(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    img=models.TextField()