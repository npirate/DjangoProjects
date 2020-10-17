from django.shortcuts import render
from rawsql.models import rawsql
from rest_framework import viewsets
from .serializers import RawsqlSerializer

# Create your views here.

class RawsqlViewSet (viewsets.ModelViewSet):
    queryset = rawsql.objects.raw('select * from fn_get_staff(%s)',['True'])
    serializer_class = RawsqlSerializer