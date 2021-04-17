from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from posters.models import Poster


@admin.register(Poster)
class PosterAdmin(ModelAdmin):
    list_display = ('car','img',
                    'description',
                    )
    prepopulated_fields = {'url':('description',),}