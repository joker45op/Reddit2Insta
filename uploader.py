from instagrapi import Client
from instagrapi.types import Usertag,Location
import os
import json
from remove import remove_uploaded

def upload():
  #cl = Client()
  #print(cl)
  #cl.login(username, password)

  #os.chdir("tooUpload")
  li = os.listdir("readytoupload")
  #print(li)
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
    #print (l)
    a = l.split(".")
    #print(len(a))
    if a[1] == "mp4" and len(a) == 2 :
      print("upload reel")
      #media = cl.clip_upload("readytoupload/{0}".format(str(l)),caption.format(data[int(a[0])][1],data[int(a[0])][2]),location=Location(name='USA', lat=40.71, lng=74.00))
    elif a[1] == "jpg" and len(a) == 2:
      print("upload pic")
      #media = cl.photo_upload("readytoupload/{0}".format(str(l)),caption.format(data[int(a[0])][1],data[int(a[0])][2]),location=Location(name='USA',lat=40.71, lng=74.00))
    else:
      print ("unknown")
    remove_uploaded(l)
#media = cl.clip_upload("Output.mp4","test for first bot upload",location=Location(name='USA', lat=59.96, lng=30.29))
upload()
