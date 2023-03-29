from django.contrib.auth import logout

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def logout_view(request):
    print(f'request dict: {request.__dict__.keys()}')
    print(f'logout user{request.user}')
    print(f"user_id {request.session.get('user_id')}")

    logout(request)
    return Response()
