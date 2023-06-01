# importing necessary libraries i.e camera, light, mesh and scene
import sys
import pygame
from pygame.locals import *
from constants import *
from event import HandleEvent
from utils.vector import Vector3
from utils.camera import Camera
from utils.light import Light
from utils.mesh.base import Mesh
from utils.mesh.meshes import *
from utils.mesh.spheres import *
from utils.mesh.point import *
from utils.matrix import *
from utils.tools import *
from utils.world import Scene

pygame.init()
# screen = pygame.display.set_mode(Size)
flags = DOUBLEBUF
screen = pygame.display.set_mode(Size, flags, 16)
clock = pygame.time.Clock()
fps = 60
#mouse setup
pygame.mouse.get_rel()
pygame.mouse.set_visible(True)
a = pygame.event.set_grab(False)

#creating mesh

Car = Mesh()
# first parameter for the obj file and second one for the color in RGB
Car.triangles = LoadMesh("../assets/temple.obj", (255, 0, 0))

# create scene and the world
# creating a scene  
scene = Scene()
#adding object you want to display into the world
scene.world.append(Car)

#camera setup
camera = Camera(Vector3(0, 0, 0), 0.1, 1000.0, 75.0)
camera.speed = 0.5
camera.rotationSpeed = 0.8

#light setup
light = Light(Vector3(0.9, 0.9, -1))
hue = 0.5

angle = 0
moveLight = True
run = True

while run:
    screen.fill(BackgroundColor)
    clock.tick(fps)
    dt = clock.tick(fps)/100
    frameRate = clock.get_fps()
    pygame.display.set_caption(str(frameRate) + " fps")
    run = HandleEvent(camera, dt)
    hue = 0
    # handle input
    camera.HandleInput(dt)

    if moveLight == True and light != None:
        mx, my = pygame.mouse.get_pos()
        _x = translateValue( mx, 0,  Width,  -1,  1)
        _y = translateValue( my, 0, Height, -1, 1)
        light = Light(Vector3(-_x, -_y, -1))

    # apply the transformation matrix here
    Car.transform = Matrix.rotation_y(angle) @ Matrix.scaling(1.9)


    # display scene
    scene.update(
        dt = dt,
        camera=camera,
        light=light,
        screen=screen,
        showAxis=True,
        fill=True,
        wireframe=False,
        vertices=True,
        depth=True,
        clippingDebug=False,
        showNormals=False,
        radius=1,
        verticeColor=False,
        wireframeColor=(255, 255, 255),
        ChangingColor=hue)


    pygame.display.flip()
    angle += 0.01

pygame.quit()
sys.exit()
