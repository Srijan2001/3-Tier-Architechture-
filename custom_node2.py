#! /usr/bin/env python
import rospy
from custom_task.msg import Num
from custom_task2.msg import Num2

rospy.init_node("custom_node2",anonymous=True)
pub=rospy.Publisher('/custom_data2',Num2,queue_size=10)
rate=rospy.Rate(10)
msg2=Num2()
	
def callback(data):
	msg2.name=data.name

	if (data.age)>=18:
		msg2.status="Eligible"
	else:
		msg2.status="Ineligible"

	#rospy.loginfo(msg2)	
	pub.publish(msg2)
	rate.sleep()
				

def listener():	
	rospy.Subscriber("/custom_data",Num,callback)
	rospy.spin()

if __name__=='__main__':
	listener()

