from RedDownloader import RedDownloader
import json


def take_list(list_file):
  f = open(list_file)
  lst = f.readlines()
  f.close()
  return lst 
    
    
def download():
  print("starting downloads")
  lst = take_list("list_file.txt")
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