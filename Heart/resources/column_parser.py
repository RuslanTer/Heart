import xlrd

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
              ':': '', ';': '', '<': '', '>': '', '\'': '', '"': '', '\\': '', '/': '', '№': '',
              '[': '', ']': '', '{': '', '}': '', 'ґ': '', 'ї': '', 'є': '', 'Ґ': 'g', 'Ї': 'i',
              'Є': 'e', '—': ''}

    for key in slovar:
        name = name.replace(key, slovar[key])
    return name

def get_column_name():
    rb = xlrd.open_workbook('data.xls', formatting_info=True)
    nsheet = rb.nsheets
    my_file = open("fields.txt", "w")
    my_file.close()
    my_file = open("fields.txt", 'a')
    for sheets in range(nsheet):
        sheet = rb.sheet_by_index(sheets)
        for colnum in range(sheet.ncols):
            if type(sheet.col_values(colnum)[2]) == str:
                if len(sheet.col_values(colnum)[2])<100:
                    name = transliterate(sheet.col_values(colnum)[0])
                    field_type = 'models.CharField(max_length=254, null = True)'
            else:
                if type(sheet.col_values(colnum)[2]) == float:
                    name = transliterate(sheet.col_values(colnum)[0])
                    field_type = 'models.FloatField(null=True, blank=True)'
                else:
                    name = transliterate(sheet.col_values(colnum)[0])
                    field_type = 'models.TextField()'

            name = modify_name(name, colnum, sheets)
            my_file.writelines("\n"+name+' = '+ field_type)


def modify_name(name, colnum, sheets):
    number = ''
    name = name.replace('…', '')
    name = name.replace('.', '')

    name = name.replace('__', '_')
    name = name.replace('__', '_')

    for n in name:
        if n.isdigit() or n == '_':
            number += n
        else:
            break
    name = name[len(number):] + number + '_' + str(colnum) + '_' + str(sheets)

    name = name.replace('__', '_')
    if len(name)>63:
        name=name[len(name)-63:]
    return name


get_column_name()