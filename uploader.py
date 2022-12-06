from instagrapi import Client
from instagrapi.types import Usertag,Location
import os
import json
from details import username, password

def upload():

  try:
    cl = Client()
    cl.login(username,password)

  except:
    def get_code_from_sms(username):
      while True:
          code = input(f"Enter code (6 digits) for {username}: ").strip()
          if code and code.isdigit():
              return code
      return None
    get_code_from_sms(username=username)

    li = os.listdir("readytoupload")
    f = open('info.json',"r")
    data = json.loads(f.read())
    caption = '''{0}
    follow me now :- @legendarymemezs
    .
    .
    it is a re-reddit postedt by {1}
    .
    .
    #memeimages #newestmemes #todaymemes #recentmemes #decentmemes #memearmy #memedose #memehumor #questionablememes #sickmeme #oldmeme #unusualmeme #memeculture #memehour #bizarrememe #scarymeme #sarcasm #goofymemes #entertaining #ironic #stupidmemes #crazymemes #lightmeme #annoyingthings #memehearted #wtfmeme #dogmemes #catmeme #fortnitememes #clevermemes'''
    print ("start to upload")
    for l in li:
      print (l)
      a = l.split(".")
      if a[1] == "mp4" and len(a) == 2 :
        print("upload reel")
        media = cl.clip_upload("readytoupload/{0}".format(str(l)),caption.format(data[int(a[0])][1],data[int(a[0])][2]),location=Location(name='USA', lat=40.71, lng=74.00))
      elif a[1] == "jpg" and len(a) == 2:
        print("upload pic")
        media = cl.photo_upload("readytoupload/{0}".format(str(l)),caption.format(data[int(a[0])][1],data[int(a[0])][2]),location=Location(name='USA',lat=40.71, lng=74.00))
      else:
        print ("unknown")
  
