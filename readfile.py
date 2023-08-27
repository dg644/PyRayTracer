from vector import Vector
from sphere import Sphere
from box import Box
from floor import Floor
from materials import Material
from config import Config

STRIPCHARS = ", \n\r\t"

def readObject(line):
    if ':' in line:
        x = line.find(':')
        return line[:x], line[x+1:]


    
#The input string is expected to start with three numbers enclosed in square
#brackets and separated by commas, followed by a comma or the end of the string.
#Any spaces before or after the numbers or the square brackets are ignored.
def readVector(line):
    if '[' in line and ']' in line:
        x = line.find('[') + 1
        y = line.find(']')
        
        vector = (line[x:y]).split(',')
        other = line[y+1:].strip(STRIPCHARS)
        
        numberx = float((vector[0].replace(',', '')).strip(STRIPCHARS))
        numbery = float((vector[1].replace(',', '')).strip(STRIPCHARS))
        numberz = float((vector[2].replace(',', '')).strip(STRIPCHARS))
        
        return Vector(numberx, numbery, numberz), other
    else:
        return line, None

    
        
#The input string is expected to start with a number followed by a comma or
#the end of the string.  Any spaces before or after the number are ignored.
#The function returns the number that was read and the remaining part of
#the input string afterthe comma (if any)
def readNumber(line):
    if ',' in line:
        x = line.find(',')
        val = line[:x].strip(STRIPCHARS)
        number = float(val)
        rest = (line[x+1:]).strip(STRIPCHARS)
        return number, rest
    else:
        return float(line), ""



#Start with a string in speech marks and followed by a comma or the end of the line.
#Any spaces before and after the name are ignored and the function returns the
#name inside the speech marks.
def readName(line):
    if "," in line:
        x = line.find(",")
        val = line[:x].strip("'" + STRIPCHARS)
        material = val
        rest = (line[x+1:]).strip(STRIPCHARS)
        return material, rest
    else:
        line = line.strip("'" + STRIPCHARS)
        return line, ""




def ReadObjects(filename):

    objects = []
    materials = {}
    config = Config(0, 0, 0, 0, 0, 0, 0)

    with open(filename, "r") as f: #opens file to read
        for line in f:
            if ':' in line:
                objtype, other = readObject(line)
                
                if objtype.lower() == "sphere": #read sphere shape from file
                    centre, other = readVector(other)
                    radius, other = readNumber(other)
                    material, other = readName(other)
                    sphere = Sphere(centre, radius, material)
                    objects.append(sphere)
                    
                elif objtype.lower() == "box": #read box shape from file
                    centre, other = readVector(other)
                    edgelength, other = readVector(other)
                    material, other = readName(other)
                    box = Box(centre, edgelength, material)
                    objects.append(box)
                    
                elif objtype.lower() == "floor": #read floor object from file
                    floorheight, other = readNumber(other)
                    material, other = readName(other)
                    floor = Floor(floorheight, material)
                    objects.append(floor)
                    
                elif objtype.lower() == "material": #read material from file
                    colourname, other = readName(other)
                    reflective, other = readNumber(other)
                    colourrgb, other = readVector(other)
                    materials[colourname] = Material(reflective, colourrgb)
                    
                elif objtype.lower() == "campos": #sky camera position
                    position, other = readVector(other)
                    config.CamPos = position
                elif objtype.lower() == "lightdir": #sky light direction
                    direction, other = readVector(other)
                    config.LightDir = direction
                    
                elif objtype.lower() == "screensize": #sky screen size
                    width, other = readNumber(other)
                    height, other = readNumber(other)
                    config.ScreenSize = (int(width), int(height))
                    config.ScreenWidth = int(width)
                    config.ScreenHeight = int(height)
                    
                elif objtype.lower() == "skycolour": #read sky colour
                    colour, other = readVector(other)
                    config.SkyColour = colour
                elif objtype.lower() == "camangle": #camera angle from y axis
                    angle, other = readNumber(other)
                    config.CamAngle = angle

                    


    return objects, materials, config
    #returns the objects list, materials dictionary and config class
