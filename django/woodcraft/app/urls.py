"""woodcraft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views.ProjectAPIView import ProjectAPIView
from .views.TeacherAPIView import TeacherAPIView
from .views.StudentAPIView import StudentAPIView
from .views.testview import TestView
from .views.LoginView import LoginAPIView
from .views.logout import logout_view
from .views.UserProjectAPIView import UserProjectAPIView
from .views.TokenObtainPairView import MyTokenObtainPairView
from .views.test_image import test_image
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('test/', TestView.as_view()),
    path('project/', ProjectAPIView.as_view()),
    path('project/<int:pk>/', ProjectAPIView.as_view()),
    path('user_project/', UserProjectAPIView.as_view()),
    path('teacher/', TeacherAPIView.as_view()),
    path('teacher/<int:pk>/', TeacherAPIView.as_view()),
    path('student/', StudentAPIView.as_view()),
    path('student/<int:pk>/', StudentAPIView.as_view()),
    path('student/teacher/<int:pk>/', StudentAPIView.get_student_of_teacher),
    path('login/', LoginAPIView.as_view()),
    path('logout/', logout_view),
    path('test_image/', test_image),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

