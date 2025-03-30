from django.db import models

# Create your models here.
class ExampleModel(models.Model):
    text = models.CharField(max_length=200)
