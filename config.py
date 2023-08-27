from vector import Vector

class Config:
#configuration class for the scene

    def __init__(self, CamPos, CamAngle, LightDir, ScreenSize, ScreenWidth, ScreenHeight, SkyColour):
        self.CamPos = CamPos #camera position
        self.CamAngle = CamAngle #camera angle, rotated about y axis
        self.LightDir = LightDir #light direction
        self.ScreenSize = ScreenSize #width, height
        self.ScreenWidth = ScreenWidth
        self.ScreenHeight = ScreenHeight
        self.SkyColour = SkyColour

