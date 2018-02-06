 
#!/usr/bin/env python

#
# Subscriber example from ROS documentation
# http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
#
   
import rospy
from std_msgs.msg import String


def callback(data):

	print "Someone said \"" + str(data.data) + '\"'


def listener():

	rospy.init_node('listener', anonymous=True)     # initialize node
	rospy.Subscriber("chatter", String, callback)   # create subscriber
	rospy.spin()                                    # don't exit until node is stopped

if __name__ == '__main__':
	listener()