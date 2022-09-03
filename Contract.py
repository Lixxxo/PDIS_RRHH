# Single contract class
class Contract:
    def __init__(self, contract_number, employee_rut, employee_name, position, salary, project, contract_type,
                 workday, start_date, finish_date, validity):
        self._contract_number = contract_number
        self._employee_rut = employee_rut
        self._employee_name = employee_name
        self._position = position
        self._salary = salary
        self._project = project
        self._contract_type = contract_type
        self._workday = workday
        self._start_date = start_date
        self._finish_date = finish_date
        self._validity = validity

    @property
    def contract_number(self):
        return self._contract_number

    @property
    def employee_rut(self):
        return self._employee_rut
    
    @property
    def employee_name(self):
        return self._employee_name
