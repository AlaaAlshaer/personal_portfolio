from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=50)
    descrption = models.TextField()
    tecnologe = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")