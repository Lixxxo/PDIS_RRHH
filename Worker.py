# Single worker class
class Worker:
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
    def rut(self, rut):
        self._rut = rut

    @dv.setter
    def dv(self, dv):
        self._dv = dv

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @second_name.setter
    def second_name(self, second_name):
        self._second_name = second_name

    @paternal_last_name.setter
    def paternal_last_name(self, paternal_last_name):
        self._paternal_last_name = paternal_last_name

    @maternal_last_name.setter
    def maternal_last_name(self, maternal_last_name):
        self._maternal_last_name = maternal_last_name

    @nationality.setter
    def nationality(self, nationality):
        self._nationality = nationality

    @birth_date.setter
    def birth_date(self, birth_date):
        self._birth_date = birth_date

    @title.setter
    def title(self, title):
        self._title = title

    @address.setter
    def address(self, address):
        self._address = address

    @mail.setter
    def mail(self, mail):
        self._mail = mail

    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number = phone_number
