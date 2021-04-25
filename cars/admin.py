from django.contrib import admin
from django.utils.safestring import mark_safe

from django.contrib.admin import ModelAdmin

from cars.models import Car, Comment


@admin.register(Car)
class CarAdmin(ModelAdmin):
    list_display = ('user','manufacturer',
                    'model','is_deleted','is_published','image',
                    'made_data','milleage',
                    'price')
    prepopulated_fields = {'url':('model',),}

    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'car', 'created','active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name','email', 'body')