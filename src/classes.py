class Person:
    @staticmethod
    def get_class_name():
        return "Person"

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello {self.name}")


if __name__ == "__main__":

    class Male(Person):
        def __init__(self, name):
            super().__init__(name)

    print(Person.get_class_name())
    male = Male(name="Niraj")
    male.greet()
