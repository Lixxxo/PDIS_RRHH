# Single employee class
class Employee:
    def __init__(self, no_digit_rut: int, first_name: str, second_name: str,
                 paternal_last_name: str, maternal_last_name: str, nationality: str, birth_date: str,
                 title: str, address: str, mail: str, phone_number: str):
        self.__no_digit_rut = no_digit_rut
        self.__first_name = first_name
        self.__second_name = second_name
        self.__paternal_last_name = paternal_last_name
        self.__maternal_last_name = maternal_last_name
        self.__nationality = nationality
        self.__birth_date = birth_date
        self.__title = title
        self.__address = address
        self.__mail = mail
        self.__phone_number = phone_number

    @property
    def no_digit_rut(self):
        return self.__no_digit_rut

    @property
    def first_name(self):
        return self.__first_name

    @property
    def second_name(self):
        return self.__second_name

    @property
    def paternal_last_name(self):
        return self.__paternal_last_name

    @property
    def maternal_last_name(self):
        return self.__maternal_last_name

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

    @no_digit_rut.setter
    def no_digit_rut(self, value):
        self.__no_digit_rut = value

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @second_name.setter
    def second_name(self, value):
        self.__second_name = value

    @paternal_last_name.setter
    def paternal_last_name(self, value):
        self.__paternal_last_name = value

    @maternal_last_name.setter
    def maternal_last_name(self, value):
        self.__maternal_last_name = value

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

    @property
    def rut_digit(self):
        # https://gist.github.com/rbonvall/464824
        from itertools import cycle

        reversed_digits = map(int, reversed(str(self.__no_digit_rut)))
        factors = cycle(range(2, 8))
        s = sum(d * f for d, f in zip(reversed_digits, factors))

        dv = (-s) % 11

        if dv == 10:
            dv = "K"

        return dv

    @property
    def rut(self):
        return str(self.__no_digit_rut) + "-" + str(self.rut_digit)

    @property
    def fullname(self):
        _fullname = (self.__first_name + " " + self.__second_name + " " +
                     self.__paternal_last_name + " " + self.__maternal_last_name)
        return _fullname
