import GUI
from json import load


def run():
    with open('db.json') as f:
        data = load(f)

    GUI.show_window(data)


if __name__ == "__main__":
    run()