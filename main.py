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
from raytracer import RayTracer

#other people make me object lists FEEDBACK
#cylinder if not hit infinite then no finite either
#if infinitecyl.z pos are not in finitecyl.z
#if the 2 z are between ztop and zbottom then hit finite
#texture mapping objects
#refraction
#more light rays for each pixel
#signed to distance function, fog

def main():
    pygame.init()
    
    objects, materials, config = ReadObjects("ball of balls.txt")
    ##INSERT NAME OF TEXT FILE IN LINE ABOVE ReadObjects("nameoffile.txt")
    
    screen = pygame.display.set_mode(config.ScreenSize)
    LIGHTDIR = (config.LightDir).normalize()  #unit vector for direction of light

    ray_tracer = RayTracer(LIGHTDIR, objects, materials, config)
    
    gameState = "running"
    ##while gameState != "exit":
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameState = "exit"

    angle = math.radians(config.CamAngle) #calculations so the angles only need to be calculated once
    cosAngle = math.cos(angle)
    sinAngle = math.sin(angle)

    for row in range(config.ScreenHeight):
        for col in range(config.ScreenWidth):
            
            x = col - (config.ScreenWidth/2)
            y = -(row - (config.ScreenHeight/2))

            #converting the pixel coordinate on screen to a ray
            rayDir = Vector(x, y, ray_tracer.ZSCREEN).normalize()
            
            x = rayDir.x
            z = rayDir.z
            #rotation of camera
            rayDir.x = (cosAngle * x) - (sinAngle * z)
            rayDir.z = (sinAngle * x) + (cosAngle * z)
            
            colour = ray_tracer.rayTrace(config.CamPos, rayDir, 0)
            red = round(colour.x * 255) #multiplies the vector for colour by 255 and rounds to 0dp
            green = round(colour.y * 255)
            blue = round(colour.z * 255)
            
            screen.set_at((col, row), (red, green, blue, 255)) #sets each pixel to the calculated colour
        pygame.display.flip()
        
    renderTime = round(pygame.time.get_ticks() / 1000, 1) #time since pygame.init() was called
    print("Render time:", renderTime, " seconds.")


if __name__ == "__main__":
    main()

##pygame.quit()

