#! /usr/bin/env python

import rospy
"""
get_param(键,default)
若有返回值则返回,没有返回default
get_param_cached

get_param_names
获取键的集合
has_param
判断键是否存在
search_param
寻找参数的键，返回完整键名
"""
if __name__ == "__main__":
    rospy.init("param_get_p")
