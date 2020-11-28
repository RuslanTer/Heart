from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from Heart.resources.value_parse import create_object
from patient.models import Patient, PatientCharacters, PatientImmutableCharacters, PatientDiet, PatienDietBase, PatientInternet
from ..serializers.patiencharacters_serializer import PatientCharactersSerializer



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
        data = request.data
        create_object(data)
        first = PatientCharacters.objects.filter(ID_0_0=data['ID_0_0']).order_by('-date').first()
        all = PatientCharacters.objects.all()
        PatientImmutableCharacters.objects.filter(ID_0_0=data['ID_0_0']).order_by('-date').first()
        PatientDiet.objects.filter(ID_0_11=data['ID_0_0']).order_by('-date').first()
        PatienDietBase.objects.filter(ID_0_9=data['ID_0_0']).order_by('-date').first()
        PatientInternet.objects.filter(ID_0_10=data['ID_0_0']).order_by('-date').first()
        return Response(200)
