import datetime


# Single contract class
class Contract:
    def __init__(self, employee_rut: str, employee_fullname: str, position: str, salary: int, project: str,
                 contract_type: str, workday: str, start_date: str, finish_date: str, validity: bool):

        self.__employee_rut = employee_rut
        self.__employee_fullname = employee_fullname
        self.__position = position
        self.__salary = salary
        self.__project = project
        self.__contract_type = contract_type
        self.__workday = workday
        self.__start_date = start_date
        self.__finish_date = finish_date
        self.__validity = validity

    @property
    def employee_rut(self):
        return self.__employee_rut

    @property
    def employee_fullname(self):
        return self.__employee_fullname

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
        return self.__validity

    @employee_rut.setter
    def employee_rut(self, value):
        self.__employee_rut = value

    @employee_fullname.setter
    def employee_fullname(self, value):
        self.__employee_fullname = value

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

    @validity.setter
    def validity(self, value):
        self.__validity = value

    def __dict__(self):
        return {"employee_rut": self.__employee_rut,
                "employee_fullname": self.__employee_fullname, "position": self.__position,
                "salary": self.__salary, "project": self.__project, "contract_type": self.__contract_type,
                "workday": self.__workday, "start_date": self.__start_date, "finish_date": self.__finish_date,
                "validity": self.__validity}
