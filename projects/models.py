from django.db import models

# Create your models here.
class Project(models.Model):
    nombre = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    image = models.CharField(max_length=200)