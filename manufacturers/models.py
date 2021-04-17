from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    url = models.SlugField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name