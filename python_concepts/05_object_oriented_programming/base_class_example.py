"""Base Class"""


class Person:

    def __init__(self, fn, ln):
        self.fn = fn
        self.ln = ln

    def get_info(self):
        print("First Name:", self.fn)
        print("Last Name:", self.ln)


if __name__ == "__main__":
    p = Person("Manoj", "Kumar")
    p.get_info()
