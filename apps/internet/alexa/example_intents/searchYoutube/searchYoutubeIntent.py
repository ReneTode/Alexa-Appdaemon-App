import appdaemon.plugins.hass.hassapi as hass
import random
import urllib
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

class searchYoutubeIntent(hass.Hass):

    def initialize(self):
        return

    def getIntentResponse(self, slots, devicename):
        ############################################
        # this intent creates a dashboard with the top 6 from a youtube search
        # it also creates 6 fullscreen dashboards for each part,
        # you can view those dashboards with the showYoutubeIntent
        ############################################
        try:
            x = 0
            textToSearch = slots["search"]
            query = urllib.parse.quote(textToSearch)
            url = "https://www.youtube.com/results?search_query=" + query
            url_response = urllib.request.urlopen(url).readlines()
            for line in url_response:
                if "yt-uix-tile-link" in line.decode("utf-8") :
                    start = line.decode("utf-8").find("watch?v=")
                    if line.decode("utf-8")[start+7:start+8] == "=" and line.decode("utf-8")[start+19:start+20] == '"' and x<7:
                        try:
                            widgetfile =  open(self.args["dashboarddir"] + self.args["VideoWidgetsOverviewDash"][x] + ".yaml","w")
                            widgetfile.write("widget_type: iframe\n")
                            widgetfile.write("url_list:\n")
                            widgetfile.write("  - https://www.youtube.com/embed/")
                            widgetfile.write(line.decode("utf-8")[start+8:start+19])
                            widgetfile.close
                        except:
                            self.log("a small youtubewidget could not be created")
                        try:
                            widgetfile2 =  open(self.args["dashboarddir"] + self.args["VideoWidgetsSingleVideoDash"][x] + ".yaml","w")
                            widgetfile2.write("widget_type: iframe\n")
                            widgetfile2.write("url_list:\n")
                            widgetfile2.write("  - https://www.youtube.com/embed/")
                            widgetfile2.write (line.decode("utf-8")[start+8:start+19] + "?autoplay=1")
                            widgetfile2.close
                        except:
                            self.log("a fullscreen youtubewidget could not be created")
                        x = x + 1
                    elif x >= 7:
                        #self.log("stop search")
                        break
            self.dash_navigate("dash_youtube", 60)
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

