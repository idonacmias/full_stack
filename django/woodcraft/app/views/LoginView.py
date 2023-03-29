from django.http import HttpResponseRedirect


from rest_framework.views import APIView

from django.contrib.auth import authenticate, login

from rest_framework.response import Response
from rest_framework import status


class LoginAPIView(APIView):

    def post(self, request):
        print(f'LoginAPIView request.data{request.data}')
        if 'username' and 'password' not in request.data:
            print('expect username and password')
            return Response(status=status.HTTP_401_UNAUTHORIZED)    

        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(f'prev user: {request.user}')
            login(request, user)
            # request.session['user_id'] = user.id
            # request.session.save()
            # print(f'request.session {request.session["user_id"]}')
            print('a valid user')
            print(f'new user: {request.user}')
            
            return Response(status=status.HTTP_202_ACCEPTED)

        else:
            print('not a valid user')            
            return Response(status=status.HTTP_401_UNAUTHORIZED)


