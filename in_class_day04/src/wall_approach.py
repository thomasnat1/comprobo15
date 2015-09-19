#!/usr/bin/env python

""" This ROS node uses proportional control to guide a robot to a specified
    distance from the obstacle immediately in front of it """

import rospy
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry

class WallApproach(object):
    """ A ROS node that implements a proportional controller to approach an obstacle
        immediately in front of the robot """
    def __init__(self, target_distance):
        """ Initialize a node with the specified target distance
            from the forward obstacle """
        rospy.init_node('wall_approach')
        rospy.Subscriber("odom", Odometry, self.process_odom)
        rospy.Subscriber("scan", LaserScan, self.process_scan)
        
        self.controller = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        self.distanceToWall = 0

    def process_odom(self, odom):
        pass
        # print odom

    def process_scan(self, scan):
        self.distanceToWall = scan.ranges[0]
        

    def run(self):
        """ Our main 5Hz run loop """
        r = rospy.Rate(5)
        while not rospy.is_shutdown():
            twist = Twist()
            if self.distanceToWall != 0 and self.distanceToWall < 1: 
                print "GET DE FUCK OUT THE WAY"
            else:
                print "INCOMING BITCHES!"
            twist.linear.x = self.distanceToWall - 1; twist.linear.y = 0; twist.linear.z = 0
            twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
            self.controller.publish(twist)
            r.sleep()



if __name__ == '__main__':
    node = WallApproach(1.0)
    node.run()