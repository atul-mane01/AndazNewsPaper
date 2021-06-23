from django.db import models

# Create your models here.
class info(models.Model):
    dist = models.CharField(max_length=25)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=30)
    
