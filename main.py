#Oscar Fernando López Barrios
#Carné 20679
#Gráficas Por Computadora
#Proyecto 1

from gl import Render
from texture import *
from math import *
from vector import *
from shaders import *

r = Render()

r.glCreateWindow(1024, 1024)

r.glClearColor(0.5, 0.6, 0.8)

r.glColor(0, 0, 0)

r.glClear()

r.lookAt(V3(0, 0, 10), V3(0, 0, 0), V3(0, 1, 0))

# background = Texture('./background.bmp')

# r.setBackground(background.pixels)

lamp_texture = Texture('./desk_lamp.bmp')

cup_texture = Texture('./cup.bmp')

r.loadModel('./desk_lamp.obj', translate=[612, 512, 0], scale=[500, 500, 500], rotate=(-pi/3, 0, -pi/2), texture=lamp_texture)

r.loadModel('./book.obj', translate=[612, 112, 0], scale=[500, 500, 500], rotate=(-pi/3, -pi/2, -pi/2))

r.loadModel('./cup.obj', translate=[612, 712, 0], scale=[10, 10, 10], rotate=(0, 0, -pi/2), texture=cup_texture)

r.loadModel('./sharpener.obj', translate=[912, 712, 0], scale=[500, 500, 500], rotate=(0, 0, -pi/2))

r.setShader(glasses_shader)
r.loadModel('./glasses.obj', translate=[612, 312, 0], scale=[500, 500, 500], rotate=(0, 0, -pi/2))

r.setShader(table_shader)
r.loadModel('./desk.obj', translate=[112, 512, 0], scale=[0.5, 0.5, 0.5], rotate=(0, -pi/6, -pi/2))

r.glFinish("Proyecto_1.bmp")