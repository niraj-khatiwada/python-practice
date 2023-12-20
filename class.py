class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def greet(self):
        print(f"Hello {self.__name}")


person = Person("Niraj")
person.greet()
print(person.name)
person.name = "King"
person.greet()
