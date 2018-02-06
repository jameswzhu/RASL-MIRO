
from obstacle_detector import obstacle_detector
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist



class basic_navigator:

	def __init__(self):

		self.wheel_control = rospy.Publisher("/miro/rob01/control/cmd_vel", Twist, queue_size=1)
		self.obstacle_detector = rospy.Subscriber("Obstacle_Warnings", String, self.object_detector_callback)
		self.object_detected = False


	def object_detector_callback(self, msg):
		if (msg.data == obstacle_detector.CLIFF_MSG) or (msg.data == obstacle_detector.OBJECT_MSG):
			self.object_detected = True


	# Drive in random direction, picking new direction whenever an obstacle is detected
	def drive_randomly(self):

		# Create an obstacle/cliff detection publisher
		detector = obstacle_detector()

		# Continue running until Ctrl-C pressed
		while not rospy.is_shutdown():

			# Check for obstacle
			if self.object_detected:

				# Turn random amount between 45 and 180 degrees
				wheel_speed_l = 0.1
				wheel_speed_r = 0.1

				# Reset detected obstacle variable
				self.object_detected = False



if __name__ == "__main__":
	rospy.init_node("basic_navigator", anonymous=True)
	navigator = basic_navigator()
	navigator.drive_randomly()