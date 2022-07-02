from django.db import models

# Create your models here.
class Career(models.Model):
    name = models.CharField(max_length=30)
    # image = models.ImageField()
    special = models.TextField(max_length=250)
    skills = models.TextField(max_length=500)