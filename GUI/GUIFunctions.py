from tkinter import END, filedialog, LEFT
from tkinter.ttk import Button

from GUI.GUI import first_name_entry, second_name_entry, paternal_lastname_entry, maternal_lastname_entry, \
    employee_rut_entry, nationality_entry, birthday_entry, title_entry, address_entry, mail_entry, phone_number_entry, \
    treeview_employees, show_window, contract_employee_rut_entry, employee_fullname_entry, position_entry, salary_entry, \
    project_entry, contract_type_entry, workday_entry, start_date_entry, finish_date_entry, validity_entry, \
    treeview_contracts, bottom, buttons_frame_contracts, buttons_frame_employee

from Logic.RRHH_System import RRHHSystem
from Requirements.RRHH_impl import read_linking_file, read_unlinking_file
from resources.Constants import linking_button_txt, unlinking_button_txt


def fill_treeview():
    count = 0
    for employee in RRHHSystem.employees:
        _values = (
            employee.rut,
            employee.first_name,
            employee.paternal_last_name,
            employee.title,
            employee.mail,
            employee.phone_number,
            employee.second_name,
            employee.maternal_last_name,
            employee.nationality,
            employee.birth_date,
            employee.address,
            )
        if count % 2 == 0:
            treeview_employees.insert(parent='',
                                      index='end',
                                      iid=str(count),
                                      text='',
                                      values=_values,
                                      tags=('even-row',))
        else:
            treeview_employees.insert(parent='',
                                      index='end',
                                      iid=str(count),
                                      text='',
                                      values=_values,
                                      tags=('odd-row',))
        # Increment counter
        count += 1
    count = 0
    for contract in RRHHSystem.contracts:
        _values = (
            contract.employee_rut,
            contract.employee_fullname,
            contract.position,
            contract.project,
            contract.start_date,
            contract.finish_date,
            contract.validity,
            contract.salary,
            contract.contract_type,
            contract.workday
        )
        if count % 2 == 0:
            treeview_contracts.insert(parent='',
                                      index='end',
                                      iid=str(count),
                                      text='',
                                      values=_values,
                                      tags=('even-row',))
        else:
            treeview_contracts.insert(parent='',
                                      index='end',
                                      iid=str(count),
                                      text='',
                                      values=_values,
                                      tags=('odd-row',))
        # Increment counter
        count += 1


def select_employee_data(event):
    # Clear entry boxes.
    first_name_entry.delete(0, END)
    second_name_entry.delete(0, END)
    paternal_lastname_entry.delete(0, END)
    maternal_lastname_entry.delete(0, END)
    employee_rut_entry.delete(0, END)
    nationality_entry.delete(0, END)
    birthday_entry.delete(0, END)
    title_entry.delete(0, END)
    address_entry.delete(0, END)
    mail_entry.delete(0, END)
    phone_number_entry.delete(0, END)

    # Grab data Number
    selected = treeview_employees.focus()

    print(selected)

    # Grab data Values
    values = treeview_employees.item(selected, 'values')

    if not values:
        return

    # Output to entry boxes

    first_name_entry.insert(0, values[1])
    second_name_entry.insert(0, values[6])
    paternal_lastname_entry.insert(0, values[2])
    maternal_lastname_entry.insert(0, values[7])
    employee_rut_entry.insert(0, values[0])
    nationality_entry.insert(0, values[8])
    birthday_entry.insert(0, values[9])
    title_entry.insert(0, values[3])
    address_entry.insert(0, values[10])
    mail_entry.insert(0, values[4])
    phone_number_entry.insert(0, values[5])


def select_contract_data(e):
    # Clear entry boxes.
    contract_employee_rut_entry.delete(0, END)
    employee_fullname_entry.delete(0, END)
    position_entry.delete(0, END)
    salary_entry.delete(0, END)
    project_entry.delete(0, END)
    contract_type_entry.delete(0, END)
    workday_entry.delete(0, END)
    start_date_entry.delete(0, END)
    finish_date_entry.delete(0, END)
    validity_entry.delete(0, END)

    # Grab data Number
    selected = treeview_contracts.focus()

    # Grab data Values
    values = treeview_contracts.item(selected, 'values')

    if not values:
        return

    # Output to entry boxes

    contract_employee_rut_entry.insert(0, values[0])
    employee_fullname_entry.insert(0, values[1])
    position_entry.insert(0, values[2])
    salary_entry.insert(0, values[3])
    project_entry.insert(0, values[4])
    contract_type_entry.insert(0, values[8])
    workday_entry.insert(0, values[9])
    start_date_entry.insert(0, values[4])
    finish_date_entry.insert(0, values[5])
    validity_entry.insert(0, values[6])



def select_linking_file():
    _filepath = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                           filetypes=(("Archivos csv", "*.csv"),))
    read_linking_file(_filepath)


def select_unlinking_file():
    _filepath = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                           filetypes=(("Archivos csv", "*.csv"),))
    read_unlinking_file(_filepath)


def run_gui():
    # Capture click up event.
    treeview_employees.bind("<ButtonRelease-1>", select_employee_data)
    treeview_contracts.bind("<ButtonRelease-1>", select_contract_data)

    read_linking_files_button = Button(bottom, text=linking_button_txt, command=select_linking_file)
    read_linking_files_button.pack(padx=10, pady=10, side=LEFT)

    read_unlinking_files_button = Button(bottom, text=unlinking_button_txt, command=select_unlinking_file)
    read_unlinking_files_button.pack(padx=10, pady=10, side=LEFT)

    update_employee_button = Button(buttons_frame_employee, text="Actualizar")
    update_employee_button.grid(row=0, column=0, padx=10, pady=10)

    add_employee_button = Button(buttons_frame_employee, text="Agregar")
    add_employee_button.grid(row=0, column=1, padx=10, pady=10)

    delete_employee_button = Button(buttons_frame_employee, text="Eliminar")
    delete_employee_button.grid(row=0, column=2, padx=10, pady=10)

    update_contract_button = Button(buttons_frame_contracts, text="Actualizar")
    update_contract_button.grid(row=0, column=0, padx=10, pady=10)

    add_contract_button = Button(buttons_frame_contracts, text="Agregar")
    add_contract_button.grid(row=0, column=1, padx=10, pady=10)

    delete_contract_button = Button(buttons_frame_contracts, text="Eliminar")
    delete_contract_button.grid(row=0, column=2, padx=10, pady=10)

    fill_treeview()

    # Show GUI.
    show_window()


