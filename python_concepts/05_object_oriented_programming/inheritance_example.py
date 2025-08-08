from base_class_example import Person

"""Derived Class 
Employee extends Person"""


class Employee(Person):

    # pass
    def __init__(self, eid, fn, ln):
        self.eid = eid
        super().__init__(fn, ln)

    def get_info(self):
        print("employee id :", self.eid)
        super().get_info()  # Invoke overriden method


if __name__ == "__main__":
    # e = Employee("Guido", "rossum")
    e = Employee(1, "Guido", "rossum")
    e.get_info()
