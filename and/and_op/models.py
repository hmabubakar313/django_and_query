from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)

class Class(models.Model):
    roll_number = models.IntegerField()
    class_number = models.CharField(max_length=50)

class BaseItem(models.Model):
    title = models.CharField(max_length=250)
    created = models.CharField(max_length=250)
    update = models.CharField(max_length=250)

    class Meta:
        abstract= True
        ordering = ['title']


class ItemA(BaseItem):
    content = models.TextField()

    ordering = ['-created']

class ItemB(BaseItem):
    file = models.FileField(upload_to='files')

class ItemC(BaseItem):
    file = models.FileField(upload_to='files')


class ItemD(BaseItem):
    slug=models.SlugField(max_length=255,unique=True)




  
