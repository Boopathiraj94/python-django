from django.db import models

# Create your models here.
class Lists(models.Model):
    messages = models.TextField(max_length=500,null=True)
    added_at = models.DateTimeField(auto_now_add=True)