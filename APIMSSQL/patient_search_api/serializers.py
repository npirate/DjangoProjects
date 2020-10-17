from .models import patient_search_api
from rest_framework import serializers

class Patient_search_sr (serializers.Serializer):
    row_no = serializers.IntegerField()
    PatientUID = serializers.CharField(max_length=100)
    Fname = serializers.CharField(max_length=25)
    Lname = serializers.CharField(max_length=25)
    Gender = serializers.CharField(max_length=10)
    DOB = serializers.DateField()
    Mob = serializers.CharField(max_length=25)
    count = serializers.IntegerField()