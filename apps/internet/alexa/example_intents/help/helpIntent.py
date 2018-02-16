import appdaemon.plugins.hass.hassapi as hass
import random

class helpIntent(hass.Hass):

    def initialize(self):
        return

    def getIntentResponse(self, slots, devicename):
        ############################################
        # help is asked, give a list
        ############################################
        try:
            text = self.random_arg(self.args["Start"])
            for helpitem in self.args["List"]:
                text = text + helpitem
        except:
            text = self.args["Error"]
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
