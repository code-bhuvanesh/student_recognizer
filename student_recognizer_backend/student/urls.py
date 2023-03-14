from django.contrib import admin
from django.urls import path, include
from student import views
from rest_framework import routers

# router = routers.DefaultRouter(trailing_slash=False)
# router.register('images', views.showImages)

urlpatterns = [
path('', views.getRoutes),
path('images/', views.showImages),
path('upload/', views.get_student_details, name='upload_file'),
path('register/', views.registerStudent, name='register student'),
]