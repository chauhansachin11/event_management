from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.IntegerField()
    salary = models.FloatField()
    city = models.CharField(max_length=100)
