import math

class Vector:
#A three element vector used in 3D graphics for multiple purposes

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def str(self): #vector in string form
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def dot(self, other): #dot product of vector
        return self.x * other.x + self.y * other.y + self.z * other.z

    def magnitude(self): #size of vector (pythagoras)
        return math.sqrt(self.dot(self))

    def clamp(self):
        return Vector(max(0, min(1, self.x)), max(0, min(1, self.y)), max(0, min(1, self.z)))

    def normalize(self): #unit vector of self
        return self.div(self.magnitude())

    def add(self, other): #add a vector to another
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def sub(self, other): #subtract a vector from another
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def mul(self, other): #multiply a vector by a scalar
        assert not isinstance(other, Vector)
        return Vector(self.x * other, self.y * other, self.z * other)

    def div(self, other): #divide a vector by a scalar
        assert not isinstance(other, Vector)
        return Vector(self.x / other, self.y / other, self.z / other)
