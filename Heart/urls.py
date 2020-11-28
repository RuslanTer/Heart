from django.urls import include, path
from rest_framework import routers
from auth import views
from patient.views.create_patient_view import CreatePatients

router = routers.DefaultRouter()
router.register(r'patient', CreatePatients, basename='CreatePatients')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    path('api/patient/', CreatePatients.as_view(), name="createpatients"),
]