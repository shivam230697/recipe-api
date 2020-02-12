from django.shortcuts import render
from .serializer import UserSerializer, AuthTokenSerializer
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken,Token
from rest_framework.settings import api_settings


# Create your views here.

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
