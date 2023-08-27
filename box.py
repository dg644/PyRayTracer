from vector import Vector


class Box:
#Box object with a centre, the lengths of edges and material

    def __init__(self, centre, edgeLength, material):
        self.centre = centre
        self.edgeLength = edgeLength #Vector(width, height, depth)
        self.material = material

    def rayHitsXrect(self, rayStart, rayDir, ymin, ymax, zmin, zmax, x, normalDir):
    #checks if ray intersects the side of the box
        if rayDir.x == 0:
            return None
        t = (x - rayStart.x) / rayDir.x
        if t < 0:
            return None
        pos = rayStart.add(rayDir.mul(t))
        if pos.y < ymin or pos.y > ymax or pos.z < zmin or pos.z > zmax:
            return None
        norm = Vector(normalDir, 0, 0)
        return t, pos, norm

    def rayHitsYrect(self, rayStart, rayDir, xmin, xmax, zmin, zmax, y, normalDir):
    #checks if ray intersects the side of the box
        if rayDir.y == 0:
            return None
        t = (y - rayStart.y) / rayDir.y
        if t < 0:
            return None
        pos = rayStart.add(rayDir.mul(t))
        if pos.x < xmin or pos.x > xmax or pos.z < zmin or pos.z > zmax:
            return None
        norm = Vector(0, normalDir, 0)
        return t, pos, norm

    def rayHitsZrect(self, rayStart, rayDir, xmin, xmax, ymin, ymax, z, normalDir):
    #checks if ray intersects the side of the box
        if rayDir.z == 0:
            return None
        t = (z - rayStart.z) / rayDir.z
        if t < 0:
            return None
        pos = rayStart.add(rayDir.mul(t))
        if pos.x < xmin or pos.x > xmax or pos.y < ymin or pos.y > ymax:
            return None
        norm = Vector(0, 0, normalDir) 
        return t, pos, norm

    def rayHits(self, rayStart, rayDir):
    #checks which side of box is intersected first by the ray
        Min = self.centre.sub((self.edgeLength).div(2))
        Max = self.centre.add((self.edgeLength).div(2))
        
        xRectMin = self.rayHitsXrect(rayStart, rayDir, Min.y, Max.y, Min.z, Max.z, Min.x, -1)
        xRectMax = self.rayHitsXrect(rayStart, rayDir, Min.y, Max.y, Min.z, Max.z, Max.x, +1)    
        yRectMin = self.rayHitsYrect(rayStart, rayDir, Min.x, Max.x, Min.z, Max.z, Min.y, -1)
        yRectMax = self.rayHitsYrect(rayStart, rayDir, Min.x, Max.x, Min.z, Max.z, Max.y, +1)   
        zRectMin = self.rayHitsZrect(rayStart, rayDir, Min.x, Max.x, Min.y, Max.y, Min.z, -1)
        zRectMax = self.rayHitsZrect(rayStart, rayDir, Min.x, Max.x, Min.y, Max.y, Max.z, +1)
        
        result = xRectMin
        if xRectMax is not None and (result is None or result[0] > xRectMax[0]):
            result = xRectMax
        if yRectMin is not None and (result is None or result[0] > yRectMin[0]):
            result = yRectMin
        if yRectMax is not None and (result is None or result[0] > yRectMax[0]):
            result = yRectMax
        if zRectMin is not None and (result is None or result[0] > zRectMin[0]):
            result = zRectMin
        if zRectMax is not None and (result is None or result[0] > zRectMax[0]):
            result = zRectMax
        return result

