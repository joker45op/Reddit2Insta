import os

def remove_uploaded(name):
  spli = name.split(".")
  if spli[1] == "jpg" and len(spli) == 2:
    os.remove('downloads/{0}.jpeg'.format(str(spli[0])))
    os.remove('readytoupload/{0}'.format(str(name)))
    
  elif spli[1] == "mp4" and len(spli) == 2:
    os.remove('downloads/{0}'.format(str(name)))
    os.remove('readytoupload/{0}'.format(str(name)))
    os.remove('readytoupload/{0}.jpg'.format(str(name)))
    os.remove('audioofvid/{0}.mp3'.format(str(spli[0])))
    os.remove('videospro/{0}.mkv'.format(str(spli[0])))
    
    
def detect_url(url):
  if "www.reddit.com" in url:
    print("reddit")
    
url = "https://www.reddit.com/r/USAmemes/comments/u71yza/a_dark_one/?utm_medium=android_app&utm_source=share"

detect(url)