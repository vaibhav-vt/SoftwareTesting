import cv2
import numpy as np

# x_circle = 0
# y_circle = 0

def detect_circles(img):
  output = img.copy()
  #detect circles and round off
  circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.2, 100)
  circles = np.uint16(np.around(circles))

  x_circle =  circles[0][0][0]
  y_circle = circles[0][0][1]

  #plot circle
  for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(output,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(output,(i[0],i[1]),2,(0,0,255),3)

  return (output, x_circle, y_circle)
