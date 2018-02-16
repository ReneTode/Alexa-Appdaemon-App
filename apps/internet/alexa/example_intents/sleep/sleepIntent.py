import appdaemon.plugins.hass.hassapi as hass
import random

class sleepIntent(hass.Hass):

    def initialize(self):
        return

    def getIntentResponse(self, slots, devicename):
        ############################################
        # if a switch is on give some text, if its off another
        ############################################
        return self.random_arg(self.args[self.get_state(self.args["switch"])])

    def random_arg(self,argName):
        ############################################
        # pick a random text from a list
        ############################################
        if isinstance(argName,list):
            text = random.choice(argName)
        else:
            text = argname
        return text

