# coding: cp1251
import xlrd
from django.db import models
from patient.models import Patient, PatientCharacters





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
    return name

def transliterate(name):
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
              ':': '', ';': '', '<': '', '>': '', r'\'': '', '"': '', r'\\': '', '/': '', '№': '',
              '[': '', ']': '', '{': '', '}': '', 'ґ': '', 'ї': '', 'є': '', 'Ґ': 'g', 'Ї': 'i',
              'Є': 'e', '—': ''}
    name = ''
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
                dict[name] = sheet.col_values(colnum)[2]
        dict = {}


def create_object(dict):
    print(dict)
    p = Patient.objects.create(ID=dict['ID_0_0'])
    pc = PatientCharacters.objects.create(ID_0_0=dict['ID_0_0'])
    for key, value in dict:
        pc.objects.update(getattr(PatientCharacters, key), value)
    pc.objects.save()
    p.objects.save()