from rest_framework import serializers
from patient.models import Patient

class PatientSerializer(serializers.Serializer):

    ID = serializers.CharField()
    name = serializers.CharField()

    class Meta:
        model = Patient
        fields = '__all__'