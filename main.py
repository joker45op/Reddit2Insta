import os
from red import download
import img1
import json
import vidg
from uploader import upload
from extras import remove_uploaded
# download from redit
# correct ratio
# upload to instagram

def main():
  download()
  #os.chdir("/home/img/downloads")
  print("downloads completed")
  f = open('info.json',"r")
  data = json.loads(f.read())
  #print(data)
  files = os.listdir("downloads")
  for fi in files:
    name,ext = fi.split(".")
    print("starting to process {0}". format (fi))
    if ext == "mp4":
      vidg.pura_vid(name)
    elif ext == "jpeg":
      img1.ratio_img(name)
    elif ext=="json":
      continue 
    else:
      print("filename error")
    
    print("{0} done".format(fi))
  upload()
  
  f = open('info.json',"r")
  for name in f:
    remove_uploaded(name)
  
def main2():
  upload()
main()