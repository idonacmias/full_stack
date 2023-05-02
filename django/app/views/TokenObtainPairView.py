
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.decorators import api_view



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):

        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        # token['grup'] = user.grup #TODO: add grup to user 
        print('user confairm')

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer





@api_view(['GET'])
def getRoutes(request):
	print('getRoutes')
	routes = [
        '/api/token',
        '/api/token/refresh',
    ]

	return Response(routes)
