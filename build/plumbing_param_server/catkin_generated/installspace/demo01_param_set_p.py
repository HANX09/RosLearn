#!/usr/bin/env python3

import rospy

if __name__ == "__main__":
    rospy.init_node("param_set_p")
    rospy.set_param("type_p","xiaoHuangChe")
    rospy.set_param("radius_p",0.15)
    rospy.set_param("radius_p",0.01)