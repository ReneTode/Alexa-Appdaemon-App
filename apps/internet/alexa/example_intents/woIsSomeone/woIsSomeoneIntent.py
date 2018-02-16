import appdaemon.plugins.hass.hassapi as hass
import random

class woIsSomeoneIntent(hass.Hass):

    def initialize(self):
        return

    def getIntentResponse(self, slots, devicename):
        try:
            ############################################
            # an example Intent to show how you can change text
            # based on sensor states or time
            ############################################
            if self.slots["person"] in self.args["household"]:
                ############################################
                # decide if a person is guest or not
                ############################################
                if self.get_state("sensor." + self.slots["person"]) == "In bed":
                    ############################################
                    # assumes that there are sensors for every person 
                    # with a state if thet are in Bed
                    ############################################
                    text = self.random_arg(self.args["inBed"])
                elif self.get_state("sensor.kellertime") == "ja":
                    ############################################
                    # assumes that there is a sensor thats set to "ja"
                    # for a certain event
                    ############################################
                    text = self.random_arg(self.args["kellerTime"])
                elif self.now_is_between("18:00:00","18:30:00"):
                    ############################################
                    # at dinertime give another text
                    ############################################
                    text = self.random_arg(self.args["diner"])
                elif self.slots["person"] == "olinde":
                    if self.now_is_between("16:00:00","17:30:00"):
                        ############################################
                        # text for a certain person at a certain time
                        ############################################
                        text = self.random_arg(self.args["Olinde"]["couch"])
                    elif self.now_is_between("17:30:00","18:00:00"):
                        ############################################
                        # text for a certain person at a certain time
                        ############################################
                        text = self.random_arg(self.args["Olinde"]["cooking"])
                    else:
                        text = self.random_arg(self.args["Olinde"]["somethingElse"])
                elif self.slots["person"] == "rene":
                    if self.now_is_between("19:00:00","20:00:00"):
                        ############################################
                        # text for a certain person at a certain time
                        ############################################
                        text = self.random_arg(self.args["Rene"]["couch"])
                    else:
                        text = self.random_arg(self.args["Rene"]["somethingElse"])
                else:
                    text = self.random_arg(self.args["Other"]["somethingElse"])
            else:
                text = self.random_arg(self.args["Other"]["somethingElse"])
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
