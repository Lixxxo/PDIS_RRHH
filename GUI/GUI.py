from tkinter import Tk, LEFT, X, RIGHT, Y, NO, W, StringVar
from tkinter.ttk import Button, Treeview, Frame, LabelFrame, Scrollbar, Label, Entry, OptionMenu
from tkcalendar import DateEntry

from resources.Constants import (
    APP_TITLE)

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


# Declare container for both treeview (employees and contracts).
upper_container = Frame(header)
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
treeview_employees['columns'] = ('Rut',
                                 'First_name',
                                 'Paternal_last_name',
                                 'Title',
                                 'Mail',
                                 'Phone_number')

# Format Columns
treeview_employees.column('#0', width=0, stretch=NO)
treeview_employees.column("Rut", anchor=W, width=100)
treeview_employees.column("First_name", anchor=W, width=100)
treeview_employees.column("Paternal_last_name", anchor=W, width=100)
treeview_employees.column("Title", anchor=W, width=100)
treeview_employees.column("Mail", anchor=W, width=100)
treeview_employees.column("Phone_number", anchor=W, width=150)

# Creating Headings
treeview_employees.heading("#0", text="", anchor=W)
treeview_employees.heading("Rut", text="Rut", anchor=W)
treeview_employees.heading("First_name", text="Nombre", anchor=W)
treeview_employees.heading("Paternal_last_name", text="Apellido Paterno", anchor=W)
treeview_employees.heading("Title", text="Título", anchor=W)
treeview_employees.heading("Mail", text="Correo", anchor=W)
treeview_employees.heading("Phone_number", text="Número de Teléfono", anchor=W)

# Add striped row tags.
treeview_employees.tag_configure('odd-row', background="White")
treeview_employees.tag_configure('even-row', background="lightblue")

# Add data entry boxes.
data_frame = LabelFrame(left_frame, text="Datos")
data_frame.pack(fill="both", expand=True, padx=10, pady=10)

first_name_label = Label(data_frame, text="Primer Nombre")
first_name_label.grid(row=0, column=0, padx=10, pady=10)
first_name_entry = Entry(data_frame)
first_name_entry.grid(row=0, column=1, padx=10, pady=10)

second_name_label = Label(data_frame, text="Segundo Nombre")
second_name_label.grid(row=0, column=2, padx=10, pady=10)
second_name_entry = Entry(data_frame)
second_name_entry.grid(row=0, column=3, padx=10, pady=10)

paternal_lastname_label = Label(data_frame, text="Primer Apellido")
paternal_lastname_label.grid(row=1, column=0, padx=10, pady=10)
paternal_lastname_entry = Entry(data_frame)
paternal_lastname_entry.grid(row=1, column=1, padx=10, pady=10)

maternal_lastname_label = Label(data_frame, text="Segundo Apellido")
maternal_lastname_label.grid(row=1, column=2, padx=10, pady=10)
maternal_lastname_entry = Entry(data_frame)
maternal_lastname_entry.grid(row=1, column=3, padx=10, pady=10)

employee_rut_label = Label(data_frame, text="Rut")
employee_rut_label.grid(row=2, column=0, padx=10, pady=10)
employee_rut_entry = Entry(data_frame)
employee_rut_entry.grid(row=2, column=1, padx=10, pady=10)

nationality_label = Label(data_frame, text="Nacionalidad")
nationality_label.grid(row=2, column=2, padx=10, pady=10)
nationality_entry = Entry(data_frame)
nationality_entry.grid(row=2, column=3, padx=10, pady=10)

birthday_label = Label(data_frame, text="Fecha de nacimiento")
birthday_label.grid(row=3, column=2, padx=10, pady=10)
birthday_entry = DateEntry(data_frame, date_pattern='dd-MM-yyyy')
birthday_entry.grid(row=3, column=3, padx=10, pady=10)

title_label = Label(data_frame, text="Título")
title_label.grid(row=3, column=0, padx=10, pady=10)
title_entry = Entry(data_frame)
title_entry.grid(row=3, column=1, padx=10, pady=10)

address_label = Label(data_frame, text="Dirección")
address_label.grid(row=4, column=2, padx=10, pady=10)
address_entry = Entry(data_frame)
address_entry.grid(row=4, column=3, padx=10, pady=10)

mail_label = Label(data_frame, text="Correo")
mail_label.grid(row=4, column=0, padx=10, pady=10)
mail_entry = Entry(data_frame)
mail_entry.grid(row=4, column=1, padx=10, pady=10)

phone_number_label = Label(data_frame, text="Número de teléfono")
phone_number_label.grid(row=5, column=2, padx=10, pady=10)
phone_number_entry = Entry(data_frame)
phone_number_entry.grid(row=5, column=3, padx=10, pady=10)

# Add buttons.
buttons_frame_employee = LabelFrame(left_frame, text="Acciones")
buttons_frame_employee.pack(fill="both", expand=True, padx=10, pady=10)


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
treeview_contracts['columns'] = ('Employee_rut',
                                 'Employee_fullname',
                                 'Position',
                                 'Project',
                                 'Start_date',
                                 'Finish_date',
                                 'Validity')

# Format Columns
treeview_contracts.column('#0', width=0, stretch=NO)
treeview_contracts.column("Employee_rut", anchor=W, width=100)
treeview_contracts.column("Employee_fullname", anchor=W, width=150)
treeview_contracts.column("Position", anchor=W, width=100)
treeview_contracts.column("Project", anchor=W, width=100)
treeview_contracts.column("Start_date", anchor=W, width=120)
treeview_contracts.column("Finish_date", anchor=W, width=120)
treeview_contracts.column("Validity", anchor=W, width=100)


# Creating Headings
treeview_contracts.heading("#0", text="", anchor=W)
treeview_contracts.heading("Employee_rut", text="Rut", anchor=W)
treeview_contracts.heading("Employee_fullname", text="Nombre", anchor=W)
treeview_contracts.heading("Position", text="Puesto", anchor=W)
treeview_contracts.heading("Project", text="Proyecto", anchor=W)
treeview_contracts.heading("Start_date", text="Fecha de Inicio", anchor=W)
treeview_contracts.heading("Finish_date", text="Fecha de Término", anchor=W)
treeview_contracts.heading("Validity", text="Vigente", anchor=W)

# Add striped row tags.
treeview_contracts.tag_configure('odd-row', background="White")
treeview_contracts.tag_configure('even-row', background="lightblue")

# Add data entry boxes.
data_frame = LabelFrame(right_frame, text="Datos")
data_frame.pack(fill="both", expand=True, padx=10, pady=10)

contract_employee_rut_label = Label(data_frame, text="Rut Trabajador")
contract_employee_rut_label.grid(row=0, column=0, padx=10, pady=10)
contract_employee_rut_entry = Entry(data_frame)
contract_employee_rut_entry.grid(row=0, column=1, padx=10, pady=10)

employee_fullname_label = Label(data_frame, text="Nombre Trabajador")
employee_fullname_label.grid(row=0, column=2, padx=10, pady=10)
employee_fullname_entry = Entry(data_frame)
employee_fullname_entry.grid(row=0, column=3, padx=10, pady=10)

position_label = Label(data_frame, text="Puesto")
position_label.grid(row=1, column=0, padx=10, pady=10)
position_entry = Entry(data_frame)
position_entry.grid(row=1, column=1, padx=10, pady=10)

salary_label = Label(data_frame, text="Salario")
salary_label.grid(row=1, column=2, padx=10, pady=10)
salary_entry = Entry(data_frame)
salary_entry.grid(row=1, column=3, padx=10, pady=10)

project_label = Label(data_frame, text="Proyecto")
project_label.grid(row=2, column=0, padx=10, pady=10)
project_entry = Entry(data_frame)
project_entry.grid(row=2, column=1, padx=10, pady=10)

contract_type_label = Label(data_frame, text="Tipo de Contrato")
contract_type_label.grid(row=2, column=2, padx=10, pady=10)
contract_type_entry = Entry(data_frame)
contract_type_entry.grid(row=2, column=3, padx=10, pady=10)

workday_label = Label(data_frame, text="Jornada")
workday_label.grid(row=3, column=0, padx=10, pady=10)
workday_entry = Entry(data_frame)
workday_entry.grid(row=3, column=1, padx=10, pady=10)

start_date_label = Label(data_frame, text="Fecha de Inicio")
start_date_label.grid(row=3, column=2, padx=10, pady=10)
# start_date_entry = Entry(data_frame)
#start_date_entry.grid(row=3, column=3, padx=10, pady=10)

start_date_entry = DateEntry(data_frame, selectmode='day', date_pattern='dd-MM-yyyy')
start_date_entry.grid(row=3, column=3, padx=10, pady=10)

finish_date_label = Label(data_frame, text="Fecha de Término")
finish_date_label.grid(row=4, column=0, padx=10, pady=10)
finish_date_entry = DateEntry(data_frame, selectmode="day", date_pattern='dd-MM-yyyy')
finish_date_entry.grid(row=4, column=1, padx=10, pady=10)



'''
validity_label = Label(data_frame, text="Vigente")
validity_label.grid(row=4, column=2, padx=10, pady=10)
validity_entry = Entry(data_frame)
validity_entry.grid(row=4, column=3, padx=10, pady=10)

'''

validity_var = StringVar(data_frame)
# default value

options_list = ["Seleccione una opción", "Sí", "No"]

validity_label = Label(data_frame, text="Vigente")
validity_label.grid(row=4, column=2, padx=10, pady=10)
validity_option_menu = OptionMenu(data_frame, validity_var, *options_list)
validity_option_menu.grid(row=4, column=3, padx=10, pady=10)

bottom = LabelFrame(header, text="Lectura y escritura de archivos")
bottom.pack(fill="both", padx=20, pady=20)

# Add buttons.
buttons_frame_contracts = LabelFrame(right_frame, text="Acciones")
buttons_frame_contracts.pack(fill="both", expand=False, padx=10, pady=10)


def show_window():
    root.mainloop()
