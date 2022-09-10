from tkinter import *
from tkinter.ttk import Button, Treeview
from resources.Constants import (
    APP_TITLE)

# Declare the window.
root = Tk()

# Lock the size of the window.
root.resizable(width=True, height=True)

# Set iconbitmap
root.iconbitmap("resources/RRHH.ico")

# Set the window title
root.title(APP_TITLE)

# Handle header.
header = Frame(root, bg="yellow")
header.pack()

label_title = Label(header, text="Administración de Recursos Humanos")
label_title.pack()

# Declare container for both treeview (employees and contracts).
upper_container = Frame(root)
upper_container.pack(pady=10, padx=10)

# Handle Treeview of employees

# Declare left frame.
left_frame = LabelFrame(upper_container, text="Trabajadores")
left_frame.pack(pady=10, padx=10, side=LEFT)

# Declare Treeview Frame.
treeview_frame = Frame(left_frame)
treeview_frame.pack(pady=10, fill=X)

# Declare Treeview Scrollbar.
treeview_scroll = Scrollbar(treeview_frame)
treeview_scroll.pack(fill=Y, side=RIGHT)

# Declare Employees Treeview.
treeview_employees = Treeview(treeview_frame, yscrollcommand=treeview_scroll.set, selectmode="extended", padding="5px")
treeview_employees.pack(fill=X, padx=10)

# Configure the Scrollbar.
treeview_scroll.config(command=treeview_employees.yview)

# Define Columns
treeview_employees['columns'] = ('First Name', 'Last Name', 'Rut')

# Format Columns
treeview_employees.column('#0', width=0, stretch=NO)
treeview_employees.column("First Name", anchor=W, width=140)
treeview_employees.column("Last Name", anchor=W, width=140)
treeview_employees.column("Rut", anchor=W, width=140)

# Creating Headings
treeview_employees.heading("#0", text="", anchor=W)
treeview_employees.heading("First Name", text="Nombre", anchor=W)
treeview_employees.heading("Last Name", text="Apellido", anchor=W)
treeview_employees.heading("Rut", text="Rut", anchor=W)

# Add striped row tags.
treeview_employees.tag_configure('odd-row', background="White")
treeview_employees.tag_configure('even-row', background="lightblue")

# Add data entry boxes.
data_frame = LabelFrame(left_frame, text="Datos")
data_frame.pack(fill="both", expand=True, padx=10, pady=10)

fn_label = Label(data_frame, text="Primer Nombre")
fn_label.grid(row=0, column=0, padx=10, pady=10)
fn_entry = Entry(data_frame)
fn_entry.grid(row=0, column=1, padx=10, pady=10)

sn_label = Label(data_frame, text="Segundo Nombre")
sn_label.grid(row=0, column=2, padx=10, pady=10)
sn_entry = Entry(data_frame)
sn_entry.grid(row=0, column=3, padx=10, pady=10)

pl_label = Label(data_frame, text="Primer Apellido")
pl_label.grid(row=1, column=0, padx=10, pady=10)
pl_entry = Entry(data_frame)
pl_entry.grid(row=1, column=1, padx=10, pady=10)

ml_label = Label(data_frame, text="Segundo Apellido")
ml_label.grid(row=1, column=2, padx=10, pady=10)
ml_entry = Entry(data_frame)
ml_entry.grid(row=1, column=3, padx=10, pady=10)

r_label = Label(data_frame, text="Rut")
r_label.grid(row=2, column=0, padx=10, pady=10)
r_entry = Entry(data_frame)
r_entry.grid(row=2, column=1, padx=10, pady=10)

n_label = Label(data_frame, text="Nacionalidad")
n_label.grid(row=2, column=2, padx=10, pady=10)
n_entry = Entry(data_frame)
n_entry.grid(row=2, column=3, padx=10, pady=10)

bd_label = Label(data_frame, text="Fecha de nacimiento")
bd_label.grid(row=3, column=2, padx=10, pady=10)
bd_entry = Entry(data_frame)
bd_entry.grid(row=3, column=3, padx=10, pady=10)

t_label = Label(data_frame, text="Título")
t_label.grid(row=3, column=0, padx=10, pady=10)
t_entry = Entry(data_frame)
t_entry.grid(row=3, column=1, padx=10, pady=10)

a_label = Label(data_frame, text="Dirección")
a_label.grid(row=4, column=2, padx=10, pady=10)
a_entry = Entry(data_frame)
a_entry.grid(row=4, column=3, padx=10, pady=10)

m_label = Label(data_frame, text="Correo")
m_label.grid(row=4, column=0, padx=10, pady=10)
m_entry = Entry(data_frame)
m_entry.grid(row=4, column=1, padx=10, pady=10)

pnm_label = Label(data_frame, text="Número de teléfono")
pnm_label.grid(row=5, column=2, padx=10, pady=10)
pnm_entry = Entry(data_frame)
pnm_entry.grid(row=5, column=3, padx=10, pady=10)


# Select Data
def select_employee_data(e):
    # Clear entry boxes.
    fn_entry.delete(0, END)
    sn_entry.delete(0, END)
    pl_entry.delete(0, END)
    ml_entry.delete(0, END)
    r_entry.delete(0, END)
    n_entry.delete(0, END)
    bd_entry.delete(0, END)
    t_entry.delete(0, END)
    a_entry.delete(0, END)
    m_entry.delete(0, END)
    pnm_entry.delete(0, END)

    # Grab data Number
    selected = treeview_employees.focus()

    # Grab data Values
    values = treeview_employees.item(selected, 'values')

    # Output to entry boxes

    fn_entry.insert(0, values[0])
    sn_entry.insert(0, values[1])
    pl_entry.insert(0, values[2])
    ml_entry.insert(0, values[3])
    r_entry.insert(0, values[4])
    n_entry.insert(0, values[5])
    bd_entry.insert(0, values[6])
    t_entry.insert(0, values[7])
    a_entry.insert(0, values[8])
    m_entry.insert(0, values[9])
    pnm_entry.insert(0, values[10])


# Add buttons.
buttons_frame = LabelFrame(left_frame, text="Acciones")
buttons_frame.pack(fill="both", expand=True, padx=10, pady=10)

update_employee_button = Button(buttons_frame, text="Actualizar")
update_employee_button.grid(row=0, column=0, padx=10, pady=10)

add_employee_button = Button(buttons_frame, text="Agregar")
add_employee_button.grid(row=0, column=1, padx=10, pady=10)

delete_employee_button = Button(buttons_frame, text="Eliminar")
delete_employee_button.grid(row=0, column=2, padx=10, pady=10)

# Bind the Treeview
treeview_employees.bind("<ButtonRelease-1>", select_employee_data)

# Handle Treeview of contracts.

# Declare right Frame.
right_frame = LabelFrame(upper_container, text="Contratos")
right_frame.pack(pady=10, padx=10, side=RIGHT, fill=Y)

# Declare Treeview Frame.
treeview_frame = Frame(right_frame)
treeview_frame.pack(pady=10, fill=X)

# Declare Treeview Scrollbar.
treeview_scroll = Scrollbar(treeview_frame)
treeview_scroll.pack(pady=10, side=RIGHT, fill=Y)

# Declare Contracts Treeview.
treeview_contracts = Treeview(treeview_frame, yscrollcommand=treeview_scroll.set, selectmode="extended", padding="5px")
treeview_contracts.pack(fill=X, padx=10)

# Configure the Scrollbar.
treeview_scroll.config(command=treeview_contracts.yview)

# Define Columns
treeview_contracts['columns'] = ('Contract ID', 'Position', 'Project')

# Format Columns
treeview_contracts.column('#0', width=0, stretch=NO)
treeview_contracts.column("Contract ID", anchor=W, width=140)
treeview_contracts.column("Position", anchor=W, width=140)
treeview_contracts.column("Project", anchor=W, width=140)

# Creating Headings
treeview_contracts.heading("#0", text="", anchor=W)
treeview_contracts.heading("Contract ID", text="ID", anchor=W)
treeview_contracts.heading("Position", text="Puesto", anchor=W)
treeview_contracts.heading("Project", text="Proyecto", anchor=W)

# Add striped row tags.
treeview_contracts.tag_configure('odd-row', background="White")
treeview_contracts.tag_configure('even-row', background="lightblue")

# Add data entry boxes.
data_frame = LabelFrame(right_frame, text="Datos")
data_frame.pack(fill="both", expand=True, padx=10, pady=10)

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
pro_entry.grid(row=2, column=1, padx=10, pady=10)

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


# Select Data
def select_contract_data(e):
    # Clear entry boxes.
    er_entry.delete(0, END)
    en_entry.delete(0, END)
    pos_entry.delete(0, END)
    sal_entry.delete(0, END)
    pro_entry.delete(0, END)
    ct_entry.delete(0, END)
    w_entry.delete(0, END)
    sd_entry.delete(0, END)
    fd_entry.delete(0, END)
    v_entry.delete(0, END)

    # Grab data Number
    selected = treeview_contracts.focus()

    # Grab data Values
    values = treeview_contracts.item(selected, 'values')

    # Output to entry boxes

    er_entry.insert(0, values[1])
    en_entry.insert(0, values[2])
    pos_entry.insert(0, values[3])
    sal_entry.insert(0, values[4])
    pro_entry.insert(0, values[5])
    ct_entry.insert(0, values[6])
    w_entry.insert(0, values[7])
    sd_entry.insert(0, values[8])
    fd_entry.insert(0, values[9])
    v_entry.insert(0, values[10])


# Add buttons.
buttons_frame = LabelFrame(right_frame, text="Acciones")
buttons_frame.pack(fill="both", expand=False, padx=10, pady=10)

update_contract_button = Button(buttons_frame, text="Actualizar")
update_contract_button.grid(row=0, column=0, padx=10, pady=10)

add_contract_button = Button(buttons_frame, text="Agregar")
add_contract_button.grid(row=0, column=1, padx=10, pady=10)

delete_contract_button = Button(buttons_frame, text="Eliminar")
delete_contract_button.grid(row=0, column=2, padx=10, pady=10)

# Bind the Treeview
treeview_contracts.bind("<ButtonRelease-1>", select_contract_data)


def show_window(data):
    # Add data to the screen.

    count = 0
    for record in data['employees']:
        if count % 2 == 0:
            treeview_employees.insert(parent='',
                                      index='end',
                                      iid=str(count),
                                      text='',
                                      values=(record['first_name'],
                                              record['second_name'],
                                              record['paternal_last_name'],
                                              record['maternal_last_name'],
                                              record['rut'],
                                              record['nationality'],
                                              record['birth_date'],
                                              record['tittle'],
                                              record['address'],
                                              record['mail'],
                                              record['phone_number']),
                                      tags=('even-row',))
        else:
            treeview_employees.insert(parent='',
                                      index='end',
                                      iid=str(count),
                                      text='',
                                      values=(record['first_name'],
                                              record['second_name'],
                                              record['paternal_last_name'],
                                              record['maternal_last_name'],
                                              record['rut'],
                                              record['nationality'],
                                              record['birth_date'],
                                              record['tittle'],
                                              record['address'],
                                              record['mail'],
                                              record['phone_number']),
                                      tags=('odd-row',))
        # Increment counter
        count += 1
    count += 1
    for record in data['contracts']:
        if count % 2 == 0:
            treeview_contracts.insert(parent='',
                                      index='end',
                                      iid=str(count),
                                      text='',
                                      values=(record['contract_number'],
                                              record['employee_rut'],
                                              record['employee_fullname'],
                                              record['position'],
                                              record['salary'],
                                              record['project'],
                                              record['contract_type'],
                                              record['workday'],
                                              record['start_date'],
                                              record['finish_date'],
                                              record['validity']),
                                      tags=('even-row',))
        else:
            treeview_contracts.insert(parent='',
                                      index='end',
                                      iid=str(count),
                                      text='',
                                      values=(record['contract_number'],
                                              record['employee_rut'],
                                              record['employee_fullname'],
                                              record['position'],
                                              record['salary'],
                                              record['project'],
                                              record['contract_type'],
                                              record['workday'],
                                              record['start_date'],
                                              record['finish_date'],
                                              record['validity']),
                                      tags=('odd-row',))
        # Increment counter
        count += 1

    # Run the main window.
    root.mainloop()
