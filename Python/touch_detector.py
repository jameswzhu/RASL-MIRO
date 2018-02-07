import rospy
import numpy
from miro_msgs.msg import platform_sensors
from std_msgs.msg import String
from array import array

class touch_detector:

	HEAD_TOUCH_MSG = "HEAD TOUCH DETECTED"
	BODY_TOUCH_MSG = "BODY TOUCH DETECTED"

	def __init__(self, print_warnings=False):
		self.sensor_stream = rospy.Subscriber("/miro/rob01/platform/sensors", platform_sensors, self.sensor_stream_callback)
		self.publisher = rospy.Publisher("Touch_Monitor", String, queue_size=1)
		self.head_touch_reading = 0
		self.body_touch_reading=0
		self.print_warnings = print_warnings

	def sensor_stream_callback(self, data): 
		self.head_touch_reading = numpy.sum(data.touch_head)
		self.body_touch_reading = numpy.sum(data.touch_body)

		if self.head_touch_reading[0] > 0 or self.head_touch_reading[1] > 0
			self.publisher.publish(self.HEAD_TOUCH_MSG)
			if self.print_warnings:
				print self.HEAD_TOUCH_MSG

		if self.body_touch_reading[0] > 0 or self.body_touch_reading[0] > 0 
			self.publisher.publish(self.BODY_TOUCH_MSG)
			if self.print_warnings:
				print self.BODY_TOUCH_MSG

	def __repr__(self):
		return "Head:\t" + str(self.cliff_reading) + "\n" + "Body:\t" + str(self.sonar_reading)



if __name__ == "__main__":
	detector = touch_detector(print_warnings=True)
	rospy.init_node("touch_detector", anonymous=True)
	rospy.spin()
