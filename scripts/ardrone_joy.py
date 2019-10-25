#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

#Publisher : Publish velocity
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
 
def joy_callback(data):
	twist = Twist()
        # You should change axes number according to the joystick controller
	twist.linear.x = 4*data.axes[1]
        twist.linear.y = 4*data.axes[3]
        twist.linear.z = 4*data.axes[4]
	twist.angular.z = 4*data.axes[0]
	pub.publish(twist)
 
def ardrone_joy():
	rospy.init_node('ArdroneJoy')
        #Subscriber : Receive joy topis
	rospy.Subscriber("joy", Joy, joy_callback)

	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
		rate.sleep()
	rospy.spin()
 
if __name__ == '__main__':
    ardrone_joy()
