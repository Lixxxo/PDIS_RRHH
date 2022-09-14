from GUI.GUIFunctions import run_gui
from json import load


def run():
    # Todo: verify if the db.json exists.
    with open('db.json') as f:
        data = load(f)

    run_gui()


if __name__ == "__main__":
    run()
