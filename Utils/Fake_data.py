import json
from random import randint, choice
from Model.Contract import Contract
from Model.Employee import Employee


def fake_db():
    """Generate a fake database and store in db.json"""

    names = ["Juan", "Ítalo", "Alejandro", "Evelyn"]
    lastnames = ["Quispe", "Donoso", "Peña", "Hormazabal"]
    nationalities = ["Chileno", "Zaunita", "Noxiano", "PEruano", "Demaciano", "Piltillo"]


    positions = ["Administrativo", "Soldador", "Mecánico", "Bodeguero"]

    workdays = ["Completa", "Media"]
    project = []
    for i in range(7):
        project.append(''.join([choice("JBGH"), choice("PCOG"), str(randint(111, 666))]))



    contract_types = ["Temporal", "Indefinido"]

    data = {"employees": [], "contracts": []}

    for i in range(15):
        _rut = randint(15_000_000, 27_000_000)
        _name = choice(names)
        _lastname1 = choice(lastnames)
        _lastname2 = choice(lastnames)
        _nationality = choice(nationalities)
        _birth_date = '-'.join([str(randint(0, 31)), str("0" + str(randint(1, 10))), str(randint(1973, 1999))])
        _mail = _name[0].lower() + _lastname1.lower() + "@.ucn.cl"
        _phone = "9" + str(randint(11_111_111, 99_999_999))

        e = Employee(
            no_digit_rut=_rut,
            first_name=_name,
            second_name="",
            paternal_last_name=_lastname1,
            maternal_last_name=_lastname2,
            nationality=_nationality,
            birth_date=_birth_date,
            title="",
            address="",
            mail=_mail,
            phone_number=_phone)

        for j in range(randint(0, 3)):
            _position = choice(positions)
            _salary = randint(2_000, 5_000_000)
            _project = choice(project)
            _contract_type = choice(contract_types)
            _workday = choice(workdays)
            _start_date = '-'.join([str(randint(0, 31)), str("0" + str(randint(1, 10))), str(randint(2019, 2024))])
            _finish_date = '-'.join([str(randint(0, 31)), str("0" + str(randint(1, 10))), str(randint(2019, 2024))])
            c = Contract(
                employee_rut=e.rut,
                employee_fullname=e.fullname,
                position=_position,
                salary=_salary,
                project=_project,
                contract_type=_contract_type,
                workday=_workday,
                start_date=_start_date,
                finish_date=_finish_date,
                validity=False
            )
            data["contracts"].append(c.__dict__)

        data["employees"].append(e.__dict__)

    with open('db.json', 'w') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)
