from PIL import Image
import numpy as np

img1 = Image.open('test3.jpg')
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

print (w,h)
print (w1,h1)

img2 = Image.open('black.jpg')
img2 = img2.resize((w1,h1))

img2.paste(img1,(x,y))
if img2.mode != 'RGB':
  img2.convert('RGB')
img2.save('fin2.jpg')