#! /usr/bin/env python
import rospy
from custom_task.msg import Num

def talker():
	pub=rospy.Publisher('/custom_data',Num,queue_size=10)			#Name is being published to /custom_data topic 

	rospy.init_node('custom_node1',anonymous=True)				#Name of the node is custom_node1

	rate=rospy.Rate(10)
	msg= Num()

	while not rospy.is_shutdown():
		msg.name= raw_input("Name: ")
		msg.age=int(raw_input("Age: "))
		rospy.loginfo(msg)
		pub.publish(msg)
		rate.sleep()

if __name__=='__main__':
	try:
	    talker()
	except rospy.ROSInterruptException:
	    pass
