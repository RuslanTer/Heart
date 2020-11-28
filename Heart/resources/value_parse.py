# coding: cp1251
import xlrd
from django.db import models
from patient.models import Patient, PatientCharacters





def modify_name(name, colnum, sheets):
    number = ''
    name = name.replace('�', '')
    name = name.replace('.', '')
    for n in name:
        if n.isdigit() or n == '_':
            number += n
        else:
            break
    name = name[len(number):] + number + '_' + str(colnum) + '_' + str(sheets)
    return name

def transliterate(name):
    # ������� � ��������
    slovar = {'�': 'a', '�': 'b', '�': 'v', '�': 'g', '�': 'd', '�': 'e', '�': 'yo',
              '�': 'zh', '�': 'z', '�': 'i', '�': 'i', '�': 'k', '�': 'l', '�': 'm', '�': 'n',
              '�': 'o', '�': 'p', '�': 'r', '�': 's', '�': 't', '�': 'u', '�': 'f', '�': 'h',
              '�': 'c', '�': 'ch', '�': 'sh', '�': 'sch', '�': '', '�': 'y', '�': '', '�': 'e',
              '�': 'u', '�': 'ya', '�': 'A', '�': 'B', '�': 'V', '�': 'G', '�': 'D', '�': 'E', '�': 'YO',
              '�': 'ZH', '�': 'Z', '�': 'I', '�': 'I', '�': 'K', '�': 'L', '�': 'M', '�': 'N',
              '�': 'O', '�': 'P', '�': 'R', '�': 'S', '�': 'T', '�': 'U', '�': 'F', '�': 'H',
              '�': 'C', '�': 'CH', '�': 'SH', '�': 'SCH', '�': '', '�': 'y', '�': '', '�': 'E',
              '�': 'U', '�': 'YA', ',': '', '?': '', ' ': '_', '~': '', '!': '', '@': '', '#': '',
              '$': '', '%': '', '^': '', '&': '', '*': '', '(': '', ')': '', '-': '', '=': '', '+': '',
              ':': '', ';': '', '<': '', '>': '', r'\'': '', '"': '', r'\\': '', '/': '', '�': '',
              '[': '', ']': '', '{': '', '}': '', '�': '', '�': '', '�': '', '�': 'g', '�': 'i',
              '�': 'e', '�': ''}
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