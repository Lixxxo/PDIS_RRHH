class FullName:
    def __init__(self, first_name, second_name, paternal_last_name, maternal_last_name):
        self._first_name = first_name
        self._second_name = second_name
        self._paternal_last_name = paternal_last_name
        self._maternal_last_name = maternal_last_name

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

    def __str__(self):
        return self._first_name + " " + self._second_name + " " + self._paternal_last_name + " " + \
               self._maternal_last_name
