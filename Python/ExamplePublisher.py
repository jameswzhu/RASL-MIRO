 
#!/usr/bin/env python

#
# Publisher example from ROS documentation
# http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
#
   
import rospy
from std_msgs.msg import String

def talker():
	pub = rospy.Publisher('chatter', String, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		message = "Current time is " + str(rospy.get_time())
		pub.publish(message)
		rate.sleep()


# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		print "ROSInterrupException occured"
	