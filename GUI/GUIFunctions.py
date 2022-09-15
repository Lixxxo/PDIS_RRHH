from tkinter import END, filedialog, LEFT, NORMAL, DISABLED
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring
from tkinter.ttk import Button

from GUI.GUI import first_name_entry, second_name_entry, paternal_lastname_entry, maternal_lastname_entry, \
    employee_rut_entry, nationality_entry, birthday_entry, title_entry, address_entry, mail_entry, phone_number_entry, \
    treeview_employees, show_window, contract_employee_rut_entry, employee_fullname_entry, position_entry, salary_entry, \
    project_entry, contract_type_entry, workday_entry, start_date_entry, finish_date_entry, \
    treeview_contracts, bottom, buttons_frame_contracts, buttons_frame_employee, validity_var, contract_type_var, \
    workday_var

from Logic.RRHH_System import RRHHSystem
from Logic.Database_manager import JsonManager
from Model.Contract import Contract
from Model.Employee import Employee
from Requirements.RRHH_impl import read_linking_file, read_unlinking_file, edit_employee, add_employee, delete_employee, \
    edit_contract, add_contract, delete_contract
from resources.Constants import linking_button_txt, unlinking_button_txt


class SelectedData:
    selected_employee, selected_contract = None, None
    employee_index, contract_index = 0, 0
    in_employee_contracts = False


def show_employee_contracts():
    contracts = []

    for contract in RRHHSystem.contracts:
        if contract.employee_rut == employee_rut_entry.get():
            contracts.append(contract)

    fill_treeview_contracts(contracts)


def remove_contract(contract: Contract):
    if not delete_contract(contract):
        return

    deselect_contract()
    if SelectedData.selected_contract:
        fill_treeview_contracts(RRHHSystem.contracts)
        return
    show_employee_contracts()


def add_new_employee(system: RRHHSystem):
    add_employee(new_employee())
    fill_treeview_employees(system)
    pass


def add_new_contract():
    add_contract(new_contract())

    # Show contracts of the employee.
    contracts = []

    for contract in RRHHSystem.contracts:
        if contract.employee_rut == employee_rut_entry.get():
            contracts.append(contract)

    fill_treeview_contracts(contracts)


def update_employee(employee: Employee, index: int):
    if not treeview_employees.selection():
        print("ERROR: Employee not selected.")
        return
    employee.phone_number = employee.phone_number.replace(" ", "")
    edit_employee(employee, index)


def update_contract(contract: Contract, index: int):
    if not treeview_contracts.selection():
        print("ERROR: Contract not selected.")
        return
    edit_contract(contract, index)

    # Show contracts of the employee.
    contracts = []

    for contract in RRHHSystem.contracts:
        if contract.employee_rut == employee_rut_entry.get():
            contracts.append(contract)

    fill_treeview_contracts(contracts)

    fill_treeview_contracts(contracts)


def deselect_employee():
    for item in treeview_employees.get_children():
        treeview_employees.selection_remove(item)


def deselect_contract():
    for item in treeview_contracts.get_children():
        treeview_contracts.selection_remove(item)


def clean_treeview_employees(deselect=True):
    if deselect:
        deselect_employee()

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


def clean_treeview_contracts(deselect=True):
    if deselect:
        deselect_contract()

    contract_employee_rut_entry.config(state=NORMAL)
    employee_fullname_entry.config(state=NORMAL)

    contract_employee_rut_entry.delete(0, END)
    employee_fullname_entry.delete(0, END)
    position_entry.delete(0, END)
    salary_entry.delete(0, END)
    project_entry.delete(0, END)
    contract_type_var.set("Seleccione")
    workday_var.set("Seleccione")
    start_date_entry.delete(0, END)
    finish_date_entry.delete(0, END)
    validity_var.set("Seleccione")


def fill_treeview_employees(system: RRHHSystem):
    JsonManager.save("test.json", system)
    for item in treeview_employees.get_children():
        treeview_employees.delete(item)

    count = 0
    for employee in RRHHSystem.employees:

        phone = employee.phone_number
        phone = phone[:1] + " " + phone[1:]
        phone = phone[:6] + " " + phone[6:]

        _values = (
            employee.rut,
            employee.first_name,
            employee.paternal_last_name,
            employee.title,
            employee.mail,
            phone,
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


def fill_treeview_contracts(contracts):
    # JsonManager.save('test.json', system)
    for item in treeview_contracts.get_children():
        treeview_contracts.delete(item)
    count = 0
    for contract in contracts:
        _values = (
            contract.employee_rut,
            contract.employee_fullname,
            contract.position,
            contract.project,
            contract.start_date,
            contract.finish_date,
            "Sí" if contract.validity else "No",
            contract.salary,
            contract.contract_type,
            contract.workday,
            contract.id
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
    clean_treeview_employees(False)

    # Grab data Number
    selected = treeview_employees.focus()

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

    SelectedData.selected_employee = RRHHSystem.employees[int(selected)]
    SelectedData.employee_index = int(selected)

    # Show contracts of the employee.
    contracts = []

    for contract in RRHHSystem.contracts:
        if contract.employee_rut == employee_rut_entry.get():
            contracts.append(contract)

    fill_treeview_contracts(contracts)

    contract_employee_rut_entry.config(state=NORMAL)
    employee_fullname_entry.config(state=NORMAL)

    contract_employee_rut_entry.delete(0, "end")
    employee_fullname_entry.delete(0, "end")

    fullname = ""

    if len(first_name_entry.get()) > 0:
        fullname += first_name_entry.get()
    if len(second_name_entry.get()) > 0:
        fullname += " " + second_name_entry.get()
    if len(paternal_lastname_entry.get()) > 0:
        fullname += " " + paternal_lastname_entry.get()
    if len(maternal_lastname_entry.get()) > 0:
        fullname += " " + maternal_lastname_entry.get()

    contract_employee_rut_entry.insert(0, employee_rut_entry.get())
    employee_fullname_entry.insert(0, fullname)

    contract_employee_rut_entry.config(state=DISABLED)
    employee_fullname_entry.config(state=DISABLED)


def new_employee():
    return Employee(
        no_digit_rut=employee_rut_entry.get().split('-')[0],
        first_name=first_name_entry.get(),
        second_name=second_name_entry.get(),
        paternal_last_name=paternal_lastname_entry.get(),
        maternal_last_name=maternal_lastname_entry.get(),
        nationality=nationality_entry.get(),
        birth_date=birthday_entry.get(),
        title=title_entry.get(),
        address=address_entry.get(),
        mail=mail_entry.get(),
        phone_number=phone_number_entry.get())


def new_contract():
    return Contract(
        employee_rut=contract_employee_rut_entry.get(),
        employee_fullname=employee_fullname_entry.get(),
        position=position_entry.get(),
        salary=salary_entry.get(),
        project=project_entry.get(),
        contract_type=contract_type_var.get(),
        workday=workday_var.get(),
        start_date=start_date_entry.get(),
        finish_date=finish_date_entry.get(),
        validity=validity_var.get() == "Sí"
    )


def select_contract_data(e):
    contract_employee_rut_entry.config(state=NORMAL)
    employee_fullname_entry.config(state=NORMAL)
    # Clear entry boxes.
    clean_treeview_contracts(False)
    # validity_entry.delete(0, END)

    # Grab data Number
    selected = treeview_contracts.focus()

    # Grab data Values
    values = treeview_contracts.item(selected, 'values')
    # print(values)
    if not values:
        return

    # Output to entry boxes
    validity_var.set("Sí" if values[6] == "Sí" else "No")
    contract_employee_rut_entry.insert(0, values[0])
    employee_fullname_entry.insert(0, values[1])
    position_entry.insert(0, values[2])
    project_entry.insert(0, values[3])
    start_date_entry.insert(0, values[4])
    finish_date_entry.insert(0, values[5])
    salary_entry.insert(0, values[7])
    contract_type_var.set("Temporal" if values[8] == "Media" else "Indefinido")
    workday_var.set("Media" if values[9] == "Media" else "Completa")

    if SelectedData.in_employee_contracts:
        fill_treeview_contracts(RRHHSystem.contracts)
    # print(values[10])
    for i in range(len(RRHHSystem.contracts)):
        print(RRHHSystem.contracts[i].id)
        print(values[10])
        if str(RRHHSystem.contracts[i].id).__eq__(values[10]):
            print("Contract found.")
            SelectedData.selected_contract = RRHHSystem.contracts[i]
            break



    # SelectedData.selected_contract = RRHHSystem.contracts[int(selected)]
    # SelectedData.contract_index = int(selected)

    contract_employee_rut_entry.config(state=DISABLED)
    employee_fullname_entry.config(state=DISABLED)

    print(SelectedData.selected_contract)


def select_linking_file():
    _filepath = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                           filetypes=(("Archivos csv", "*.csv"),))
    read_linking_file(_filepath)


def select_unlinking_file():
    _filepath = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                           filetypes=(("Archivos csv", "*.csv"),))
    read_unlinking_file(_filepath)


def run_gui(system: RRHHSystem):
    # Capture click up event.
    treeview_employees.bind("<ButtonRelease-1>", select_employee_data)
    treeview_contracts.bind("<ButtonRelease-1>", select_contract_data)

    read_linking_files_button = Button(bottom, text=linking_button_txt, command=select_linking_file)
    read_linking_files_button.pack(padx=10, pady=10, side=LEFT)

    read_unlinking_files_button = Button(bottom, text=unlinking_button_txt, command=select_unlinking_file)
    read_unlinking_files_button.pack(padx=10, pady=10, side=LEFT)

    update_employee_button = Button(buttons_frame_employee, text="Actualizar",
                                    command=lambda: [update_employee(new_employee(), SelectedData.employee_index),
                                                     fill_treeview_employees(system)])
    update_employee_button.grid(row=0, column=0, padx=10, pady=10)

    add_employee_button = Button(buttons_frame_employee, text="Agregar",
                                 command=lambda: add_new_employee(system))
    add_employee_button.grid(row=0, column=1, padx=10, pady=10)

    delete_employee_button = Button(buttons_frame_employee, text="Eliminar",
                                    command=lambda: [delete_employee(SelectedData.selected_employee.no_digit_rut),
                                                     fill_treeview_employees(system),
                                                     fill_treeview_contracts(system.contracts)])
    delete_employee_button.grid(row=0, column=2, padx=10, pady=10)

    clean_data_employees_button = Button(buttons_frame_employee, text="Limpiar Celdas",
                                         command=clean_treeview_employees)
    clean_data_employees_button.grid(row=0, column=3, padx=10, pady=10)

    update_contract_button = Button(buttons_frame_contracts, text="Actualizar",
                                    command=lambda: update_contract(new_contract(), SelectedData.contract_index))
    update_contract_button.grid(row=0, column=0, padx=10, pady=10)

    add_contract_button = Button(buttons_frame_contracts, text="Agregar",
                                 command=lambda: add_new_contract())
    add_contract_button.grid(row=0, column=1, padx=10, pady=10)

    delete_contract_button = Button(buttons_frame_contracts, text="Eliminar",
                                    command=lambda: [remove_contract(SelectedData.selected_contract)])
    delete_contract_button.grid(row=0, column=2, padx=10, pady=10)

    clean_data_contracts_button = Button(buttons_frame_contracts, text="Limpiar Celdas",
                                         command=clean_treeview_contracts)
    clean_data_contracts_button.grid(row=0, column=3, padx=10, pady=10)

    show_contracts_button = Button(buttons_frame_contracts, text="Mostrar Todos",
                                   command=lambda: fill_treeview_contracts(system.contracts))
    show_contracts_button.grid(row=0, column=4, padx=10, pady=10)

    fill_treeview_employees(system)

    fill_treeview_contracts(system.contracts)

    # Show GUI.
    show_window()
