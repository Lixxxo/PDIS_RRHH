# Single contract class
import datetime


class Contract:
    def __init__(self, contract_number, employee_rut, employee_full_name, position, salary, project, contract_type,
                 workday, start_date, finish_date):
        self._contract_number = contract_number
        self._employee_rut = employee_rut
        self._employee_full_name = employee_full_name
        self._position = position
        self._salary = salary
        self._project = project
        self._contract_type = contract_type
        self._workday = workday
        self._start_date = start_date
        self._finish_date = finish_date

    @property
    def contract_number(self):
        return self._contract_number

    @property
    def employee_rut(self):
        return self._employee_rut

    @property
    def employee_full_name(self):
        return self._employee_full_name

    @property
    def position(self):
        return self._position

    @property
    def salary(self):
        return self._salary

    @property
    def project(self):
        return self._project

    @property
    def contract_type(self):
        return self._contract_type

    @property
    def workday(self):
        return self._workday

    @property
    def start_date(self):
        return self._start_date

    @property
    def finish_date(self):
        return self._finish_date

    @property
    def validity(self):
        return datetime.datetime.now() > self._finish_date

    @contract_number.setter
    def contract_number(self, value):
        self._contract_number = value

    @employee_rut.setter
    def employee_rut(self, value):
        self._employee_rut = value

    @employee_full_name.setter
    def employee_full_name(self, value):
        self._employee_full_name = value

    @position.setter
    def position(self, value):
        self._position = value

    @salary.setter
    def salary(self, value):
        self._salary = value

    @project.setter
    def project(self, value):
        self._project = value

    @contract_type.setter
    def contract_type(self, value):
        self._contract_type = value

    @workday.setter
    def workday(self, value):
        self._workday = value

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    @finish_date.setter
    def finish_date(self, value):
        self._finish_date = value
