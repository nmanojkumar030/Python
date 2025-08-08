"""
Implementing Custom Exception
"""


class TooManyConnectionError(Exception):
    # toString method
    def __str__(self):
        return "{} : {}".format(self.__class__.__name__, self.args[0])


class Connections:
    # Class Variables
    counter = 0
    max_connections = 5

    # initializer
    def __init__(self, connection_id):
        Connections.counter += 1
        self.connection_id = connection_id  # Instance variables
        Connections.check4limits()

    # Class method
    @classmethod  # here @ is called decorators
    def check4limits(cls):
        if cls.counter > cls.max_connections:
            raise TooManyConnectionError("Too many concurrent connections")

    def __str__(self):
        return "[{} connection id = {}]".format(
            self.__class__.__name__, self.connection_id
        )


# Main method
if __name__ == "__main__":
    try:
        list_of_connection = list()
        for item in range(1, 7):
            list_of_connection.append(Connections(item))
    except TooManyConnectionError as err:
        print(err)

    for item in list_of_connection:
        print(item)
