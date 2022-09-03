# Single employee class


class Employee:
    def __init__(self, identifier, rut, dv, full_name,
                 nationality, birth_date, title, address, mail, phone_number):
        self._identifier = identifier
        self._rut = rut
        self._dv = dv
        self._full_name = full_name
        self._nationality = nationality
        self._birth_date = birth_date
        self._title = title
        self._address = address
        self._mail = mail
        self._phone_number = phone_number

    @property
    def identifier(self):
        return self._identifier

    @property
    def rut(self):
        return self._rut

    @property
    def dv(self):
        return self._dv

    @property
    def full_name(self):
        return self._full_name

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

    @identifier.setter
    def identifier(self, value):
        self._identifier = value

    @rut.setter
    def rut(self, value):
        self._rut = value

    @dv.setter
    def dv(self, value):
        self._dv = value

    @full_name.setter
    def full_name(self, value):
        self._full_name = value

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
