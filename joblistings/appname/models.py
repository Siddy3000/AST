from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)




def __str__(self):
    return self.title