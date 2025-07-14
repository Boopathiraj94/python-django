from django.db import models

# Create your models here.

class Students(models.Model):
    student_name = models.CharField(max_length=250)
    student_phone = models.CharField(max_length=20,null=True)
    student_class= models.CharField(max_length=20,null=True)
    student_section= models.CharField(max_length=20,null=True)
    student_email = models.EmailField(max_length=200,null=True)
    student_address= models.TextField(null=True)

