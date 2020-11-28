from rest_framework import serializers
from patient.models import PatientInternet

class PatientInternetSerializer(serializers.Serializer):
    Zamechaniya_kuryaschim_detyam20_166_10 = serializers.CharField()
    Zamechaniya_kuryaschim_podrostkam20_167_10 = serializers.CharField()
    Zamechaniya_nezdorovoi_edy_deti21_168_10 = serializers.CharField()
    Zamechaniya_nezdorovaya_eda_podrostki21_169_10 = serializers.CharField()
    Sovety_fiz_aktivnosti_deti22_170_10 = serializers.CharField()
    Sovety_fiz_aktivnosti_podrostki22_171_10 = serializers.CharField()

    class Meta:
        model = PatientInternet
        fields = ['__all__']