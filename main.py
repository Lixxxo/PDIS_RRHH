import GUI
from json import load


def run():
    # Todo: verify if the db.json exists.
    with open('db.json') as f:
        data = load(f)

    GUI.show_window(data)


if __name__ == "__main__":
    run()
