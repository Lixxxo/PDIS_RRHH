from Model.Employee import Employee
from Model.Contract import Contract
from Logic.RRHH_System import RRHHSystem


# region Requerimiento 2

def add_employee(employee: Employee):
    if not RRHHSystem.employees:
        RRHHSystem.employees.append(employee)
        return
    e = next((item for item in RRHHSystem.employees if item.no_digit_rut == employee.no_digit_rut))
    if e:
        # TODO: Show alert message (Pop-up)
        print("Employee already exists.")
        return

    RRHHSystem.employees.append(employee)


def edit_employee(employee: Employee, index: int):
    if employee is None:
        print("Invalid employee.")
        return

    RRHHSystem.employees[index] = employee


def delete_employee(index: int):
    RRHHSystem.employees.pop(index)


def add_contract(contract: Contract):
    if not RRHHSystem.contracts:
        RRHHSystem.contracts.append(contract)
        return
    print("Contract already exists!")


def edit_contract(contract: Contract, index: int):
    RRHHSystem.contracts[index] = contract


def delete_contract(index: int):
    RRHHSystem.contracts.pop(index)


# endregion

# region Requerimiento 3

def read_linking_file(filepath):
    pass


def read_unlinking_file(filepath):
    pass


# endregion

# region Requerimiento 4

def generate_report():
    pass

# endregion
