from django.db import models

# Create your models here.
class RegModel(models.Model):
    Fname=models.CharField(max_length=10)
    Lname=models.CharField(max_length=10)
    Uname=models.CharField(max_length=10)
    Password=models.CharField(max_length=10)
    Cpassword=models.CharField(max_length=10)
    Email=models.EmailField()
    Mobno=models.CharField(max_length=10)

