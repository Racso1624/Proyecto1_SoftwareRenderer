#Oscar Fernando López Barrios
#Carné 20679
#Gráficas Por Computadora
#Proyecto 1

import random

def setColor(r, g, b):
    return bytes([int(b), int(g), int(r)])


def table_shader(**kwargs):

    intensity = kwargs['intensity']

    random_value = random.random()

    if (random_value <= 0.5):
        return setColor(74 * intensity, 49 * intensity, 38 * intensity)
    elif ((0.05 < random_value <= 0.3)):
        return setColor(58 * intensity, 37 * intensity, 29 * intensity)
    else:
        return setColor(161 * intensity, 117 * intensity, 81 * intensity)

def glasses_shader(**kwargs):

    intensity = kwargs['intensity']

    random_value = random.random()

    if (random_value <= 0.5):
        return setColor(232 * intensity,0 * intensity,2 * intensity)
    elif ((0.05 < random_value <= 0.3)):
        return setColor(130 * intensity,6 * intensity,8 * intensity)
    else:
        return setColor(85 * intensity,10 * intensity,9 * intensity)

def sharpener_shader(**kwargs):

    intensity = kwargs['intensity']

    return setColor(195 * intensity,120 * intensity,85 * intensity)

def dragon_shader(**kwargs):

    intensity = kwargs['intensity']

    random_value = random.random()

    if (random_value <= 0.5):
        return setColor(195 * intensity,57 * intensity,36 * intensity)
    elif ((0.05 < random_value <= 0.3)):
        return setColor(214 * intensity,121 * intensity,69 * intensity)
    else:
        return setColor(108 * intensity,32 * intensity,88 * intensity)