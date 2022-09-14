from GUI.GUIFunctions import run_gui
from Logic.Database_manager import JsonManager

from Utils.Fake_data import fake_db


def run():

    # Create a fake db
    # fake_db()
    jm = JsonManager.load_file(db_path='db.json')
    if jm is None:
        jm = JsonManager.create(db_name='db.json')

    # print(json_dict)
    run_gui()


if __name__ == "__main__":
    run()
