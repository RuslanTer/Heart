from patient.models import PatientImmutableCharacters
from rest_framework import serializers

class PatientImmutableSerializer(serializers.Serializer):
    Pol_1_1 = serializers.CharField()
    Etnos_3_1 = serializers.CharField()
    Nacionalnost_4_1 = serializers.CharField()

    class Meta:
        model = PatientImmutableCharacters
        fields = '__all__'