from tkinter import END, filedialog, LEFT
from tkinter.ttk import Button

from GUI.GUI import first_name_entry, second_name_entry, paternal_lastname_entry, maternal_lastname_entry, \
    employee_rut_entry, nationality_entry, birthday_entry, title_entry, address_entry, mail_entry, phone_number_entry, \
    treeview_employees, show_window, contract_employee_rut_entry, employee_fullname_entry, position_entry, salary_entry, \
    project_entry, contract_type_entry, workday_entry, start_date_entry, finish_date_entry, validity_entry, \
    treeview_contracts, bottom
from Logic.RRHH_System import employees, contracts
from Requirements.RRHH_impl import read_linking_file, read_unlinking_file
from resources.Constants import linking_button_txt, unlinking_button_txt


def fill_treeview():
    count = 0
    for employee in employees:
        _values = (
            employee.rut,
            employee.first_name,
            employee.paternal_last_name,
            employee.second_name,
            employee.maternal_last_name,
            employee.nationality,
            employee.birth_date,
            employee.title,
            employee.address,
            employee.mail,
            employee.phone_number)
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
    count += 1
    for contract in contracts:
        _values = (
            contract.contract_number,
            contract.position,
            contract.project,
            contract.validity,
            contract.employee_rut,
            contract.employee_fullname,
            contract.salary,
            contract.contract_type,
            contract.workday,
            contract.start_date,
            contract.finish_date
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


def select_employee_data(e):
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

    # Grab data Values
    values = treeview_employees.item(selected, 'values')

    if not values:
        return

    # Output to entry boxes

    first_name_entry.insert(0, values[1])
    second_name_entry.insert(0, values[3])
    paternal_lastname_entry.insert(0, values[2])
    maternal_lastname_entry.insert(0, values[4])
    employee_rut_entry.insert(0, values[0])
    nationality_entry.insert(0, values[5])
    birthday_entry.insert(0, values[6])
    title_entry.insert(0, values[7])
    address_entry.insert(0, values[8])
    mail_entry.insert(0, values[9])
    phone_number_entry.insert(0, values[10])


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

    contract_employee_rut_entry.insert(0, values[4])
    employee_fullname_entry.insert(0, values[5])
    position_entry.insert(0, values[1])
    salary_entry.insert(0, values[6])
    project_entry.insert(0, values[2])
    contract_type_entry.insert(0, values[7])
    workday_entry.insert(0, values[8])
    start_date_entry.insert(0, values[9])
    finish_date_entry.insert(0, values[10])
    validity_entry.insert(0, values[3])


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

    # Show GUI.
    show_window()

    fill_treeview()
