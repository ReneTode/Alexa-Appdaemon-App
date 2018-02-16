import appdaemon.plugins.hass.hassapi as hass
import random

class repeatStoryIntent(hass.Hass):

    def initialize(self):
        return

    def getIntentResponse(self, slots, devicename):
        ############################################
        # repeat the story is asked
        ############################################
        try:
            ############################################
            # find out which story number was last told
            ############################################
            storydir = self.args["storydir"]
            laststoryfile = open(storydir + "laststory.txt", 'r')
            laststoryfilelines = laststoryfile.readlines()
            lastreadstorynr = int(laststoryfilelines[0])
            newstorynr = lastreadstorynr
            laststoryfile.close()

            ############################################
            # find out the name of the next story
            ############################################
            storylist = open(storydir + "storylist.txt", 'r')
            storylistlines = storylist.readlines()
            storylist.close()

            ############################################
            # get the story from the file and put it in text
            ############################################
            text = "<prosody volume='soft'>"
            story = open(storydir + storylistlines[newstorynr].strip(), 'r',encoding="ISO-8859-1")
            for line in story:
                text = text + "<p>" + line + "</p>"
            story.close()
            text = text + "</prosody>"

            ############################################
            # save the told story number for next time
            ############################################
            laststoryfile = open(storydir + "laststory.txt", 'w')
            laststoryfile.write(str(newstorynr))
            laststoryfile.close()
        except:    
            text = self.args["Error"]
        return text
