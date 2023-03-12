from django.apps import AppConfig
from django.contrib import admin
from django.urls import path, include
from student import views
from rest_framework import routers

class StudentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'student'


    router = routers.DefaultRouter(trailing_slash=False)
    router.register('studentdetails', views.Student)

    urlpatterns = [
    path('', include(router.urls)),
]