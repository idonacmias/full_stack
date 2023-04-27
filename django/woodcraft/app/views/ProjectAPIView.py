from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from rest_framework.permissions import IsAuthenticated


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view, permission_classes

from django.contrib.auth.models import User

from ..models import Project
from ..serializers import ProjectSerializer




@permission_classes([IsAuthenticated])
class ProjectAPIView(APIView):
    """
    This class handle the CRUD operations for Project
    """
    def get(self, request,pk=-1):
        """
        Handle GET requests to return a list of Project objects
        """
        if (pk > -1):
            my_model = Project.objects.get(id=pk)
            print(my_model.image)
            serializer = ProjectSerializer(my_model)
            # serializer.data['image'] = ''
            print(dir(serializer))
            print(serializer.__dict__)
            print(serializer.data['image'])

            print(f'comper fileds: {serializer.data["image"] == my_model.image}')
        else:
            my_model = Project.objects.all()
            serializer = ProjectSerializer(my_model, many=True)
        
        return Response(serializer.data)

    def post(self, request):
        """
        Handle POST requests to create a new Project object
        """
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        """
        Handle PUT requests to update an existing Project object
        """
        my_model = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """
        Handle DELETE requests to delete a Project object
		"""
        my_model = Project.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# model crud
# @permission_classes([IsAuthenticated])
# class MyModelView(APIView):
#     """
#     This class handle the CRUD operations for MyModel
#     """
#     def get(self, request):
#         """
#         Handle GET requests to return a list of MyModel objects
#         """
#         my_model = request.user.task_set.all()
#         serializer = TaskSerializer(my_model, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         """
#         Handle POST requests to create a new Task object
#         """
#         # usr =request.user
#         # print(usr)
#         serializer = TaskSerializer(data=request.data, context={'user': request.user})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def put(self, request, pk):
#         """
#         Handle PUT requests to update an existing Task object
#         """
#         my_model = Task.objects.get(pk=pk)
#         serializer = TaskSerializer(my_model, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         """
#         Handle DELETE requests to delete a Task object
#         """
#         my_model = Task.objects.get(pk=pk)
#         my_model.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)













# # ////////////////////////////////login /register
# # login
# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         # Add custom claims
#         token['username'] = user.username
#         # ...
#         return token


# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer

# # register
# @api_view(['POST'])
# def  register(req):
#     username=req.data["username"]
#     password=req.data["password"]
#     # create a new user (encrypt password)
#     try:
#         User.objects.create_user(username=username,password=password)

#     except:
#         return Response("error")    

#     return Response(f"{username} registered")
 






# # @method_decorator(csrf_protect, name='dispatch')
# class ProjectView(View):
# 	def get(self, request, my_id=-1):
# 		if my_id == -1:
# 			data = Project.objects.all()
# 			serializer = ProjectSerializer(data, many=True)
# 			return HttpResponse(serializer)

# 		else:
# 			data = get_object_or_404(Project, id=my_id)
# 			serializer = ProjectSerializer(data, many=True)
# 			return HttpResponse(serializer)
	
# 	def post(self, request, *args, **kwargs):
# 		serializer = ProjectSerializer(data=request.POST)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)

# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





