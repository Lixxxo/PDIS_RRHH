from GUI.GUIFunctions import run_gui
from json import load, dump
from Logic.RRHH_System import RRHHSystem

from Model.Employee import Employee
from Model.Contract import Contract


def run():

    try:
        with open('db.json') as f:
            data = load(f)
    except FileNotFoundError:
        with open('db.json', 'w') as outfile:
            data = {"employee": [], "contracts": []}
            dump(data, outfile, indent=4, ensure_ascii=False)

    for r in data["employees"]:

        RRHHSystem.employees.append(
            Employee(
                no_digit_rut=r["rut"].split("-")[0],
                first_name=r["first_name"],
                second_name=r["second_name"],
                paternal_last_name=r["paternal_last_name"],
                maternal_last_name=r["maternal_last_name"],
                nationality=r["nationality"],
                birth_date=r["birth_date"],
                title=r["tittle"],
                address=r['address'],
                mail=r["mail"],
                phone_number=r["phone_number"]
            )
        )

    for r in data["contracts"]:
        RRHHSystem.contracts.append(
            Contract(
                employee_rut=r["employee_rut"],
                employee_fullname=r["employee_fullname"],
                position=r["position"],
                salary=r["salary"],
                project=r["project"],
                contract_type=r["contract_type"],
                workday=r["workday"],
                start_date=r["start_date"],
                finish_date=r["finish_date"],
                validity=r["validity"]
            )
        )

    run_gui()


if __name__ == "__main__":
    run()
