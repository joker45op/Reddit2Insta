#import os
from RedDownloader import RedDownloader
#from os.path import exists
import json

#os.chdir('downloads')
#file = RedDownloader.Download("https://www.reddit.com/r/wholesomememes/comments/vfa89c/it_really_do_be_like_that/?utm_medium=android_app&utm_source=share",output="MyAwesomeRedditMedi")

def take_list(list_file):
  f = open(list_file)
  lst = f.readlines()
    #print(lst)
  f.close()
  return lst 
    
    
def download():
  print("starting downloads")
  lst = take_list("list_file.txt")
  #os.chdir("/home/img/downloads")
  # info = open("info.j","w")
  infoli=[]
  
  for count,l in enumerate(lst):
    title = RedDownloader.GetPostTitle(l).Get()
    author= RedDownloader.GetPostAuthor(l).Get()
    file = RedDownloader.Download(l,output="downloads/"+str(count))
    #print("title :- ",title)
    #print ("author:- ", author)
    infoli.append([count,title,author])
  #print(infoli)
  f=open('info.json', 'w')
  json.dump(infoli, f)
  f.close()
  
#download()