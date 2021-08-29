#!/usr/bin/env python 

import cv2

#video_capture = cv2.VideoCapture(0)
video_capture = cv2.VideoCapture('video/sample.mp4')

while(True):
	ret, frame = video_capture.read()
	
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
	edges = cv2.Canny(frame,100,200)
	cv2.imshow("Frame",edges)
	if cv2.waitKey(35) & 0xFF == ord('q'):
		break

video_capture.release()
cv2.destroyAllWindows()
