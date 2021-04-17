from django.contrib import admin

# Register your models here.
from manufacturers.models import Manufacturer


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name','state','city')
    prepopulated_fields = {'url':('name',),}