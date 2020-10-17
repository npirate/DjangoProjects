from .models import patient_search_api
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

#@api_view(['GET', 'POST'])
#def patient_list (request, format = None):
#    if request.method == 'GET':
#        return Response (patient_search_api.objects.sql(1))
#    elif request.method =='POST':
#        return Response ('This is post request')

class PatientAPI (APIView):
    def get (self, request, format=None): #this is same as if request.method == 'GET'
        #print (request.data.get('count'))
        dict_params = request.data
        print ('following are the incoming parameters')
        print (dict_params)

        #validate incoming parameters here
        if dict_params.get('get_count') is None or dict_params.get('get_count') == '':
            dict_params['get_count'] = 1     
        return Response (patient_search_api.objects.sql(dict_params))

    def post (self, request, format=None): #format defines the format of Response. None means all formats are possible
        return Response ('This is a post request')


