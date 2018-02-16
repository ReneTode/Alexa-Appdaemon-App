import appdaemon.plugins.hass.hassapi as hass
import random

class whatDoesSomeoneIntent(hass.Hass):

    def initialize(self):
        return

    def getIntentResponse(self, slots, devicename):
        try:
            ############################################
            # get the state from a sensor and if its true
            # get the text for the person
            # when false check if person is part of household
            # and give text for household person or error text
            ############################################
            entityState = self.get_state(self.args["entityID"])
            if entityState == self.get_state(self.args["entityState"]):
                if slots["person"] in self.args["event_" + entityState]: 
                    text = self.random_arg(self.args["event_" + entityState][slots["person"]])
            else:
                if slots["person"] in self.args["household"]:
                    text = self.random_arg(self.args["event_" + entityState]["Household"])
                else:
                    text = self.random_arg(self.args["event_" + entityState]["notHousehold"])
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
