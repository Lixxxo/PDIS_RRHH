from tkinter import *
from tkinter.ttk import Button, Style, Treeview
from resources.Constants import (
    APP_TITLE)

from Utils.Fake_data import fake_db

# Declare the window.
root = Tk()

# Lock the size of the window.
root.resizable(width=False, height=False)

# Set iconbitmap
root.iconbitmap("resources/RRHH.ico")

# Set the window title
root.title(APP_TITLE)

# Handle header.
header = Frame(root)
header.pack()

label_title = Label(header, text="Software de administración de recursos humanos")
label_title.pack()

# Declare container for both treeview (employees and contracts).
upper_container = Frame(root)
upper_container.pack(pady=10, padx=10)

# Handle Treeview of employees
left_frame = LabelFrame(upper_container, text="Trabajadores")
left_frame.pack(pady=10, padx=10, side=LEFT)

treeview_frame = Frame(left_frame)
treeview_frame.pack(pady=10)

treeview_scroll = Scrollbar(treeview_frame)
treeview_scroll.pack(pady=10, side=RIGHT)

treeview = Treeview(treeview_frame, yscrollcommand=treeview_scroll.set, selectmode="extended", padding="5px")
treeview.pack()

treeview['columns'] = ('First Name', 'Last Name', 'Rut')

# Create columns
treeview.column('#0', width=0, stretch=NO)
treeview.column("First Name", anchor=W, width=140)
treeview.column("Last Name", anchor=W, width=140)
treeview.column("Rut", anchor=W, width=140)

# Creating Headings
treeview.heading("#0", text="", anchor=W)
treeview.heading("First Name", text="Nombre", anchor=W)
treeview.heading("Last Name", text="Apellido", anchor=W)
treeview.heading("Rut", text="Rut", anchor=W)

# Add striped row tags.
treeview.tag_configure('oddrow', background="White")
treeview.tag_configure('evenrow', background="lightblue")

# Add data entry boxes.
data_frame = LabelFrame(left_frame, text="Datos")
data_frame.pack(fill="x", expand="yes", padx=10, pady=10)

fn_label = Label(data_frame, text="Primer Nombre")
fn_label.grid(row=0, column=0, padx=10, pady=10)
fn_entry = Entry(data_frame)
fn_entry.grid(row=0, column=1, padx=10, pady=10)

sn_label = Label(data_frame, text="Segundo Nombre")
sn_label.grid(row=0, column=2, padx=10, pady=10)
sn_entry = Entry(data_frame)
sn_entry.grid(row=0, column=3, padx=10, pady=10)

pn_label = Label(data_frame, text="Primer Apellido")
pn_label.grid(row=1, column=0, padx=10, pady=10)
pn_entry = Entry(data_frame)
pn_entry.grid(row=1, column=1, padx=10, pady=10)

mn_label = Label(data_frame, text="Segundo Apellido")
mn_label.grid(row=1, column=2, padx=10, pady=10)
mn_entry = Entry(data_frame)
mn_entry.grid(row=1, column=3, padx=10, pady=10)

n_label = Label(data_frame, text="Nacionalidad")
n_label.grid(row=2, column=0, padx=10, pady=10)
n_entry = Entry(data_frame)
n_entry.grid(row=2, column=1, padx=10, pady=10)

bd_label = Label(data_frame, text="Fecha de nacimiento")
bd_label.grid(row=2, column=2, padx=10, pady=10)
bd_entry = Entry(data_frame)
bd_entry.grid(row=2, column=3, padx=10, pady=10)

t_label = Label(data_frame, text="Título")
t_label.grid(row=3, column=0, padx=10, pady=10)
t_entry = Entry(data_frame)
t_entry.grid(row=3, column=1, padx=10, pady=10)

a_label = Label(data_frame, text="Dirección")
a_label.grid(row=3, column=2, padx=10, pady=10)
a_entry = Entry(data_frame)
a_entry.grid(row=3, column=3, padx=10, pady=10)

m_label = Label(data_frame, text="Correo")
m_label.grid(row=4, column=0, padx=10, pady=10)
m_entry = Entry(data_frame)
m_entry.grid(row=4, column=1, padx=10, pady=10)

pnm_label = Label(data_frame, text="Número de teléfono")
pnm_label.grid(row=4, column=2, padx=10, pady=10)
pnm_entry = Entry(data_frame)
pnm_entry.grid(row=4, column=3, padx=10, pady=10)

# Add buttons.
buttons_frame = LabelFrame(left_frame, text="Acciones")
buttons_frame.pack(fill="both", expand="yes", padx=10, pady=10)

_button = Button(buttons_frame, text="Actualizar")
_button.grid(row=0, column=0, padx=10, pady=10)

_button = Button(buttons_frame, text="Agregar")
_button.grid(row=0, column=1, padx=10, pady=10)

_button = Button(buttons_frame, text="Eliminar")
_button.grid(row=0, column=2, padx=10, pady=10)

# Handle Treeview of contracts.
right_frame = LabelFrame(upper_container, text="Contratos")
right_frame.pack(pady=10, padx=10, side=RIGHT)

treeview_frame = Frame(right_frame)
treeview_frame.pack(pady=10)

treeview_scroll = Scrollbar(treeview_frame)
treeview_scroll.pack(pady=10, side=RIGHT)

treeview = Treeview(treeview_frame, yscrollcommand=treeview_scroll.set, selectmode="extended", padding="5px")
treeview.pack()

treeview['columns'] = ('Contract ID', 'Position', 'Project')

# Create columns
treeview.column('#0', width=0, stretch=NO)
treeview.column("Contract ID", anchor=W, width=140)
treeview.column("Position", anchor=W, width=140)
treeview.column("Project", anchor=W, width=140)

# Creating Headings
treeview.heading("#0", text="", anchor=W)
treeview.heading("Contract ID", text="ID", anchor=W)
treeview.heading("Position", text="Puesto", anchor=W)
treeview.heading("Project", text="Proyecto", anchor=W)

# Add striped row tags.
treeview.tag_configure('oddrow', background="White")
treeview.tag_configure('evenrow', background="lightblue")

# Add data entry boxes.
data_frame = LabelFrame(right_frame, text="Datos")
data_frame.pack(fill="x", expand="yes", padx=10, pady=10)

er_label = Label(data_frame, text="Rut Trabajador")
er_label.grid(row=0, column=0, padx=10, pady=10)
er_entry = Entry(data_frame)
er_entry.grid(row=0, column=1, padx=10, pady=10)

en_label = Label(data_frame, text="Nombre Trabajador")
en_label.grid(row=0, column=2, padx=10, pady=10)
en_entry = Entry(data_frame)
en_entry.grid(row=0, column=3, padx=10, pady=10)

pos_label = Label(data_frame, text="Puesto")
pos_label.grid(row=1, column=0, padx=10, pady=10)
pos_entry = Entry(data_frame)
pos_entry.grid(row=1, column=1, padx=10, pady=10)

sal_label = Label(data_frame, text="Salario")
sal_label.grid(row=1, column=2, padx=10, pady=10)
sal_entry = Entry(data_frame)
sal_entry.grid(row=1, column=3, padx=10, pady=10)

pro_label = Label(data_frame, text="Proyecto")
pro_label.grid(row=2, column=0, padx=10, pady=10)
pro_entry = Entry(data_frame)
n_entry.grid(row=2, column=1, padx=10, pady=10)

ct_label = Label(data_frame, text="Tipo de Contrato")
ct_label.grid(row=2, column=2, padx=10, pady=10)
ct_entry = Entry(data_frame)
ct_entry.grid(row=2, column=3, padx=10, pady=10)

w_label = Label(data_frame, text="Jornada")
w_label.grid(row=3, column=0, padx=10, pady=10)
w_entry = Entry(data_frame)
w_entry.grid(row=3, column=1, padx=10, pady=10)

sd_label = Label(data_frame, text="Fecha de Inicio")
sd_label.grid(row=3, column=2, padx=10, pady=10)
sd_entry = Entry(data_frame)
sd_entry.grid(row=3, column=3, padx=10, pady=10)

fd_label = Label(data_frame, text="Fecha de Término")
fd_label.grid(row=4, column=0, padx=10, pady=10)
fd_entry = Entry(data_frame)
fd_entry.grid(row=4, column=1, padx=10, pady=10)

v_label = Label(data_frame, text="Validez")
v_label.grid(row=4, column=2, padx=10, pady=10)
v_entry = Entry(data_frame)
v_entry.grid(row=4, column=3, padx=10, pady=10)

# Add buttons.
buttons_frame = LabelFrame(right_frame, text="Acciones")
buttons_frame.pack(fill="both", expand="yes", padx=10, pady=10)

_button = Button(buttons_frame, text="Actualizar")
_button.grid(row=0, column=0, padx=10, pady=10)

_button = Button(buttons_frame, text="Agregar")
_button.grid(row=0, column=1, padx=10, pady=10)

_button = Button(buttons_frame, text="Eliminar")
_button.grid(row=0, column=2, padx=10, pady=10)

def show_window(data):
    # Add data to the screen.
    root.mainloop()


'''
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
    
'''
