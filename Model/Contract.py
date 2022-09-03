import datetime


# Single contract class
class Contract:
    def __init__(self, contract_number, employee_rut, employee_full_name, position, salary, project, contract_type,
                 workday, start_date, finish_date):
        self.__contract_number = contract_number
        self.__employee_rut = employee_rut
        self.__employee_full_name = employee_full_name
        self.__position = position
        self.__salary = salary
        self.__project = project
        self.__contract_type = contract_type
        self.__workday = workday
        self.__start_date = start_date
        self.__finish_date = finish_date

    @property
    def contract_number(self):
        return self.__contract_number

    @property
    def employee_rut(self):
        return self.__employee_rut

    @property
    def employee_full_name(self):
        return self.__employee_full_name

    @property
    def position(self):
        return self.__position

    @property
    def salary(self):
        return self.__salary

    @property
    def project(self):
        return self.__project

    @property
    def contract_type(self):
        return self.__contract_type

    @property
    def workday(self):
        return self.__workday

    @property
    def start_date(self):
        return self.__start_date

    @property
    def finish_date(self):
        return self.__finish_date

    @property
    def validity(self):
        return datetime.datetime.now() > self.__finish_date

    @contract_number.setter
    def contract_number(self, value):
        self.__contract_number = value

    @employee_rut.setter
    def employee_rut(self, value):
        self.__employee_rut = value

    @employee_full_name.setter
    def employee_full_name(self, value):
        self.__employee_full_name = value

    @position.setter
    def position(self, value):
        self.__position = value

    @salary.setter
    def salary(self, value):
        self.__salary = value

    @project.setter
    def project(self, value):
        self.__project = value

    @contract_type.setter
    def contract_type(self, value):
        self.__contract_type = value

    @workday.setter
    def workday(self, value):
        self.__workday = value

    @start_date.setter
    def start_date(self, value):
        self.__start_date = value

    @finish_date.setter
    def finish_date(self, value):
        self.__finish_date = value
