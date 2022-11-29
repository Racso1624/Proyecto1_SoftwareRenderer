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

background = Texture('./background.bmp')

r.setBackground(background.pixels)

lamp_texture = Texture('./desk_lamp.bmp')

cup_texture = Texture('./cup.bmp')

book_texture = Texture('./book.bmp')


#Modelos con Texturas
r.loadModel('./desk_lamp.obj', translate=[470, 550, 0], scale=[650, 650, 650], rotate=(-pi/3, 0, -pi/2), texture=lamp_texture)

r.loadModel('./book.obj', translate=[535, 250, 0], scale=[10, 10, 10], rotate=(0, -pi/2, -pi/2), texture=book_texture)

r.loadModel('./cup.obj', translate=[470, 712, 0], scale=[7, 7, 7], rotate=(0, 0, -pi/2), texture=cup_texture)

#Modelos con Shaders
r.setShader(dragon_shader)
r.loadModel('./mask.obj', translate=[770, 712, 0], scale=[150, 150, 150], rotate=(0, 0, -pi/2))

r.setShader(sharpener_shader)
r.loadModel('./sharpener.obj', translate=[1100, 850, 0], scale=[900, 900, 900], rotate=(0, 0, -pi/2))

r.setShader(glasses_shader)
r.loadModel('./glasses.obj', translate=[470, 450, 0], scale=[600, 600, 600], rotate=(-pi/3, 0, -pi/2))

r.setShader(table_shader)
r.loadModel('./desk.obj', translate=[30, 540, 0], scale=[0.6, 0.6, 0.6], rotate=(0, 0, -pi/2))

r.glFinish("Proyecto_1.bmp")