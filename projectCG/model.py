#The process of opengl rendering pipeling goes like this 
#It first accepts the vertices and pass it into the vertex shader then to primitive assembly and then comes rasterization where the primitives are divided into fragments and then a fragment shader is launched for each fragments After various tests then it finally outputs to framebuffer, To get as expected results the fragment shader and the vertex shader is connected with uniforms variables
import moderngl as mgl
import numpy as np

class Cube:
    def __init__(self, app):
        self.app=app
        self.ctx=app.ctx
        self.vbo = self.get_vbo()
        self.shader_program = self.get_shader_program('default')
        self.vao= self.get_vao()
    #to use the render we need to call  the render on the vao
    def render(self):
        self.vao.render() 
    #now destroying it since there is no garbage collector in opengl
    def destroy(self):
        self.vbo.release()
        self.shader_program.release()
        self.vao.release()
    #now getting vertex array object i.e VAO In our case each vertex has assigned the 3 float numbers and this numbers corresponds to attribute called inposition 
    def get_vao(self):
        #3f is buffer format and in position is the attributes
        vao = self.ctx.vertex_array(self.shader_program, [(self.vbo, '3f', 'in_position')])
        return vao
    def get_vertex_data(self):
        vertices = [(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1), (-1, 1, -1), (-1, -1, -1), (1, -1, -1), (1,1,-1)]
        #in opengl the order of verticies is counterclockwise passing the indices which makes up a triangle which joins to make cube at last
        indices =[(0, 2, 3), (0, 1, 2), (1, 7, 2), (1, 6, 7), (6, 5, 4), (4, 7, 6), (3, 4, 5), (3, 5, 0), (3, 7, 4), (3, 2, 7), (0, 6, 1), (0, 5, 6)]

        vertex_data = self.get_data(vertices, indices)
        return vertex_data
    @staticmethod
    def get_data(vertices, indices):
        data=[vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')
    #when we finally have the vertices we have to send it to the gpu i.e CPU --(vertexData)-> GPU(vbo)
    def get_vbo(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo
    #The shader program is necessary to compile our shaders using cpu and they will be ready to use on gpu side
    def get_shader_program(self, shader_name):
        with open(f'shaders/{shader_name}.vert') as file:
            vertex_shader = file.read()
        with open(f'shaders/{shader_name}.frag') as file:
            fragment_shader = file.read()
        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program
