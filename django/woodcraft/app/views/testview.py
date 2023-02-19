from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

# //////////test method
@api_view(['GET'])
def testview(req):
    return Response("<h1>welcome to my project -  server a live</h1>")
