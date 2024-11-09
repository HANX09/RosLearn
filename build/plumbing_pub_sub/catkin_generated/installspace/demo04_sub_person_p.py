#!/usr/bin/env python3

import rospy
from plumbing_pub_sub.msg import Person

def doMsg(person):
    rospy.loginfo(f"听到的信息：{person.name},{person.age},{person.height}")

if __name__ == "__main__":
    rospy.init_node("dama")
    sub = rospy.Subscriber("Talk",Person,doMsg,queue_size=10)
    rospy.spin()