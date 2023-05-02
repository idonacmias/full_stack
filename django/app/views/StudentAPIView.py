from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import permission_classes

from django.contrib.auth.models import User

from ..models import Student
from ..serializers import StudentSerializer


from django.http import HttpResponse


# model crud
# @permission_classes([IsAuthenticated])
class StudentAPIView(APIView):
    def get(self, request,pk=-1):

        if (pk > -1):
            my_model = Student.objects.get(id=pk)
            serializer = StudentSerializer(my_model)

        else:
            my_model = Student.objects.all()
            serializer = StudentSerializer(my_model, many=True)
        return Response(serializer.data)

    def post(self, request):
        # print(dir(request))
        # print(f'request.POST: {request.POST}')
        user = User.objects.create_user(request.data['username'], request.data['email'], request.data['password'])
        print(dir(user))
        print(help(user.groups))
        print(type(user.groups))
        student_data = {'user' : user.id}
        serializer = StudentSerializer(data=student_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        my_model = Student.objects.get(pk=pk)
        serializer = StudentSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        my_model = Student.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def options(self, request):
        # breakpoint()
        # print(dir(request))
        # print(request.data)
        print(request)
        return Response()

    @api_view()
    def get_student_of_teacher(request, pk):
        my_model = Student.objects.filter(teacher=pk)
        serializer = StudentSerializer(my_model, many=True)
        
        return Response(serializer.data)



