#! /usr/bin/env python

import rospy
from  std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("sanDai")
    pub = rospy.Publisher("che",String,queue_size=10) #发布者对象
    msg = String() #发布数据对象
    rate = rospy.Rate(1)
    count = 0
    rospy.sleep(2)
    while not rospy.is_shutdown():
        count += 1
        msg.data = "hello" + str(count)
        pub.publish(msg.data)
        rospy.loginfo("%s",msg.data)
        rate.sleep()