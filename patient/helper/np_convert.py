import numpy as np
from PIL import Image
from .resolver import predict

from patient.models import Patient, PatientCharacters, PatientImmutableCharacters, PatientDiet, PatienDietBase, PatientInternet
from ..serializers.patiencharacters_serializer import PatientCharactersSerializer

def fun(ID_0_0):
    pc = PatientCharacters.objects.filter(ID_0_0=ID_0_0).order_by('-date').first()
    paths = []
    if pc.Arterialnaya_gipertenziya_13_1 is None:
        pc.Arterialnaya_gipertenziya_13_1 = 0
    if pc.Stenokardiya_IBS_infarkt_miokarda_17_1 is None:
        pc.Stenokardiya_IBS_infarkt_miokarda_17_1 = 0
    if pc.ONMK_15_1 is None:
        pc.ONMK_15_1 = 0
    if pc.Serdechnaya_nedostatochnost_19_1 is None:
        pc.Serdechnaya_nedostatochnost_19_1 = 0
    if pc.Prochie_zabolevaniya_serdca_21_1 is None:
        pc.Prochie_zabolevaniya_serdca_21_1 = 0

    if pc.Arterialnaya_gipertenziya_13_1>0:
        paths.append('sick/Arterialnaya_gipertenziya_13_1-1/')
    else:
        paths.append('sick/Arterialnaya_gipertenziya_13_1-0/')
    if pc.ONMK_15_1>0:
        paths.append('sick/ONMK_15_1-1/')
    else:
        paths.append('sick/ONMK_15_1-0/')
    if pc.Stenokardiya_IBS_infarkt_miokarda_17_1>0:
        paths.append('sick/Stenokardiya_IBS_infarkt_miokarda_17_1-1/')
    else:
        paths.append('sick/Stenokardiya_IBS_infarkt_miokarda_17_1-0/')
    if pc.Serdechnaya_nedostatochnost_19_1>0:
        paths.append('sick/Serdechnaya_nedostatochnost_19_1-1/')
    else:
        paths.append('sick/Serdechnaya_nedostatochnost_19_1-0/')
    if pc.Prochie_zabolevaniya_serdca_21_1>0:
        paths.append('sick/Prochie_zabolevaniya_serdca_21_1-1/')
    else:
        paths.append('sick/Prochie_zabolevaniya_serdca_21_1-0/')
    pc.Arterialnaya_gipertenziya_13_1 = 0
    pc.ONMK_15_1 = 0
    pc.Stenokardiya_IBS_infarkt_miokarda_17_1 = 0
    pc.Serdechnaya_nedostatochnost_19_1 = 0
    pc.Prochie_zabolevaniya_serdca_21_1 = 0
    pc = PatientCharactersSerializer(pc).data
    res=''
    for value in pc.values():
        if(type(value)==str):
            res+=value[:36]+' '*(36-len(value[:36]))
        if (type(value)!=str):
            res += str(value)[:36] + ' ' * (36 - len(str(str(value)[:36])))
    array = []
    for symbol in res:
        if ord(symbol)>127:
            array.append(ord(symbol)%127+128)
        else:
            array.append(ord(symbol))
    array = np.array(array)
    array = np.reshape(array, (60, 48))

    img = Image.fromarray(array, 'RGB')
    img = img.resize((224, 224), Image.ANTIALIAS)
    json = predict(img)
    return json