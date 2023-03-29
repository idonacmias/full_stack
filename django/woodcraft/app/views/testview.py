from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status


# //////////test method
# @api_view(['GET'])
class TestView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            my_dict = {'name' : 'bob', 'age' : 13}
            return Response(my_dict)

        else:
            return Response({'name' : 'u r not a user', 'age' : 20})
        

    def post(self, request):
        print('server POST')
        print(request.data)
        request.data['name'] = 'silvia'
        return Response(request.data, status = status.HTTP_201_CREATED)