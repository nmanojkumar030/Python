"""Custom Exception"""


class TooManyConnectionError(Exception):
    def __str__(self):
        return "{} : {}".format(self.__class__.__name__, self.args[0])


class Connections:
    counter = 0  # Class Variables
    max_connections = 5

    def __init__(self, connection_id):
        Connections.counter += 1
        self.connection_id = connection_id  # Instance variables
        Connections.check4limits()

    @classmethod  # here @ is called decorators
    def check4limits(cls):
        """Class method"""

        if cls.counter > cls.max_connections:
            raise TooManyConnectionError("Too many concurrent connections")

    def __str__(self):
        return "[{} connection id = {}]".format(self.__class__.__name__, self.connection_id)


if __name__ == '__main__':
    try:
        list_of_connection = list()
        for item in range(1, 7):
            list_of_connection.append(Connections(item))
    except TooManyConnectionError as err:
        print(err)

    for item in list_of_connection:
        print(item)
