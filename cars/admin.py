from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from cars.models import Car


@admin.register(Car)
class CarAdmin(ModelAdmin):
    list_display = ('user','manufacturer',
                    'model','image',
                    'made_data','milleage',
                    'price')
    prepopulated_fields = {'url':('model',),}

