import appdaemon.plugins.hass.hassapi as hass
import random

class inKellerIntent(hass.Hass):

    def initialize(self):
        return

    def getIntentResponse(self, slots, devicename):
        if self.get_state("sensor.kellertime") == "ja":
            if slots["person"] in self.args["persons"]:
                idnr = self.args["persons"][slots["person"]]
                runtime = datetime.datetime.now().strftime("%d-%m-%Y")
                try:
                    log = open(self.args["datafile"], 'a')
                    log.write(runtime + ";  " + str(idnr) + "\n")
                    log.close()
                except:
                   self.log("AANWEZIGHEIDSFILE CANT BE WRITTEN!!")
                text = "<p>Hi, {{person}}.</p><p>Schoen das du wieder da bist</p>"
            else:
                runtime = datetime.datetime.now().strftime("%d-%m-%Y")
                try:
                    log = open(self.args["newdatafile"], 'a')
                    log.write(runtime + ";  " + slots["person"] + "\n")
                    log.close()
                except:
                   self.log("AANWEZIGHEIDSFILE CANT BE WRITTEN!!")
                text = "<p>Hallo, {{person}}.</p><p>Leider habe ich noch kein registratie nummer, aber dass mach renee bestimmt in ordnung.</p>"

        else:
            text = "<p>Hi, {{person}}.</p><p>Schoen das du Olinde und renee besucht</p>" 
        return text
        