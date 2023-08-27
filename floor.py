from vector import Vector

class Floor:
#Object Floor is a plane with height being a y value and a material

    def __init__(self, floorHeight, material):
        self.floorHeight = floorHeight
        self.material = material


    def rayHits(self, rayStart, rayDir):
    #checks if ray intersects the plane
    #returns distance to point of intersection, position of point and normal at point
        if rayDir.y >= 0:
            return None
        else:
            distance = (rayStart.y - self.floorHeight) / (-rayDir.y)
            pos = rayStart.add(rayDir.mul(distance))
            norm = Vector(0, 1, 0)
            return distance, pos, norm
