import appdaemon.plugins.hass.hassapi as hass
import random

class showYoutubeIntent(hass.Hass):

    def initialize(self):
        return

    def getIntentResponse(self, slots, devicename):
        ############################################
        # show 1 of the 6 videos from the last youtube search
        ############################################
        self.log(self.args["YoutubeVideoList"][(int(slots["videonr"])-1)])
        try:
            self.dash_navigate(self.args["YoutubeVideoList"][(int(slots["videonr"])-1)], self.args["VideoShowTime"])
            text = self.random_arg(self.args["normalResponse"])
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
