from django.shortcuts import render, redirect
from student.models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets


# Create your views here.
class Student(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer