from django.db import models

# Create your models here.
class course(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
class pros(models.Model):
    name = models.CharField(max_length=30)
    mobile =models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=20)