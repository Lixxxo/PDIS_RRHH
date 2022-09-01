# Single employee class
class Employee:
    def __init__(self, rut, dv, first_name, second_name, paternal_last_name, maternal_last_name, nationality,
                 birth_date, title, address, mail, phone_number):
        self._rut = rut
        self._dv = dv
        self._first_name = first_name
        self._second_name = second_name
        self._paternal_last_name = paternal_last_name
        self._maternal_last_name = maternal_last_name
        self._nationality = nationality
        self._birth_date = birth_date
        self._title = title
        self._address = address
        self._mail = mail
        self._phone_number = phone_number

    @property
    def rut(self):
        return self._rut

    @property
    def dv(self):
        return self._dv

    @property
    def first_name(self):
        return self._first_name

    @property
    def second_name(self):
        return self._second_name

    @property
    def paternal_last_name(self):
        return self._paternal_last_name

    @property
    def maternal_last_name(self):
        return self._maternal_last_name

    @property
    def nationality(self):
        return self._nationality

    @property
    def birth_date(self):
        return self._birth_date

    @property
    def title(self):
        return self._title

    @property
    def address(self):
        return self._address

    @property
    def mail(self):
        return self._mail

    @property
    def phone_number(self):
        return self._phone_number

    @rut.setter
    def rut(self, value):
        self._rut = value

    @dv.setter
    def dv(self, value):
        self._dv = value

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @second_name.setter
    def second_name(self, value):
        self._second_name = value

    @paternal_last_name.setter
    def paternal_last_name(self, value):
        self._paternal_last_name = value

    @maternal_last_name.setter
    def maternal_last_name(self, value):
        self._maternal_last_name = value

    @nationality.setter
    def nationality(self, value):
        self._nationality = value

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = value

    @title.setter
    def title(self, value):
        self._title = value

    @address.setter
    def address(self, value):
        self._address = value

    @mail.setter
    def mail(self, value):
        self._mail = value

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
