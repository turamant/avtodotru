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
    is_deleted = models.BooleanField(null=True)
    is_published = models.BooleanField(null=True)

    def __str__(self):
        return f'{self.manufacturer} / {self.model}'

    def get_absolute_url(self):
        return reverse('detail_car', kwargs={'slug':self.url})

class Comment(models.Model):
    car = models.ForeignKey(to=Car,
                            on_delete=models.CASCADE,
                            related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.car}'
