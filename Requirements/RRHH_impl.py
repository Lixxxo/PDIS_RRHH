"""el joeloop trabaja de pana acá
haga lo que estime conveniente con los tipos de datos
y cualquier weaita que se le ocurra
todo lo que está escrito es una recomendación y debe ser tratada como tal

el metodo read_linking_file tiene un ejemplo para utilizar
json dumps con las clases del modelo, como guia
lo hice ahi porque ya esta asociado a un boton en el gui
atte Lixo xoxoxoxo <3
"""
from Model.Employee import Employee
from Model.Contract import Contract

#region Requerimiento 2

def add_employee():
    pass

def edit_employee():
    pass

def add_contract(rut: str):
    pass

def edit_contract(rut: str):
    pass

#endregion

#region Requerimiento 3

def read_linking_file():
    print("pasa")
    import json
    from random import randint, choice
    names = ["Juan", "Ítalo", "Alejandro", "Evelyn"]

    data = {"employees": []}

    for i in range(10):
        _rut = randint(15_000_000, 27_000_000)
        _name = choice(names)
        e = Employee(
            no_digit_rut=_rut,
            first_name=_name,
            second_name="",
            paternal_last_name="",
            maternal_last_name="",
            nationality="",
            birth_date="",
            title="",
            address="",
            mail="",
            phone_number="")
        for j in range(5):
            c = Contract(
                contract_number=j + 1,
                employee_rut=_rut,
                employee_fullname=_name,
                position="",
                salary="",
                project="",
                contract_type="",
                workday="",
                start_date="",
                finish_date=""
            )
            c = c.__dict__()

        e = e.__dict__()

        e["contracts"] = []
        e["contracts"].append(c)

        data["employees"].append(e)

    with open('db.json', 'w') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)

    pass

def read_unlinking_file():
    print("te traspasa")
    pass

#endregion

#region Requerimiento 4

def generate_report():
    print("vuelve a pasar")
    pass

#endregion