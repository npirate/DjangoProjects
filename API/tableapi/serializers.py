from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']#define fields to return in response. groups is not available. so always sent blank

class GroupSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url','name']