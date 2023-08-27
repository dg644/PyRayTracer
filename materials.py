from vector import Vector

class Material():
    #material has reflective value (0-1) and a colour (rgb vector)

    def __init__(self, reflective, colour):
        self.reflective = reflective #0 not reflective, 1 very reflective
        self.colour = colour #colour as Vector(R, G, B)
