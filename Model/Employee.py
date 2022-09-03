# Single employee class
class Employee:
    def __init__(self, identifier, rut, dv, full_name,
                 nationality, birth_date, title, address, mail, phone_number):
        self.__identifier = identifier
        self.__rut = rut
        self.__dv = dv
        self.__full_name = full_name
        self.__nationality = nationality
        self.__birth_date = birth_date
        self.__title = title
        self.__address = address
        self.__mail = mail
        self.__phone_number = phone_number

    @property
    def identifier(self):
        return self.__identifier

    @property
    def rut(self):
        return self.__rut

    @property
    def dv(self):
        return self.__dv

    @property
    def full_name(self):
        return self.__full_name

    @property
    def nationality(self):
        return self.__nationality

    @property
    def birth_date(self):
        return self.__birth_date

    @property
    def title(self):
        return self.__title

    @property
    def address(self):
        return self.__address

    @property
    def mail(self):
        return self.__mail

    @property
    def phone_number(self):
        return self.__phone_number

    @identifier.setter
    def identifier(self, value):
        self.__identifier = value

    @rut.setter
    def rut(self, value):
        self.__rut = value

    @dv.setter
    def dv(self, value):
        self.__dv = value

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    @nationality.setter
    def nationality(self, value):
        self.__nationality = value

    @birth_date.setter
    def birth_date(self, value):
        self.__birth_date = value

    @title.setter
    def title(self, value):
        self.__title = value

    @address.setter
    def address(self, value):
        self.__address = value

    @mail.setter
    def mail(self, value):
        self.__mail = value

    @phone_number.setter
    def phone_number(self, value):
        self.__phone_number = value
