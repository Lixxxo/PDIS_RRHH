import json
from random import randint, choice
from Model.Contract import Contract
from Model.Employee import Employee


def fake_db():
    """Generate a fake database and store in db.json"""

    print("FAKE DB CREATED!")
    names = ["Juan", "Ítalo", "Alejandro", "Evelyn"]
    lastnames = ["Quispe", "Donoso", "Peña", "Hormazabal"]
    data = {"employees": [], "contracts": []}

    for i in range(15):
        _rut = randint(15_000_000, 27_000_000)
        _name = choice(names)
        _lastname1 = choice(lastnames)
        _lastname2 = choice(lastnames)
        e = Employee(
            no_digit_rut=_rut,
            first_name=_name,
            second_name="",
            paternal_last_name=_lastname1,
            maternal_last_name=_lastname2,
            nationality="",
            birth_date="",
            title="",
            address="",
            mail="",
            phone_number="")

        for j in range(randint(0, 3)):
            c = Contract(
                contract_number=int(str(i) + str(j)),
                employee_rut=e.rut,
                employee_fullname=e.fullname,
                position="",
                salary="",
                project="",
                contract_type="",
                workday="",
                start_date="",
                finish_date="",
                validity=True
            )
            data["contracts"].append(c.__dict__())

        data["employees"].append(e.__dict__())

    with open('db.json', 'w') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)

    pass