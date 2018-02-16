import appdaemon.plugins.hass.hassapi as hass
import random

class viewCameraIntent(hass.Hass):

    def initialize(self):
        return

    def getIntentResponse(self, slots, devicename):
        ############################################
        # shows 1 of your cameras listed in the yaml on the dashboard
        # expects a dashboard created for each camera
        # can also be used to show any dashboard you like on the devices where a dashboard is running
        ############################################
        try:
            if slots["location"] in self.args["CameraList"]:        
                self.dash_navigate(self.args["CameraList"][slots["location"]], self.args["CamShowTime"])
                text = self.random_arg(self.args["normalResponse"])
            else:
                text = self.random_arg(self.args["noCamResponse"])
        except:
            text = self.random_arg(self.args["Error"])
        return text

    def random_arg(self,argName):
        ############################################
        # pick a random text from a list
        ############################################
        if isinstance(argName,list):
            text = random.choice(argName)
        else:
            text = argname
        return text
