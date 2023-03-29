from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from django.contrib import auth 
from django.conf import settings


from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# model crud
# @permission_classes([IsAuthenticated])
class UserProjectAPIView(APIView):
    def get(self, request):
        print(f'dir auth: {dir(auth)}')
        print(f'backends: {auth.backends}')
        print(f'dir backends: {dir(auth.backends)}')


        print(request.user.is_authenticated)
        print(f'User: {User}')
        print(dir(User))
        print(f'User.username: {User.username}')
        print(dir(User.username))
        print(f'User.username.field: {User.username.field}')
        print(settings.AUTH_USER_MODEL)
        
        print(request.user)
        return Response()
    # def post(self, request):
    #     user = User.objects.create_user(request.data['name'], request.data['email'], request.data['password'])
    #     Teacher_data = {'user' : user.id}
    #     serializer = TeacherSerializer(data=Teacher_data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
            
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def put(self, request, pk):
    #     my_model = Teacher.objects.get(pk=pk)
    #     serializer = TeacherSerializer(my_model, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
        
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def delete(self, request, pk):
    #     my_model = Teacher.objects.get(pk=pk)
    #     my_model.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)




