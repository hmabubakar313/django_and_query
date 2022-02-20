from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)

class Class(models.Model):
    roll_number = models.IntegerField()
    class_number = models.CharField(max_length=50)


  
