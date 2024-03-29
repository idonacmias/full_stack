from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
	name = models.CharField(max_length=30)
	image = models.ImageField(upload_to='images/')
	description = models.CharField(max_length=300)  


class File(models.Model):
	name = models.CharField(max_length=30)
	measurement = models.ForeignKey(Project, on_delete=models.PROTECT)



class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Teacher(Person):
	pass
	# class Meta:
	# 	permissions = [
    #         ("reset_student_password" "Can change the password of students"),
    #     ]

class Student(Person):
	teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
	

class Student_project(models.Model):
	student = models.ForeignKey(Student, on_delete=models.PROTECT)
	project = models.ForeignKey(Project, on_delete=models.PROTECT)
	starting_date = models.DateField()
	finish_date = models.DateField(null=True)