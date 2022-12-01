
from PIL import Image
import numpy as np

def ratio_vid(overlay_img, back_img):
  img1 = overlay_img
  w = img1.size[0]
  h = img1.size[1]
  h1,w1 = 0,0
  x,y = 0,0
  if w>h:
    h1 = w
    w1=h1
    y = int((h1-h)/2)
  else:
    w1=h
    h1=w1
    x = int((w1-w)/2)
  
  #print (w,h)
  #print (w1,h1)
  
  img2 = Image.open(back_img)
  img2 = img2.resize((w1,h1))
  
  img2.paste(img1,(x,y))
  if img2.mode != 'RGB':
    img2.convert('RGB')
    
  return img2

def ratio_reel(overlay_img, back_img):
  
  #img1 = Image.open(overlay_img)
  img1=overlay_img
  w = int(img1.size[0]*0.9)
  h = int(img1.size[1]*1.6)
  img1= img1.resize((w,h))
  h1,w1 = 0,0
  x,y = 0,0
  if w>h:
    h1 = w
    w1=h1
    y = int((h1-h)/2)
  else:
    w1=h
    h1=w1
    x = int((w1-w)/2)
  
  #print (w,h)
  #print (w1,h1)
  
  img2 = Image.open(back_img)
  img2 = img2.resize((w1,h1))
  
  img2.paste(img1,(x,y))
  if img2.mode != 'RGB':
    img2.convert('RGB')
  return img2
  
def ratio_img(overlay_img, back_img="black.jpg"):
  img1 = Image.open("downloads/{0}.jpeg".format(str(overlay_img)))
  w = img1.size[0]
  h = img1.size[1]
  h1,w1 = 0,0
  x,y = 0,0
  if w>h:
    h1 = w
    w1=h1
    y = int((h1-h)/2)
  else:
    w1=h
    h1=w1
    x = int((w1-w)/2)
  
  #print (w,h)
  #print (w1,h1)
  
  img2 = Image.open(back_img)
  img2 = img2.resize((w1,h1))
  
  img2.paste(img1,(x,y))
  if img2.mode != 'RGB':
    img2.convert('RGB')
    
  img2.save('readytoupload/{0}.jpg'.format(str(overlay_img)))
  
#ratio_img('downloads/0.jpeg',"black.jpg",0)