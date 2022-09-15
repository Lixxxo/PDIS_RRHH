from Model.Employee import Employee
from Model.Contract import Contract
from Logic.RRHH_System import RRHHSystem
from functools import reduce
import os.path
import openpyxl
from datetime import datetime


# region Requerimiento 2

def add_employee(employee: Employee):
    """
    if not RRHHSystem.employees:
        RRHHSystem.employees.append(employee)
        return True

    """
    # e = next((item for item in RRHHSystem.employees if item.no_digit_rut == employee.no_digit_rut))
    for i in RRHHSystem.employees:
        if i.no_digit_rut == employee.no_digit_rut:
            print('existe')
            return False
    '''
    if e:
        # TODO: Show alert message (Pop-up)
        print("Employee already exists")
        return
    '''
    print('no existe')
    RRHHSystem.employees.append(employee)
    return True


def edit_employee(employee: Employee, index: int):
    RRHHSystem.employees[index] = employee


def delete_employee(rut: str):
    for i in range(len(RRHHSystem.employees)):
        if RRHHSystem.employees[i].no_digit_rut == rut:
            RRHHSystem.employees.pop(i)
            return True
    return False


def add_contract(contract: Contract):
    RRHHSystem.contracts.append(contract)


def edit_contract(contract: Contract, index: int):
    RRHHSystem.contracts[index] = contract


def delete_contract(contract: Contract):
    if not contract:
        return False
    print(contract.employee_rut)

    if contract not in RRHHSystem.contracts:
        print("Contract not found.")
        return False

    RRHHSystem.contracts.remove(contract)
    print("Contract deleted.")
    return True
    """
    print(rut)
    print(type(rut))
    for i in range(len(RRHHSystem.contracts)):
        if RRHHSystem.contracts[i].employee_rut == rut:
            RRHHSystem.contracts.pop(i)
            return True
    return False
    """

# endregion

# region Requerimiento 3

def read_linking_file(filepath):
    if filepath[-1] == 'v':
        with open(filepath, 'r') as archivo:
            next(archivo, None)  # Skip header of the .csv
            linea = archivo.readline()
            while linea != '':
                lista = linea.split(';')
                lista = [i.strip() for i in lista]
                if lista[0] != '':
                    employee_data = lista[:5]
                    employee = Employee(no_digit_rut=(employee_data[0]),
                                        first_name=employee_data[2][:employee_data[2].index(' ')],
                                        second_name=employee_data[2][employee_data[2].index(' ') + 1:],
                                        paternal_last_name=employee_data[3],
                                        maternal_last_name=employee_data[4],
                                        nationality='',
                                        birth_date='',
                                        title='',
                                        address='',
                                        mail='',
                                        phone_number=''
                                        )
                    contracts = []
                    contract_data = lista[5:]
                    salary = list(filter(lambda x: x != '.', contract_data[-1][1:]))
                    salary = reduce((lambda x, y: x + y), salary)

                    contract = Contract(employee_rut=employee_data[0],
                                        employee_fullname=employee_data[2],
                                        position=contract_data[2],
                                        salary=int(salary),
                                        project=contract_data[1],
                                        contract_type=contract_data[4],
                                        workday='',
                                        start_date=contract_data[3],
                                        finish_date=contract_data[5],
                                        validity=True)
                    contracts.append(contract)
                    linea = archivo.readline().strip()
                    lista = linea.split(';')
                    lista = [i.strip() for i in lista]
                    # Si entra, es por que la línea pertenece a un contrato(s).
                    while lista[0] == '' and lista != ['']:
                        contract_data = lista[5:]
                        salary = list(filter(lambda x: x != '.', contract_data[-1][1:]))
                        salary = reduce((lambda x, y: x + y), salary)

                        contract = Contract(employee_rut=employee_data[0],
                                            employee_fullname=employee_data[2],
                                            position=contract_data[2],
                                            salary=int(salary),
                                            project=contract_data[1],
                                            contract_type=contract_data[4],
                                            workday='',
                                            start_date=contract_data[3],
                                            finish_date=contract_data[5],
                                            validity=True)
                        contracts.append(contract)
                        linea = archivo.readline()
                        lista = linea.split(';')
                        lista = [i.strip() for i in lista]
            if add_employee(employee):
                for contract in contracts:
                    add_contract(contract)
    return


def read_unlinking_file(filepath):
    if filepath[-1] == 'v':
        with open(filepath, 'r') as archivo:
            next(archivo, None)  # Skip header of the .csv
            linea = archivo.readline()
            while linea != '':
                lista = linea.split(';')
                lista = [i.strip() for i in lista]
                if delete_employee(lista[0]):
                    delete_contract(lista[0])
                    return


# endregion

# region Requerimiento 4

def generate_report():
    pass

# endregion
