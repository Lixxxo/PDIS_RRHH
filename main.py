from GUI.GUIFunctions import run_gui
from Logic.Database_manager import JsonManager
from Logic.RRHH_System import RRHHSystem
from Utils.Fake_data import fake_db


def run():

    # Create a fake db
    # fake_db()
    rhs = RRHHSystem()
    _db_name = 'db.json'
    json_dict = JsonManager.load_file(db_path=_db_name, system=rhs)

    if json_dict is not None:
        print(f'No database with name {_db_name}.')
        # JsonManager.create(db_name=_db_name)
        # Create a fake db
        print(f'{_db_name} created.')

    # print(json_dict)
    run_gui(rhs)


if __name__ == "__main__":
    run()
