from .models import api_auth_user
from rest_framework import serializers

class Auth_User (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = api_auth_user
        fields = ['username','is_staff']