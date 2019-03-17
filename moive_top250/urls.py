from django.contrib import admin
from django.urls import path,include

from . import views

app_name='douban'

urlpatterns = [
    path('index/',views.index,name='index'),
    path('moive/<int:movie_id>',views.moive_info,name='moive')
]