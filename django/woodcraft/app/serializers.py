from .models import Project, File, Student, Teacher

from rest_framework import serializers

class ProjectSerializer(serializers.Serializer):
     class Meta:
        model = Project
        fields = '__all__'



class FileSerializer(serializers.Serializer):
     class Meta:
        model = File
        fields = '__all__'



class StudentSerializer(serializers.Serializer):
     class Meta:
        model = Student
        fields = '__all__'



class TeacherSerializer(serializers.Serializer):
     class Meta:
        model = Teacher
        fields = '__all__'