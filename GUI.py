import tkinter as tk
from tkinter.ttk import Button
from Constants import APP_TITLE
# Declare the window.
window = tk.Tk()

# Lock the size of the window.
window.resizable(width=False, height=False)
window.iconbitmap("resources/RRHH.ico")

# Set the window title
window.title(APP_TITLE)

# Declare the contacting button.
contacting_button = Button(text="Leer archivo de contrataciones")

# Declare the unlinking button.
unlinking_button = Button(text="Desvincular trabajador")

# Add the buttons to the grid.
contacting_button.grid(row=2, column=2, sticky="W", pady=2)
unlinking_button.grid(row=2, column=4, sticky="E", pady=2)

# Run the main window.
window.mainloop()
