from django.shortcuts import render

from django.http import HttpResponse


def test_image(request):
	return render(request, template_name='test_image.html')