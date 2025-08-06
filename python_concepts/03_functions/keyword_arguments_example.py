"""Keyword Arguments Parameter"""


def tuner(**kwargs):
    print(kwargs)
    # kwargs is a dictionary containing all keyword arguments
    # You can access them like a normal dictionary
    # For example, to print each key-value pair
    for key, value in kwargs.items():
        print(f"{key} = {value}")


tuner()
tuner(contrast=0.89, brightness=0.98, hue=0.75)

param = dict(contrast=0.89, brightness=0.98, hue=0.75)
tuner(**param)
