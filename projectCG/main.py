#Creating my own 3d engine using opengl
#importing necessary things
import pygame as pg
import moderngl as mgl
import sys
#now importing the triangle model
from model import *
from camera import Camera

#creating a graphics engine class
class GraphicsEngine:
    def __init__(self, win_size=(1600, 900)):
        pg.init()
        #window size
        self.WIN_SIZE = win_size
        #setting opengl attributes
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        #Deprecated functionality is functionality that is marked for removal in a future release.
        #The following code ensures that the deprecated functionality is not used
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        #creating opengl context
        #double buffering provides two complete color buffers for use in drawing. one buffer is displayed while the other buffer is being drawn into. when the drawing is complete, the two buffers are swapped so that the one that was being viewed is now used for drawing.
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        #now we need to detect this using opengl module
        self.ctx = mgl.create_context()
        #creating an object to help track the time
        self.clock = pg.time.Clock()
        #now creating an instance of the method and calling it
        self.scene = Cube(self)

    #listening for key presses
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type==pg.KEYDOWN and event.key == pg.K_ESCAPE):
                #added from traingle model
                self.scene.destroy()
                ##
                pg.quit()
                sys.exit()

    #lets write the render method
    #the color is specified in normalized form 0... 255-> 0.0 ..
    def render(self):
        #clearing frame buffer
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        #rendering scene traingle model
        self.scene.render()

        #swapping buffers
        pg.display.flip()
    #to start our application    
    def run(self):
        while True:
            self.check_events()
            self.render()
            #setting the frame rate to 60 seconds
            self.clock.tick(60)
#creating an instance and running the program

if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()

