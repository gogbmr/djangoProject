from django.db import models

# Create your models here.
class AllCourses(models.Model):
    coursename=models.CharField(max_length=200)
    insname=models.CharField(max_length=100)

class Details(models.Model):
    course=models.ForeignKey(AllCourses, on_delete=models.CASCADE)
    sp=models.CharField(max_length=500)
    il=models.CharField(max_length=500)