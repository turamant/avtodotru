from django.db import models

# Create your models here.
from cars.models import Car


class Poster(models.Model):
    car = models.ForeignKey(Car,on_delete=models.PROTECT, related_name='cars')
    img = models.ImageField(upload_to='posters/')
    description = models.CharField(max_length=100)
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.description