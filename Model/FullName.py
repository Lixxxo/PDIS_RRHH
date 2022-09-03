# Class that represents the full name of a person.
class FullName:
    def __init__(self, first_name, second_name, paternal_last_name, maternal_last_name):
        self.__first_name = first_name
        self.__second_name = second_name
        self.__paternal_last_name = paternal_last_name
        self.__maternal_last_name = maternal_last_name

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

    def __str__(self):
        return self.__first_name + " " + self.__second_name + " " + self.__paternal_last_name + " " + \
               self.__maternal_last_name
