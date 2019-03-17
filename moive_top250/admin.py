from django.contrib import admin

from . import models
# Register your models here.

class moiveModel(admin.ModelAdmin):
    list_display = ('serial_number','movie_name','datetime')
    list_filter = ('datetime',)

admin.site.register(models.douban_top250,moiveModel)