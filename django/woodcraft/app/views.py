from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .models import Project, File, Student, Teacher
from .serializers import ProjectSerializer, FileSerializer, StudentSerializer, TeacherSerializer

# Create your views here.

class ProjectView(View):
	def get(self, request, my_id=-1):
		if my_id == -1:
			return HttpResponse('all data')

		else:
			return HttpResponse(f'data key = {my_id}')



def test(request):
	return HttpResponse('test')