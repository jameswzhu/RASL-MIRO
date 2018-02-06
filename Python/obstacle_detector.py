
################################################################################################
#                                                                                  
# An 'obstacle_detector' object watches the sonar range data and the cliff sensor          
# data on the MIRO's platform/sensors topic and publishes warnings if the robot is             
# near a cliff or an object. Warnings are published to the 'Obstacle_Warnings' topic   
#                                                                                                                                                                    
# Created by Jacob Gloudeans                                                                 
# 2/06/2018                                                                                    
#                                                                                              
################################################################################################

import rospy
from miro_msgs.msg import platform_sensors
from std_msgs.msg import String
from array import array


class obstacle_detector:

	CLIFF_CUTOFF = 3
	SONAR_CUTOFF = 0.15
	CLIFF_MSG = "CLIFF DETECTED"
	OBJECT_MSG = "OBSTACLE DETECTED"

	def __init__(self, print_warnings=False):
		self.sensor_stream = rospy.Subscriber("/miro/rob01/platform/sensors", platform_sensors, self.sensor_stream_callback)
		self.publisher = rospy.Publisher("Obstacle_Warnings", String, queue_size=1)
		self.cliff_reading = 0
		self.sonar_reading = 0
		self.print_warnings = print_warnings

	def sensor_stream_callback(self, data): 
		self.cliff_reading = array("B", data.cliff)   # Message sent as uint8[2], this converts it to array object
		self.sonar_reading = data.sonar_range.range

		if self.cliff_reading[0] < self.CLIFF_CUTOFF or self.cliff_reading[1] < self.CLIFF_CUTOFF:
			self.publisher.publish(self.CLIFF_MSG)
			if self.print_warnings:
				print self.CLIFF_MSG

		if self.sonar_reading < self.SONAR_CUTOFF and self.sonar_reading != 0.0:
			self.publisher.publish(self.OBJECT_MSG)
			if self.print_warnings:
				print self.OBJECT_MSG

	def __repr__(self):
		return "Cliff:\t" + str(self.cliff_reading) + "\n" + "Sonar:\t" + str(self.sonar_reading)



if __name__ == "__main__":
	detector = obstacle_detector(print_warnings=True)
	rospy.init_node("obstacle_detection", anonymous=True)
	rospy.spin()








