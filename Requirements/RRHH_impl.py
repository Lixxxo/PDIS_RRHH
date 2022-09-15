import json
import openpyxl

from Model.Employee import Employee
from Model.Contract import Contract


# region Requerimiento 2
'''
'''
def add_employee(employee_data):
    e = Employee(
                no_digit_rut=employee_data[1],
                first_name=employee_data[2][0:employee_data[2].index(' ')],
                second_name=employee_data[2][employee_data[2].index(' ') + 1:],
                paternal_last_name=employee_data[3],
                maternal_last_name=employee_data[4],
                nationality="",
                birth_date="",
                title="",
                address="",
                mail="",
                phone_number="")

    pass


def edit_employee():
    pass


def add_contract(rut: str):
    pass


def edit_contract(rut: str):
    pass


# endregion

# region Requerimiento 3
'''
'''
def read_linking_file():
    '''
    with open('resources/contrataciones.csv','r') as archivo:
        next(archivo, None) # Skip header of the .csv
        linea = archivo.readline()
        while linea != '':
            lista = linea.split(';')
            lista = [i.strip() for i in lista]
            if not exists(lista[0]) and lista[0] != '':
                add_employee(lista[:4])
                linea = archivo.readline().strip()
                lista = linea.split(';')
                lista = [i.strip() for i in lista]
                # Si entra, es por que la línea pertenece a un contrato(s).
                while lista[0] == '' and linea != '':
                    linea = archivo.readline()
                    lista = linea.split(';')
                    lista = [i.strip() for i in lista]
'''
    # Open the Workbook
    workbook = openpyxl.load_workbook('resources/contrataciones.xlsx')
    # Open the worksheet
    worksheet = workbook.active
    for i in range(1, worksheet.max_row + 1):
        row = [cell.value for cell in worksheet[i]]  # sheet[n] gives nth row (list of cells)
        print(row)  # list of cell values of this row





def read_unlinking_file():
    '''
    with open('resources/desvinculaciones.csv', 'r') as archivo:
        next(archivo, None)
        linea = archivo.readline().strip()
        while linea != '':
            # Aquí se lee la línea del empleado
            lista = linea.split(';')

            # Si entra, es por que la línea pertenece a un contrato(s).
            while lista[0] == '' and linea != '':
                print(lista)
                linea = archivo.readline().strip()
                lista = linea.split(';')
            print(lista)
            linea = archivo.readline().strip()
    '''
    workbook = openpyxl.load_workbook('resources/desvinculaciones.xlsx')
    # Open the worksheet
    worksheet = workbook.active
    for i in range(1, worksheet.max_row + 1):
        row = [cell.value for cell in worksheet[i]]  # sheet[n] gives nth row (list of cells)
        print(row)  #


#TODO: Remove load data from db. Use class
def exists(rut):
    with open('db.json') as data_file:
        db = json.load(data_file)
    for employee in db['employees']:
        if rut == employee['rut']:
            return True
    return False
# endregion

# region Requerimiento 4

def generate_report():
    pass

# endregion
