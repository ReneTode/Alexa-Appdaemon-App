import appdaemon.plugins.hass.hassapi as hass
import random

class goodmorningIntent(hass.Hass):

    def initialize(self):
        return

    def getIntentResponse(self, slots, devicename):
        ############################################
        # this intent sets a sensor when called, unless its already set
        # it also collects some sensor states for temperature and riverwaterlevels
        # and it looks at a last motion sensor, all that gets spoken as a report
        # because this intent is quite specific, its hard to get the text out to the yaml
        ############################################
        if slots["person"] == "rene" or slots["person"] == "":
            if self.get_state("sensor.rene") == "Thuis":
                ############################################
                # if the sensor says home this text is added
                ############################################
                starttext = "<p><say-as interpret-as='interjection'>ist nicht dein ernst</say-as>. <say-as interpret-as='interjection'>hipp hipp hurra</say-as>. <say-as interpret-as='interjection'>war nur ein scherz</say-as>. ich hatte es ihm schoen vorher gesagt.</p> <p>Aber hier bekommst du trotzdem dein information.</p>"
            else:
                ############################################
                # not home so coming out of bed set the state to home
                ############################################
                starttext = "<p>ok ich habe lindon gesagt das renee wach ist.</p>"
                self.set_state("sensor.rene", state = "Thuis")
            ############################################
            # get the river waterlevel and add to text
            ############################################
            wasserstand = str(self.get_state("sensor.waterstand_trier"))
            waterstandtext = "<p>Der wasserstand in Trier, ist im moment " + wasserstand[0] + " meter und " + wasserstand[1:] + " centimeter.</p>"
            ############################################
            # get 2 outside temperatures and add to text
            ############################################
            tempbuiten = self.floatToStr(self.get_state("sensor.vijver_repeater_7_1"))
            tempvijver = self.floatToStr(self.get_state("sensor.vijver_repeater_7_0"))
            temptext = "<p>aussen ist es im moment " + tempbuiten + " grad<break time='1s'/> und der temperatur von der teich ist " + tempvijver + " grad.</p>"
            ############################################
            # get the last motion from a detector and add to text
            ############################################
            bewegingmar = str(self.get_state("sensor.frietkeuken_101_100_lu"))
            uur = bewegingmar[11:13]
            minuten = bewegingmar[14:16]
            martext = "<p>Der letzte bewegung, der bei Marjolein registriert ist war<break time='1s'/> " + uur + " uhr " + minuten + ".</p>"
            ############################################
            # combine the textparts
            ############################################           
            text = starttext + waterstandtext + temptext + martext
        else:
            ############################################
            # the person that woke up wasnt rene, no report or action just a goodmorning
            # here could be actions and text for other persons.
            ############################################
            text = "gutemorgen, " + slots["person"]
        return text

    def floatToStr(self,myfloat):
        ############################################
        # replace . with , for better speech
        ############################################
        floatstr = str(myfloat)
        floatstr = floatstr.replace(".",",")
        return floatstr
