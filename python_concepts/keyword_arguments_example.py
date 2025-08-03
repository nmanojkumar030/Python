""" Keyword Arguments Parameter"""


def tuner(**kwargs):
    print(kwargs)


tuner()
tuner(contrast=.89, brightness=0.98, hue=.75)

param = dict(contrast=.89, brightness=0.98, hue=.75)
tuner(**param)
