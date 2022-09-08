import tkinter as tk
from tkinter.ttk import Button, Style, Treeview
from resources.Constants import (
    APP_TITLE)
from Requirements.RRHH_impl import (
    read_linking_file,
    read_unlinking_file,
    generate_report)

# Declare the window.
window = tk.Tk()

# Set style
style = Style()

# style.theme_use('default')

# Configure the Treeview Colors.
style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")

# Change selected color.
style.map('Treeview',
          background=[('selected', "#347083")])

# Create a Treeview Frame
tree_frame = tk.Frame(window)
tree_frame.pack(pady=10)

# Create a Treeview Scrollbar
tree_scroll = tk.Scrollbar(tree_frame)
tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

# Create the Treeview
my_tree = Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended", padding="5px")

my_tree.pack()

# Configure the Scrollbar.
tree_scroll.config(command=my_tree.yview)

# Define columns
my_tree['columns'] = ("Nombre", "Apellido", "Rut")

# Format columns
my_tree.column("#0", width=0, stretch=tk.NO)
my_tree.column("Nombre", anchor=tk.W, width=140)
my_tree.column("Apellido", anchor=tk.W, width=140)
my_tree.column("Rut", anchor=tk.W, width=140)

# Creating Headings
my_tree.heading("0", text="", anchor=tk.W)
my_tree.heading("Nombre", text="Nombre", anchor=tk.W)
my_tree.heading("Apellido", text="Apellido", anchor=tk.W)
my_tree.heading("Rut", text="Rut", anchor=tk.W)


# Add striped row tags.
my_tree.tag_configure('oddrow', background="White")
my_tree.tag_configure('evenrow', background="lightblue")


# Add Buttons
button_frame = tk.LabelFrame(window, text="Commands")
button_frame.pack(fill="both", expand="yes", padx=20,)

#left = tk.Label(button_frame, text="Inside the LabelFrame")
#left.pack()

_button = Button(button_frame, text="Leer archivo \nde contrataciones")
# _button.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
_button.pack(fill="both")

_button = Button(button_frame, text="Leer archivo \nde desvinculaciones")
# _button.grid(row=0, column=1, padx=10, pady=10, sticky=tk.E)
_button.pack(fill="both")

# _button = Button(button_frame, text="Generar \nreporte")
# _button.grid(row=0, column=2, padx=10, pady=10)

# Lock the size of the window.
# window.resizable(width=False, height=False)
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
# linking_button.grid(row=0, column=0, sticky="W", pady=2)
# unlinking_button.grid(row=0, column=2, sticky="E", pady=2)
# generate_report_button.grid(row=1, column=1, sticky="W", pady=2)


def show_window(data):
    # Add data to the screen.
    global count
    count = 0

    for record in data['employees']:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record['first_name'], record['paternal_last_name'], record['rut']),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record['first_name'], record['paternal_last_name'], record['rut']),
                           tags=('oddrow',))
        # Increment counter
        count += 1

    # Run the main window.
    window.mainloop()
