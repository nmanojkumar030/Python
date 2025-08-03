class Connections:
    class __OnlyOnce:
        """Private Class"""

        def __init__(self, temp_id):
            self.temp_id = temp_id

        def __str__(self):
            return "{} id = {}".format(repr(self), self.temp_id)

    instance = dict()

    def __new__(cls, conn_id):
        if conn_id not in cls.instance:
            cls.instance[conn_id] = cls.__OnlyOnce(conn_id)

        return cls.instance


if __name__ == '__main__':
    c = Connections(1010)
    print(c)

    c1 = Connections(1011)
    print(c1)

    c2 = Connections(1011)
    print(c2)
