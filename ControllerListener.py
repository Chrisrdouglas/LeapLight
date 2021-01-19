import Leap
from LightController import LightController
import time

class ControllerListener(Leap.Listener):

    def assignLightController(self, light):
        self.light = light
        self.prevTime = 0

    def on_disconnect(self, controller):
        exit(1)

    def on_connect(self, controller):
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
        controller.add_listener(self)
        print("connected")

    def on_disconnect(self, controller):
        print("disconnected")

    def on_frame(self, controller):
        currentTime = round(time.time() * 1000)
        if currentTime - self.prevTime < 1000:
            #self.prevTime = currentTime
            return

        for gesture in controller.frame().gestures():
            if gesture.type is Leap.Gesture.TYPE_SWIPE:
                #swipe to change color
                self.light.shiftColor()
                self.prevTime = currentTime
                print("swipe")
                return
            elif gesture.type is Leap.Gesture.TYPE_KEY_TAP:
                #tap to turn on
                self.light.togglePower()
                self.prevTime = currentTime
                print("tap")
                return



