# Alexa-Appdaemon-App

The connection between Amazon Alexa and Appdaemon for Home Assistant.
This is a complete app with all needed yaml.  
You can download the complete app into your apps directory.  
But this app contains 2 sets off yaml, english and german.
To make sure that the app doesnt run twice you need to delete the yaml files from the language you dont want. 


## Installation/Tutorial.

A tutorial and installation instructions for how to create the skill and how to configure appdaemon and nginx is included.  
Read it here: 
https://github.com/ReneTode/Alexa-Appdaemon-App/blob/master/alexa%20skill%20tutorial.md

## The Alexa app

The Alexa app is useless without intents.  
In The tutorial you can find how to create or copy intents.  
Below is a list of the included example intents with a short description.   
  
## Example Intents

1) commands  
Alexa gives a list from all commands that you have programmed.  
Helpfull for when you live in a house where several people use the skill. this way they can always ask what they can say to Alexa.  
2) goodmorning  
I use Alexa to set a sensor (sensor.rene) from Asleep to Home.  
Other automations then are programmed on the state from that sensor.  
After changing the state Alexa tells me some info i like to know like temperatures, riverwater levels, last seen movement, etc.  
I didnt take out the text parts to yaml because this listens to specific sensors.  
You need to edit the app yourselve.   
3) help  
There is a default help Intent in the conversation skill.  
You can modify and use the default or just copy the one i created.  
the default would use the skill with a capital H mine is with a small h.  
4) hotCold  
This intent checks if you say warm or cold, and then sets the heating in the room that you are in low or high, for 30 minutes.  
5) inKeller  
An intent i wrote specific for our situation.  
If we say to appdaemon that someone is there a notation is made in a logfile with the time and the person.  
If it is a known person, it saves an identification number else it saves the name.  
If the time tells it is when we are home, the skill just greetz the person.  
6) lightState  
The intent is still called lightstate, because thats what i used it for at first.  
But it tells every state from every entity in home assistant that you like.  
Just add a friendly name and the entity in the yaml and you can ask alexa for the state from that entity.  
7) repeatStory    
See Story it just tells the last told story 1 more time.  
8) searchYoutube  
This intent lets you search on youtube.  
When the search is completed, it show the top 6 search entries on a dashboard  
You can then use showYoutube to view 1 of the 6 videos  
9) SetBedOlinde and setBedOlindeOff  
2 connected skills to turn on and off 1 switch.  
The reason why i didnt use 1 intent is because the sentences my wife speaks to Alexa are not with on and off in it.  
They could be combined with 1 on/off slot in it.  
10) showYoutube  
Lets you show 1 of the 6 videos from the last youtube search on a dashboard.  
Just say the number from the video and it will show for a preset time.  
As long as you dont ask for a new search, you can always repeat the last video.  
11) sleep  
An intent to tell the state from 1 specific entity on several humorous ways.  
In this case if i use it so that my wife can ask if her heating blanket is on or off, to check if automations did work.  
12) story  
An intent that tells stories.  
In a predefined directory you can place txt files with short stories.  
In 1 file you can make a list to set the order that the stories are told.  
There is also a file that has the number from the last told story.  
That way the stories wont be repeated. with the repetStory intent you can repeat the last story as much as you like.  
You can write your own stories or just collect them from the internet.
13) temperatureState
Actually the same as the lightState intent that now tells general entity states, just with textline that are specific for temperature.  
14) viewCamera  
In the yaml you can give friendly names for all cameras you own and have created in home assistant.  
After you have created a dashboard for those cameras this intent shows the cameradashboard for a set amount of time.
15) whatDoesSomeone  
A nice way to entertain your friends. Just create humorous answer for all your friends and Alexa will speak them out.  
Also included the possibilitie to make distinction between people from your household and from outside.  
16) woIsSomeone
Somewhat like the previous Intent, just with some more specific information bout the household.
You can predifene dinertimes, when people are at work, on their way home, sleeping, etc.
Lets you ask wo someone is, without having to think about the timeschedule from that person.




  
this is a work in progress.

next steps:
- adding english version for the yaml, intent and slot files.
- adding videos
