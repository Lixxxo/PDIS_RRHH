import tkinter as tk
from tkinter.ttk import Button, Style
from resources.Constants import (
    APP_TITLE)
from Requirements.RRHH_impl import (
    read_linking_file,
    read_unlinking_file,
    generate_report)


def show_window(data: {}):
    # Declare the window.
    window = tk.Tk()

    # Lock the size of the window.
    window.resizable(width=False, height=False)
    window.iconbitmap("resources/RRHH.ico")

    # Set the window title
    window.title(APP_TITLE)

    # Declare the read linking file button.
    linking_button = Button(window,
                            text="Leer archivo\nde contrataciones",
                            command=read_linking_file)

    # Declare the read unlinking file button.
    unlinking_button = Button(window,
                              text="Leer archivo\nde desvinculaciones",
                              command=read_unlinking_file)

    # Declare the export report button.
    generate_report_button = Button(window,
                                    text="Generar reporte de pana",
                                    command=generate_report)

    # Add the buttons to the grid.
    linking_button.grid(row=0, column=0, sticky="W", pady=2)
    unlinking_button.grid(row=0, column=2, sticky="E", pady=2)
    generate_report_button.grid(row=1, column=1, sticky="W", pady=2)

    # Run the main window.
    window.mainloop()
