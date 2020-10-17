from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer

# Create your views here.

# Rather than write multiple views we're grouping together all the common behavior into classes called ViewSets.
# We can easily break these down into individual views if we need to, 
# but using viewsets keeps the view logic nicely organized as well as being very concise.

class UserViewSet (viewsets.ModelViewSet):
    #API endpoint
    queryset = User.objects.all().order_by('-date_joined')#getting all fields of model User and ordering by date_joined
    serializer_class = UserSerializer #will use this serializer to convert fields to json
    permission_classes = [permissions.IsAuthenticated]#defines who gets access

class GroupViewSet(viewsets.ModelViewSet):
    #API endpoint
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]#note this is a list. can add more permissions
