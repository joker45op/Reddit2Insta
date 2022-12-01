import cv2
from img1 import ratio
from PIL import Image
import numpy as np
from vidgear.gears import WriteGear


video_cap = cv2.VideoCapture("vid1.mp4")
count=0


w = int(video_cap.get(3)) 
h = int(video_cap.get(4)) 
#print(w,h)
size = (max(w,h),max(w,h))

#out = cv2.VideoWriter('file.avi,',cv2.VideoWriter_fourcc(*'mp4v'),0,(600,400) )
#out = cv2.VideoWriter('/home/img/file.mp4',-1,0, (1280,1280) )
writer = WriteGear(output_filename="Output.mkv")

while True:
    # `success` is a boolean and `frame` contains the next video frame
    success, frame = video_cap.read()
    #cv2.imshow("frame", frame)
    # wait 20 milliseconds between frames and break the loop if the `q` key is pressed
    #if cv2.waitKey(20) == ord('q'):
    if type(frame) == type(None):
      break
    #if count > 50:
    #  break
      
    count+=1
    frame1 = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    frame1 = Image.fromarray(frame1)
    frame2 = ratio(frame1,'white.jpg')
    f = np.array(frame2)
    f= cv2.cvtColor(f, cv2.COLOR_RGB2BGR)
    #out.write(frame)
    writer.write(f)

    print (count)


# we also need to close the video and destroy all Windows
video_cap.release()
writer.close()
cv2.destroyAllWindows()