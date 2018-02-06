

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

# Saves camera streams to separate folders

class camera_subscriber:

	def __init__(self):
		self.left_stream = rospy.Subscriber("/miro/rob01/platform/caml", Image, self.left_cam_callback, queue_size=1)
		self.right_stream = rospy.Subscriber("/miro/rob01/platform/camr", Image, self.right_cam_callback, queue_size=1)
		cv2.namedWindow("Left Camera")
		cv2.namedWindow("Right Camera")
		self.leftcount = 0
		self.rightcount = 0
		self.bridge = CvBridge()


	def left_cam_callback(self, data):
		print "Left image recieved"
		new_img = self.bridge.imgmsg_to_cv2(data, "bgr8")
		cv2.imwrite("LeftImages/image_" + str(self.leftcount) + ".jpg", new_img)
		self.leftcount += 1

	def right_cam_callback(self, data):
		print "Right image recieved"
		new_img = self.bridge.imgmsg_to_cv2(data, "bgr8")
		cv2.imwrite("RightImages/image_" + str(self.rightcount) + ".jpg", new_img)
		self.rightcount += 1

# Now, this is actually useful because we could import this class into another module
# and this portion wouldn't run but the class could be used
if __name__ == "__main__":
	stream = camera_subscriber()
	rospy.init_node("Camera_Listener", anonymous=True)
	rospy.spin()