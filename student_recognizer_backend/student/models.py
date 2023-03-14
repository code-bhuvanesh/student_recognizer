from django.db import models

# Create your models here.

# class Student(models.Model):
#     sid = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     contact = models.CharField(max_length=15)
#     # image    = models.ImageField(upload_to=photos_dir, null=True, blank=True, default=None)
#     # filename = models.CharField(max_length=60, blank=True, null=True)
#     class Meta:
#         db_table = "student"
# class Meta:
#     db_table = "student"

class Image(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')

class StudentModel(models.Model):
    regno =  models.CharField(max_length=8)
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.regno + " : " + self.name 
    # sec=models.CharField(max_length=2)
    # course=models.CharField(max_length=20)
    # dob=models.CharField(max_length=10)
    # block=models.CharField(max_length=10)
    # email=models.CharField(max_length=20)
    # mobile_num=models.CharField(max_length=10)
    # parents_number=models.CharField(max_length=10)
    # father_name=models.CharField(max_length=20)
    # mother_name=models.CharField(max_length=20)
    # b_point=models.CharField(max_length=20)
    # ayear=models.CharField(max_length=10)
    # co_ordinator=models.CharField(max_length=20)