from django.shortcuts import render
from .models import api_auth_user
from .serializers import Auth_User
from rest_framework import viewsets

# Create your views here.

class AuthUserViewSet (viewsets.ModelViewSet):
    queryset = api_auth_user.objects.raw('exec sp_users @is_staff = %s',[3])
    serializer_class = Auth_User