from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from Heart.resources.value_parse import create_object
from patient.models import Patient, PatientCharacters, PatientImmutableCharacters, PatientDiet, PatienDietBase, PatientInternet
from ..serializers.patiencharacters_serializer import PatientCharactersSerializer
from ..serializers.patien_serializer import PatientSerializer
from ..serializers.patient_immutable_serializer import PatientImmutableSerializer
from ..serializers.patient_internet_serializer import PatientInternetSerializer
from ..helper.np_convert import fun



class CreatePatients(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        patients = Patient.objects.all()
        patients_json = PatientSerializer(patients, many=True).data
        return Response(patients_json, status=200)

    def put(self, request):
        data = request.data
        create_object(data)
        p = Patient.objects.filter(ID=data['ID_0_0']).first()
        pc = PatientCharacters.objects.filter(ID_0_0=data['ID_0_0']).order_by('-date').first()
        _pc_ = PatientImmutableCharacters.objects.filter(ID_0_0=data['ID_0_0']).order_by('-date').first()
        pcInternet = PatientInternet.objects.filter(ID_0_10=data['ID_0_0']).order_by('-date').first()
        p = PatientSerializer(p).data
        pc = PatientCharactersSerializer(pc).data
        _pc_ = PatientImmutableSerializer(_pc_).data
        pcInternet = PatientInternetSerializer(pcInternet).data
        result = {}
        for item in p.items():
            result[item[0]] = item[1]
        for item in pc.items():
            result[item[0]] = item[1]
        for item in _pc_.items():
            result[item[0]] = item[1]
        AI_RESULT = result
        json = fun(pc['ID_0_0'])
        return Response(json)
