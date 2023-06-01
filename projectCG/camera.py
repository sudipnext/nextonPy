# pyglm is a wrapper for the glm(opengl mathematics) module written in c++. glm has a lot of possible use cases including 3d graphics(physics, direct-X)etc
import glm
#to use key movements we use pygame module
import pygame as pg

FOV = 50  # it's in degree
NEAR = 0.1
FAR = 100
#defining the movement speed of the camera
SPEED = 0.01
#for mouse movement we need to specify the sensitivity
SENSITIVITY = 0.05
# we need to update the value of yaw, pitch and roll of the camera inorder to move this
class Camera:
    def __init__(self, app, position=(0, 0, -8), yaw=90, pitch=0):
        self.app = app
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        # moving camera
        self.position = glm.vec3(position)
        self.up = glm.vec3(0, 1, 0)
        #let's define camera coordinates it's for Y axis i.e 0, 1, 0 for X-Axis 1,0,0 and for z 0, 0, -1 for negative z axis
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0,0,-1)
        #now adding mouse sensitivity as we move the camera with the mouse
        self.yaw = yaw
        self.pitch = pitch
        # viewing matrix
        self.m_view = self.get_view_matrix()
        # projection matrix
        self.m_proj = self.get_projection_matrix()
    
    #here we define the rotate movement as
    def rotate(self):
        rel_x, rel_y = pg.mouse.get_rel()
        #calculating the new value of yaw and pitch and limiting the pitch so that there is no unnatural up and down
        self.yaw += rel_x * SENSITIVITY
        self.pitch -=rel_y * SENSITIVITY
        self.pitch = max(-89, min(89, self.pitch))
    #now we need a method for recalcuating the vectors
    def update_camera_vectors(self):
        yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)
        #by using basic trignometry we can findout the axis respectively
        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)     

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def update(self):
        self.move()
        self.rotate()
        self.update_camera_vectors()
        #since the camera is changed we need to recalculate the view matrix
        self.m_view = self.get_view_matrix()
    #defining movement for camera
    def move(self):
        velocity = SPEED * self.app.delta_time
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.position += self.forward *velocity
        if keys[pg.K_s]:
            self.position -= self.forward * velocity
        if keys[pg.K_a]:
            self.position += self.right *velocity
        if keys[pg.K_d]:
            self.position -= self.right * velocity
        if keys[pg.K_q]:
            self.position += self.up *velocity
        if keys[pg.K_e]:
            self.position -= self.up * velocity

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position+self.forward, self.up)

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)
