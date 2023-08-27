import math
from vector import Vector

class Sphere:
#3D shape with radius, centre and material

    def __init__(self, centre, radius, material):
        self.centre = centre #centre of sphere
        self.radius = radius #radius of sphere
        self.material = material #material made of

    def rayHits(self, rayStart, rayDir):
        #checks if the ray intersects the sphere and returns the distance to
        #intersection and the position of intersection
        
        point_to_centre = (self.centre).sub(rayStart)
        a = point_to_centre.dot(rayDir) #length of the ray direction to be perpendicular to b (radius perp to chord made between 2 points)
        b_sq = (point_to_centre.magnitude()*point_to_centre.magnitude()) - (a*a)
        
        if b_sq > (self.radius*self.radius):
            return None
        
        else:
            q = math.sqrt((self.radius*self.radius)-b_sq)
            if a - q > 0:
                distance = a - q #distance to 1st hit but elif if this is behind screen
            elif a + q > 0:
                distance = a + q #distance to 2nd hit
            else:
                return None
            
            pos = rayStart.add(rayDir.mul(distance)) #position where hits circle
            norm = (pos.sub(self.centre)).normalize() #normal from surface of sphere at pos
            return distance, pos, norm
