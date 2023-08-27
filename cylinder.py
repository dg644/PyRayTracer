from vector import Vector
import math

class XCylinder:
    """Cylinder laying on x axis"""

    
class YCylinder:
    """Cylinder laying on y axis"""
    

class ZCylinder:
    """Cylinder laying on z axis"""

    def __init__(self, centre, radius, material):
        self.centre = centre
        self.radius = radius
        self.material = material

    def rayHits(self, rayStart, rayDir):
        PC = self.centre.sub(rayStart)
        PC.z = 0
        D = rayDir.mul(1.0)
        D.z = 0
        Dmag = D.magnitude()
        if Dmag == 0:
            return None
        a = (PC.dot(D))/Dmag
        b_sq = (PC.magnitude()*PC.magnitude()) - (a*a)
        if b_sq > (self.radius*self.radius):
            return None
        else:
            e = math.sqrt((self.radius*self.radius)-b_sq)
            if a - e > 0:
                t = (a - e) / Dmag
            elif a + e > 0:
                t = (a + e) / Dmag
            else:
                return None
            pos = rayStart.add(rayDir.mul(t))
            norm = pos.sub(self.centre)
            norm.z = 0
            norm = (norm).normalize()
            return t, pos, norm

