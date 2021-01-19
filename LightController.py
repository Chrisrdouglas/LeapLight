from lifxlan import LifxLAN, Light, BLUE, CYAN, GREEN, ORANGE, PINK, PURPLE, RED, YELLOW, WHITE

class LightController:
    def __init__(self, mac = None, ip = None):
        self.bulb = None
        if mac != None and ip != None:
            self.bulb = Light(mac, ip) # put a try block in here later
        elif self.bulb == None: #put this in the catch block later
            lights = LifxLAN(1)
            self.bulb = lights.get_lights()[0]  # just get whatever light you find
        else:
            lights = LifxLAN(1)
            self.bulb = lights.get_lights()[0]
        self.color = 0
        #self.colors = [BLUE, CYAN, GREEN, ORANGE, PINK, PURPLE, RED, YELLOW, WHITE]
        self.colors = [BLUE, GREEN, RED, WHITE]

    def shiftColor(self):
        self.color = (1 + self.color) % len(self.colors)
        self.bulb.set_color(self.colors[self.color])

    def togglePower(self):
        if self.bulb.get_power() == 65535:
            self.bulb.set_power(0)
        else:
            self.bulb.set_power(65535)
