from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.IntegerField()
    efname=models.CharField(max_length=20)
    elname=models.CharField(max_length=20)
    edob=models.DateField()
    email=models.EmailField(max_length=40)
    eaddr=models.TextField()
    ephone=models.BigIntegerField()