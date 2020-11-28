# coding: utf-8
import xlrd
from django.db import models
from patient.models import Patient, PatientCharacters, PatientImmutableCharacters, PatientDiet, PatienDietBase, PatientInternet
from russian_names import RussianNames




def modify_name(name, colnum, sheets):
    number = ''
    name = name.replace('…', '')
    name = name.replace('.', '')
    for n in name:
        if n.isdigit() or n == '_':
            number += n
        else:
            break
    name = name[len(number):] + number + '_' + str(colnum) + '_' + str(sheets)

    name = name.replace('__', '_')
    if len(name) > 63:
        name = name[len(name) - 63:]
    return name

def transliterate(name):
    name=str(name)
    # Слоаврь с заменами
    slovar = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
              'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
              'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
              'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e',
              'ю': 'u', 'я': 'ya', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'YO',
              'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
              'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H',
              'Ц': 'C', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SCH', 'Ъ': '', 'Ы': 'y', 'Ь': '', 'Э': 'E',
              'Ю': 'U', 'Я': 'YA', ',': '', '?': '', ' ': '_', '~': '', '!': '', '@': '', '#': '',
              '$': '', '%': '', '^': '', '&': '', '*': '', '(': '', ')': '', '-': '', '=': '', '+': '',
              ':': '', ';': '', '<': '', '>': '', '\'': '', '"': '', '\\': '', '/': '', '№': '',
              '[': '', ']': '', '{': '', '}': '', 'ґ': '', 'ї': '', 'є': '', 'Ґ': 'g', 'Ї': 'i',
              'Є': 'e', '—': ''}
    for key in slovar:
        name = name.replace(key, slovar[key])
    return name

def create_rows():
    rb = xlrd.open_workbook('data.xls', formatting_info=True)
    nsheet = rb.nsheets
    dict = {}
    for rows in range(2, 1590):
        for sheets in range(nsheet):
            sheet = rb.sheet_by_index(sheets)
            for colnum in range(sheet.ncols):
                name = transliterate(sheet.col_values(colnum)[0])
                name = modify_name(name, colnum, sheets)
                dict[name] = sheet.col_values(colnum)[rows]
        create_object(dict)
        print(rows,'/',1590)
        dict = {}


def create_object(dict):
    p = Patient.objects.create(ID=dict['ID_0_0'], name = RussianNames().get_person())
    pc = PatientCharacters.objects.create(ID_0_0=dict['ID_0_0'])
    _pc_ = PatientImmutableCharacters.objects.create(ID_0_0=dict['ID_0_0'])
    _pDiet_ = PatientDiet.objects.create(ID_0_11=dict['ID_0_0'])
    _pDietBase_ = PatienDietBase.objects.create(ID_0_9=dict['ID_0_0'])
    _pcI_ = PatientInternet.objects.create(ID_0_10=dict['ID_0_0'])

    for item in dict.items():
        key = item[0]
        value = item[1]
        if value=='':
            value = None

        if key in dir(PatientImmutableCharacters):
            if (PatientImmutableCharacters._meta.get_field(key).get_internal_type()=='FloatField' and type(value)!=float):
                value = -1
            if (PatientImmutableCharacters._meta.get_field(key).get_internal_type()=='CharField' and type(value)!=str):
                value = str(value)
            setattr(_pc_, key, value)

        if key in dir(PatientCharacters):
            if (PatientCharacters._meta.get_field(key).get_internal_type()=='FloatField' and type(value)!=float):
                value = -1
            if (PatientCharacters._meta.get_field(key).get_internal_type()=='CharField' and type(value)!=str):
                value = str(value)
            setattr(pc, key, value)

        if key in dir(PatientDiet):
            if (PatientDiet._meta.get_field(key).get_internal_type() == 'FloatField' and type(value) != float):
                value = -1
            if (PatientDiet._meta.get_field(key).get_internal_type() == 'CharField' and type(value) != str):
                value = str(value)
            setattr(_pDiet_, key, value)

        if key in dir(PatienDietBase):
            if (PatienDietBase._meta.get_field(key).get_internal_type() == 'FloatField' and type(value) != float):
                value = -1
            if (PatienDietBase._meta.get_field(key).get_internal_type() == 'CharField' and type(value) != str):
                value = str(value)
            setattr(_pDietBase_, key, value)

        if key in dir(PatientInternet):
            if (PatientInternet._meta.get_field(key).get_internal_type() == 'FloatField' and type(value) != float):
                value = -1
            if (PatientInternet._meta.get_field(key).get_internal_type() == 'CharField' and type(value) != str):
                value = str(value)
            setattr(_pcI_, key, value)

    _pc_.save()
    pc.save()
    p.save()
    _pDiet_.save()
    _pDietBase_.save()
    _pcI_.save()
