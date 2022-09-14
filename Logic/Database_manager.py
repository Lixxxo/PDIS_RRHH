from json import dump, load
from Logic.RRHH_System import RRHHSystem
from Model.Employee import Employee
from Model.Contract import Contract


class JsonManager:

    def __init__(self):
        pass

    @classmethod
    def create(cls, db_name: str):
        with open(db_name, 'w') as outfile:
            data = {"employee": [], "contracts": []}
            dump(data, outfile, indent=4, ensure_ascii=False)
            return data

    @classmethod
    def load_file(cls, db_path: str):
        try:
            open(db_path)
        except FileNotFoundError:
            return

        with open(db_path, "r") as infile:
            data = load(infile)

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

    @staticmethod
    def save(self, db_name: str):
        with open(db_name, 'w') as outfile:
            # Converts to dict each data
            _employee = [i.__dict__ for i in RRHHSystem.employees]
            _contract = [i.__dict__ for i in RRHHSystem.contracts]
            data = {"employee": _employee, "contracts": _contract}

            # write json file
            dump(data, outfile, indent=4, ensure_ascii=False)
            return
