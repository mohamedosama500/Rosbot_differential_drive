#!/usr/bin/env python

import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys
from sensor_msgs.msg import CameraInfo
import camera_info_manager

rospy.init_node ('read_video')
bridge = CvBridge()

def image_callback(ros_image):
    print ('got an image')
    global bridge
    #convert ros_image into an opencv-compatible image
    try:
      frame = bridge.imgmsg_to_cv2(ros_image, "bgr8")
    except CvBridgeError as e:
        print(e)
    #from now on, you can work exactly like with opencv
    while(True):
      ret, frame = video_capture.read()
      
      frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
      edges = cv2.Canny(frame,100,200)
      cv2.imshow("Frame",edges)
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    video_capture.release()
    cv2.destroyAllWindows()

    
def main(args):
  rospy.init_node('image_converter', anonymous=True)
  #for turtlebot3 waffle
  #image_topic="/camera/rgb/image_raw/compressed"
  #for usb cam
  #image_topic="/usb_cam/image_raw"
  image_sub = rospy.Subscriber("/usb_cam/image_raw",Image, image_callback)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
