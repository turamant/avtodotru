from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse

from manufacturers.models import Manufacturer


class Car(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT)
    model = models.CharField(max_length=100)
    url = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='cars/')
    made_data = models.DateField(auto_now=False)
    milleage = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.manufacturer} / {self.model}'

    def get_absolute_url(self):
        return reverse('detail_car', kwargs={'slug':self.url})
