from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from Heart.resources.value_parse import create_object
from patient.models import Patient, PatientCharacters, PatientImmutableCharacters, PatientDiet, PatienDietBase, PatientInternet



class CreatePatients(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response(200)

    def put(self, request):
        print('debug')
        data = request.data
        create_object(data)
        Patient.objects.get(ID=data['ID_0_0'])
        PatientCharacters.objects.get(ID_0_0=data['ID_0_0'])

        return Response(200)
