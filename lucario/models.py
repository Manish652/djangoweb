from django.db import models

# Create your models here.
class person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=100)



