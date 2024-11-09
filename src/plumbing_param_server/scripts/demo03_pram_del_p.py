#! /usr/bin/env python

import rospy

if __name__ == "__main__":
    rospy.init_node("del_param")
    rospy.delete_param("radius_p")