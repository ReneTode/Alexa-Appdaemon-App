import appdaemon.plugins.hass.hassapi as hass
import random

class setBedOlindeOffIntent(hass.Hass):

    def initialize(self):
        return

    def getIntentResponse(self, slots, devicename):
        ############################################
        # turn a switch off (you could change that for off or toggle)
        # sometimes its more user friendly to have 2 Intents for 1 task
        ############################################
        self.turn_off(self.args["switch"])
        return self.random_arg(self.args["switchedText"])

    def random_arg(self,argName):
        ############################################
        # pick a random text from a list
        ############################################
        if isinstance(argName,list):
            text = random.choice(argName)
        else:
            text = argname
        return text
