#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PointStamped
from neato_node.msg import Bump
from geometry_msgs.msg import Twist
import tty
import select
import sys
import termios
import time

isDone = False

def process_bump(msg):
	print msg
	if msg.leftSide != 0 or msg.rightSide != 0 or msg.rightFront != 0 or msg.leftFront != 0:
		isDone = True

settings = termios.tcgetattr(sys.stdin)
rospy.init_node('receive_message')
rospy.Subscriber("bump", Bump, process_bump)

pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

twist = Twist()
twist.linear.x = 1; twist.linear.y = 0; twist.linear.z = 0
twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0

r = rospy.Rate(10)

while not isDone and not rospy.is_shutdown():
	print "loop"
	print twist
	pub.publish(twist)
	r.sleep()

twist = Twist()
twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
pub.publish(twist)

print "End" * 100