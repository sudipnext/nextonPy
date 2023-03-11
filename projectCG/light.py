import glm

# ambient+diffuse - specular = phong


class Light:
    def __init__(self, position=(3,  3, -3), color=(1, 1, 1)):
        self.position = glm.vec3(position)
        self.color = glm.vec3(color)
        # intensity of the color
        # for ambient
        self.Ia = 0.1 * self.color
    
        # for diffuse
        self.Id = 0.8 * self.color
        # for specular
        self.Is = 1.0 * self.color
