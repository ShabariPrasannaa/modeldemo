from django.db import models

# Create your models here.
class employee(models.Model):
    empno = models.IntegerField()
    empName = models.CharField(max_length=20)

def __str__(self):
    return 'Employee detail' 