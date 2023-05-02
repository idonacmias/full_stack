from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import permission_classes

from django.contrib.auth.models import User

from ..models import Teacher
from ..serializers import TeacherSerializer




# model crud
# @permission_classes([IsAuthenticated])
class TeacherAPIView(APIView):
    def get(self, request,pk=-1):
        if (pk > -1):
            my_model = Teacher.objects.get(id=pk)
            serializer = TeacherSerializer(my_model)

        else:
            my_model = Teacher.objects.all()
            serializer = TeacherSerializer(my_model, many=True)
        
        return Response(serializer.data)

    def post(self, request):
        user = User.objects.create_user(request.data['name'], request.data['email'], request.data['password'])
        Teacher_data = {'user' : user.id}
        serializer = TeacherSerializer(data=Teacher_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        my_model = Teacher.objects.get(pk=pk)
        serializer = TeacherSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        my_model = Teacher.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




