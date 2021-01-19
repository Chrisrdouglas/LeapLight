from LightController import LightController
from ControllerListener import ControllerListener
import sys
import json
import Leap



def main():
    #get config from json
    with open('config.json') as json_file:
        data = json.load(json_file)

        #set up listener
    listener = ControllerListener()
    lc = LightController(data['mac'], data['ip'])
    listener.assignLightController(lc)

    #get controller
    controller = Leap.Controller()
    controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
    controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)

    controller.add_listener(listener) #attach listener

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()