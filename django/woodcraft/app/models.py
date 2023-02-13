from django.db import models

# Create your models here.

from django.contrib.auth.models import User





class Project(models.Model):
	name = models.CharField(max_length=30)
	photos = models.CharField(max_length=30)
	description = models.CharField(max_length=300)  
	starting_date = models.DateField()
	finish_date = models.DateField(null=True)

class File(models.Model):
	name = models.CharField(max_length=30)
	measurement = models.ForeignKey(Project, on_delete=models.PROTECT)



class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Student(Person):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Teacher(Person):
	student = models.ForeignKey(Student, on_delete=models.PROTECT)

	class Meta:
		permissions = [
            ("reset_student_password", "Can change the password of students"),
        ]
