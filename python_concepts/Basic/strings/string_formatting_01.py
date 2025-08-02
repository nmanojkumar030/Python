"""Format String"""
# {:fmt-str}

from math import pi


def compute(radius):
    """ Function Definition"""
    return pi * radius ** 2


try:
    user_radius = float(input('enter the radius :'))
    area = compute(user_radius)
    print('Radius : {}\nArea of circle : {:.3f}'.format(user_radius, area))
except ValueError as err:
    print(err)
