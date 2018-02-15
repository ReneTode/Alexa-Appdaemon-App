# Tutorial

This tutorial has 3 parts
1) The configuration from Appdaemon
2) the configuration from NGINX as server before Appdaemon and Homeassistant
3) The configuration from Amazon developer (the skill)
4) Adding intents to the skill
5) Addings Intent apps to Appdaemon

to use and configure this app i expect people to have the following:
1) Appdaemon working and configured for normal use
2) Letsencrypt installed
3) the capability to find and edit files in a linux environment
4) basic understanding from lists [] and dictionairies {} 

Allthough it is probably also possible to use this with Hassio, i dont know how configuring on that platform would go.
for that reason i dont support tjis app on that platform.

## Part 1 configuring Appdaemon

This is the most simple part from the total.
All we have to do is edit the appdaemon.yaml
In the section appdaemon we have to add 2 lines:
```
  api_key: Your_password
  api_port: any_port
```
Remember that the api port needs to be a different port then your dashboard port and it must be a free usable port.
if you dont have any idea i suggest using 6061 or 5051

## Part 2 configuring NGINX

if you dont have NGINX installed before you need to install NGINX. (sudo apt-get install nginx)
this part can only work when you dont have ssl installed in home assistant.
most people only have 1 outside IP (the router) and so there is only 1 https port available.
to connect to Alexa we need https so we need a way to split up that port.
the way to do that is like this:
https://yourname.duckdns.org goes to http://internalIP:8123 (home assistant)
https://yourname.duckdns.org/api/appdaemon/*.* goes to http://internalIP:yourAPIport/api/appdaemon
i configured it this way (probably not the best or cleanest way but it works)
after installing NGINX
find the file /etc/nginx/sites-enabled/default and edit it.
my configuration is like this:
```
server {
        listen 80;
        server_name *.duckdns.org;
        return 301 https://$server_name$request_uri;
}
server {
        listen 443 ssl;
        server_name YOURNAME.duckdns.org;
        ssl on;  
        ssl_certificate /etc/letsencrypt/live/YOURNAME.duckdns.org/fullchain.pem; # /etc/nginx/cert.crt;
        ssl_certificate_key /etc/letsencrypt/live/YOURNAME.duckdns.org/privkey.pem; # /etc/nginx/cert.key; 
        ssl_session_cache shared:SSL:10m;
        ssl_protocols TLSv1.1 TLSv1.2;
        ssl_ciphers 'EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH';
        ssl_prefer_server_ciphers on;
        proxy_buffering off;

        location / {
            proxy_pass http://YOUR_LOCAL_IP:8123;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
        }

        location /api/appdaemon/ {
            allow all;
            proxy_pass http://YOUR_LOCAL_IP:YOUR_API_PORT;
            proxy_set_header Host $host;
            proxy_redirect http:// http://;
        }

}
```
Remember if you also want the dashboard reached outside your network, you must also add a configuration part for that here.
I dont use dashboards outside my own network so thats why i dont have that included.
After you have set this up Alexa should be able to reach your appdaemon.

## Part 3 the skill

1) Go to developer.amazon.com and login.
![Alt text](images/tutorial1.jpg)

2) chose developer console at the top right
![Alt text](images/tutorial2.jpg)

3) chose Alexa
![Alt text](images/tutorial3.jpg)

4) chose get started for alexa skills kit
![Alt text](images/tutorial4.jpg)

5) chose add new skill at the top right
![Alt text](images/tutorial5.jpg)

6) give your skill a name and an invocation name (the name you say to alexa) and chose a language and chose save
for demo i use appdaemon, Andrew and english

7) chose configuration in the menu on the left
![Alt text](images/tutorial6.jpg)

8) chose endpoint https and provide the url that we created to reach appdaemon like: https://yourname.duckdns.org/api/appdaemon/alexa_api?api_password=your_password
and chose save
![Alt text](images/tutorial7.jpg)

9)chose ssl certificate in the menu
chose "My development endpoint has a certificate from a trusted certificate authority"
and save
![Alt text](images/tutorial8.jpg)

10) chose interaction model in the left menu
![Alt text](images/tutorial9.jpg)

11) chose the big black button "lauch skill builder beta"
![Alt text](images/tutorial10.jpg)

12) now we are actually ready to start creating the skill intents. you can get back to the configuration by chosing configuration on the top right.
if you want to add your own intents then you can start by adding an intent and creating an app for that intent. if you want to add existing intents then follow the next steps. dont forget the basic intents i have implemented in the app a yesIntent, changing the StopIntent, and HelpIntent, but they are optional.

13) chose code editor in the menu left
![Alt text](images/tutorial11.jpg)


we now have a basic skill.
to this we can add intents and slottypes as much as we like.

## Part 4 the intents and slottypes

the skill in total looks like:
```
{
 "languageModel": {"intents": [], "types":[],  "invocationName": "Andrew"},
 "prompts": [],
 "dialog": {"intents": []}
}
```
between the brackets [] we can add our stuff as comma seperated lists.

an example from a "type" looks like
```
{"name": "mylocations", "values": 
          [
          {"id": null, "name": {"value": "livingroom ", "synonyms": []}},
          {"id": null, "name": {"value": "bedroom", "synonyms": []}},
          {"id": null, "name": {"value": "pond", "synonyms": []}},
          {"id": null, "name": {"value": "aquarium", "synonyms": []}}
          ]
 }
 ```
 
an example from an intent looks like:
```
{"name": "temperatureStateIntent",
    "samples": 
          [
          "what is the temperature in {location}",
          "how warm is it in {location}",
          "what temperature has {location}",
          "tell me the temperature",
          "what is the temperature"
          ],
    "slots": 
          [
          {"name": "location",
           "type": "mylocations",
           "samples": 
                [
                "{location}"
                ]
          }
          ]
}
```

