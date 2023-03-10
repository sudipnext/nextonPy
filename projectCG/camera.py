# pyglm is a wrapper for the glm(opengl mathematics) module written in c++. glm has a lot of possible use cases including 3d graphics(physics, direct-X)etc
import glm

FOV = 50  # it's in degree
NEAR = 0.1
FAR = 100

class Camera:
    def __init__(self, app):
        self.app = app
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        #projection matrix
        self.m_proj = self.get_projection_matrix()
    
    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)
