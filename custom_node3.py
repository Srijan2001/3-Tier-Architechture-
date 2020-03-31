#!/usr/bin/env python
import rospy
from custom_task2.msg import Num2

def callback(data):
    rospy.loginfo("%s is %s" % (data.name, data.status))

def listener():
    rospy.init_node('custom_node3', anonymous=True)
    rospy.Subscriber("/custom_data2", Num2, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

