"""Sublime or borgs singleton"""


class Cart:
    shared_state = dict()

    def __init__(self, card_id):
        self.__dict__ = Cart.shared_state
        self.cart_id = card_id

    def __str__(self):
        return "{} dict={} id ={} cart_id={}".format(self.__class__.__name__, self.__dict__, hex(id(self)),
                                                     self.cart_id)


if __name__ == '__main__':
    a = Cart(1001)
    b = Cart(1002)
    c = Cart(1003)

    b.cart_id = '1005'

    print(a)
    print(b)
    print(c)
