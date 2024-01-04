from django.db import models

# Create your models here.
class userregistration(models.Model):
    login=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    sname=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=50)