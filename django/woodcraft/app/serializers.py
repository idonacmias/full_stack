from .models import Project, File, Student, Teacher, Student_project

from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):


    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    class Meta:
        model = Project
        fields = '__all__'



class FileSerializer(serializers.ModelSerializer):
     class Meta:
        model = File
        fields = '__all__'



class StudentSerializer(serializers.ModelSerializer):
     class Meta:
        model = Student
        fields = '__all__'



class TeacherSerializer(serializers.ModelSerializer):
     class Meta:
        model = Teacher
        fields = '__all__'

class Student_projectSerializer(serializers.ModelSerializer):
      class Meta:
         model = Student_project
         fields = '__all__'

# profile_data = validated_data.pop('profile')
# user = User.objects.create(**validated_data)
# UserProfile.objects.create(user=user, **profile_data)
# return user
