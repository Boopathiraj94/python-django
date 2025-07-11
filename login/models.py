from django.db import models

# Create your models here.
class Loginss(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    user_name = models.CharField(max_length=250)
    address = models.CharField(max_length=250,null=True)
  

    def __str__(self):
        return self.user_name
