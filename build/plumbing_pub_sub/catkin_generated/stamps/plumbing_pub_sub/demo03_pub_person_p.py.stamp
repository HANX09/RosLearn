#! /usr/bin/env python

import rospy
from plumbing_pub_sub.msg import Person
if __name__ == "__main__":
    rospy.init_node("daMa")
    pub = rospy.Publisher("Talk",Person,queue_size=10)
    person = Person()
    person.name = "张三"
    person.age = 8
    person.height = 1.85

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        pub.publish(person)
        rospy.loginfo(f"发布的数据：{person.name},{person.age},{person.height}")
        rate.sleep()
