import pygame
import sys
import math
from vector import Vector
from sphere import Sphere
from box import Box
from floor import Floor
from materials import Material
from readfile import ReadObjects
from config import Config
from cylinder import XCylinder, YCylinder, ZCylinder

class RayTracer:

    def __init__(self, LIGHTDIR, objects, materials, config):
        self.objects = objects
        self.materials = materials
        self.config = config
        self.FOVANGLE = 70
        self.ZSCREEN = -((self.config.ScreenWidth/2) / math.tan(math.radians(self.FOVANGLE/2)))
        self.LIGHTDIR = LIGHTDIR
        self.LIGHTAMBIENT = 0.5 #0-1
        self.LIGHTSPECULAR = 50


    #background lighting in the scene
    def lighting(self, normal):
        cosAngle = self.LIGHTDIR.dot(normal)
        diffuse = 1 - self.LIGHTAMBIENT #diffuse light + ambient light has to equal 1
        light = (max(0, cosAngle) * diffuse) + self.LIGHTAMBIENT
        return light

    #specular lighting
    def lightingSpecular(self, normal, rayDir):
        rayReflect = reflectRay(rayDir, normal)
        cosAngle = self.LIGHTDIR.dot(rayReflect)
        light = max(0, cosAngle) ** self.LIGHTSPECULAR
        return light

    #fires rays at each object to see which object is hit first
    def rayFire(self, rayStart, rayDir):
        material = ""
        result = None
        
        for obj in self.objects:
            objRes = obj.rayHits(rayStart, rayDir)
            if objRes is not None and (result is None or result[0] > objRes[0]):
                result = objRes
                material = obj.material
        return result, material

    #traces the shadow of each object after ray intersects it
    def rayShadow(self, rayStart):
        start = rayStart.add(self.LIGHTDIR.mul(0.0001))
        for obj in self.objects:
            objRes = obj.rayHits(start, self.LIGHTDIR)
            if objRes is not None:
                return True
        return False    

    def rayTrace(self, rayStart, rayDir, depth):
        
        if depth > 5:
            return Vector(0, 0, 0)

        result, material = self.rayFire(rayStart, rayDir)

        
        reflective = 0
        if result is None:
            return self.config.SkyColour #background colour
        else:
            distance, position, normal = result
            if material == "floor": #maps floor pattern
                tile_x = math.floor(position.x)
                tile_z = math.floor(position.z)
                tile = (tile_x + tile_z) % 2 #if no remainder then floor material 1
                
                if tile == 0:
                    material = 'floor1'
                else:
                    material = 'floor2'


            reflective = self.materials[material].reflective
            colour = self.materials[material].colour
                
            if self.rayShadow(position):
                colour = colour.mul(self.LIGHTAMBIENT)
            else:
                light = self.lighting(normal)
                colour = colour.mul(light)
                colour = colour.add(Vector(1, 1, 1).mul(self.lightingSpecular(normal, rayDir)))
                
            if reflective > 0:
                rayReflect = reflectRay(rayDir, normal)
                reflectedColour = self.rayTrace(position.add(rayReflect.mul(0.0001)), rayReflect, depth+1)
                colour = interpolateVectors(colour, reflectedColour, reflective)
            return colour.clamp()

#reflects ray when hits object
def reflectRay(rayDir, normal):
    return rayDir.sub(normal.mul(rayDir.dot(normal) * 2))

#estimating colour values between the 2 known values to give final value of pixel
def interpolateVectors(vec0, vec1, factor):
    if factor <= 0:
        return vec0
    elif factor >= 1:
        return vec1
    else:
        return (vec1.mul(factor)).add(vec0.mul(1-factor))
