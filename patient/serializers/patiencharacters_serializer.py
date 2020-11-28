from rest_framework import serializers
from patient.models import PatientCharacters

class PatientCharactersSerializer(serializers.Serializer):
    Pol_1_1 = serializers.CharField()
    Semya_2_1 = serializers.CharField()
    Religiya_5_1 = serializers.CharField()
    Mesto_prozhivaniya_1gorod_2selo_1_0 = serializers.CharField()
    Obrazovanie_6_1 = serializers.CharField()
    Professiya_7_1 = serializers.CharField()
    Vy_rabotaete_8_1 = serializers.FloatField()
    Vyhod_na_pensiu_9_1 = serializers.FloatField()
    Prekraschenie_raboty_po_bolezni_10_1 = serializers.FloatField()
    Saharnyi_diabet_11_1 = serializers.FloatField()
    Dlitelnost_saharnogo_diabeta_12_1 = serializers.CharField()
    Arterialnaya_gipertenziya_13_1 = serializers.FloatField()
    Dlitelnost_arterialnoi_gipertenzii_14_1 = serializers.FloatField()
    ONMK_15_1 = serializers.FloatField()
    Danost_ONMK_16_1 = serializers.CharField()
    Stenokardiya_IBS_infarkt_miokarda_17_1 = serializers.FloatField()
    Dlitelnost_stenokardii_IBS_infarkta_miokarda_18_1 = serializers.FloatField()
    Serdechnaya_nedostatochnost_19_1 = serializers.FloatField()
    Dlitelnost_serdechnoi_nedostatochnosti_20_1 = serializers.CharField()
    Prochie_zabolevaniya_serdca_21_1 = serializers.FloatField()
    SAD1_1_3 = serializers.FloatField()
    DAD1_2_3 = serializers.FloatField()
    SAD2_3_3 = serializers.FloatField()
    DAD2_4_3 = serializers.FloatField()
    CHSS1_5_3 = serializers.FloatField()
    CHSS2_6_3 = serializers.FloatField()
    OT1_7_3 = serializers.FloatField()
    OT2_8_3 = serializers.FloatField()
    OB1_9_3 = serializers.FloatField()
    OB2_10_3 = serializers.FloatField()
    Ves_11_3 = serializers.FloatField()
    Rost_12_3 = serializers.FloatField()
    Plecho_13_3 = serializers.FloatField()
    Golen_14_3 = serializers.FloatField()
    Golova_15_3 = serializers.FloatField()
    Sila_levaya1_16_3 = serializers.FloatField()
    Sila_levaya2_17_3 = serializers.FloatField()
    Sila_levaya3_18_3 = serializers.FloatField()
    Sila_pravaya1_19_3 = serializers.FloatField()
    Sila_pravaya2_20_3 = serializers.FloatField()
    Sila_pravaya3_21_3 = serializers.FloatField()
    FEV1_22_3 = serializers.FloatField()
    FEV1_23p_3 = serializers.FloatField()
    FVC_24_3 = serializers.FloatField()
    FVC_25_3 = serializers.FloatField()
    PEFR_26_3 = serializers.FloatField()
    PEFRp_27_3 = serializers.FloatField()
    Glukoza_28_3 = serializers.FloatField()
    Trigliceridy_30_3 = serializers.FloatField()
    LPVP_31_3 = serializers.FloatField()
    LPNP_32_3 = serializers.FloatField()
    Ludi_obychno_chestnye_1_2 = serializers.CharField()
    Esli_ya_delau_2_2 = serializers.CharField()
    Reklama_maslo_3_2 = serializers.CharField()
    Reklama_muka_4_2 = serializers.CharField()
    Reklama_ris_5_2 = serializers.CharField()
    Reklama_bezalkogol_6_2 = serializers.CharField()
    Reklama_sneki_7_2 = serializers.CharField()
    Reklama_sigarety_8_2 = serializers.CharField()
    Reklama_alkogol_9_2 = serializers.CharField()
    Pomosch_obsch_organ_10_2 = serializers.CharField()
    Pomosch_OO_kolvo_11_2 = serializers.CharField()
    Pomosch_relig_organ_12_2 = serializers.CharField()
    Poterya_raboty36_17_2 = serializers.FloatField()
    Vyhod_na_pensiu36_18_2 = serializers.FloatField()
    Bankrotstvo36_19_2 = serializers.FloatField()
    Grabezh36_20_2 = serializers.FloatField()
    Razvod36_21_2 = serializers.FloatField()
    Konflikt_v_seme36_22_2 = serializers.FloatField()
    Bolezn36_24_2 = serializers.FloatField()
    Mashina_43_5 = serializers.FloatField()
    Garazh_44_5 = serializers.FloatField()
    Ferma_45_5 = serializers.FloatField()
    Lavka_46_5 = serializers.FloatField()
    Drugoe_47_5 = serializers.FloatField()
    CHast_dohoda_na_edu_49_5 = serializers.CharField()
    CHast_dohoda_na_edu_49_5_50_5 = serializers.CharField()
    Dostatok_po_srav_s_drug_51_5 = serializers.CharField()
    Tip_zhilya_52_5 = serializers.CharField()
    CHislo_komnat_53_5 = serializers.FloatField()
    Ploschad_zhilya_54_5 = serializers.FloatField()




    class Meta:
        model = PatientCharacters
        fields = ['__all__']
