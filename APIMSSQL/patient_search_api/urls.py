from django.urls import path
from patient_search_api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('patient_list/', views.PatientAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)