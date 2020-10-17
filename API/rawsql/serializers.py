from rawsql.models import rawsql
from rest_framework import serializers

class RawsqlSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = rawsql
        fields = ['u_name','staff'] 