import numpy as np
import cv2
  
  
video = cv2.VideoCapture('video.mp4')
out = cv2.VideoWriter('output.mp4',cv2.VideoWriter_fourcc(*'mp4v'),60,(640,480))
# define a video capture object
image = cv2.imread("img2.jpg")

size = (640,480)

print(video.isOpened())

while(video.isOpened()):
      
    # Capture the video frame
    # by frame
    ret, frame = video.read()
  
    # Display the resulting frame

    ret, frame = video.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))
 
 
    u_green = np.array([104, 70, 153])
    l_green = np.array([30, 0, 30])
 
    mask = cv2.inRange(frame, l_green, u_green)
    res = cv2.bitwise_and(frame, frame, mask = mask)
 
    f = frame - res
    f = np.where(f == 0, image, f)
 

    out.write(frame)
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

  
# After the loop release the cap object
out.release()
out.release()