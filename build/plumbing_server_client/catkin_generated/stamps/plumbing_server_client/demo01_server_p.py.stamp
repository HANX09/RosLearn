#! /usr/bin/env python

import rospy
from plumbing_server_client.srv import AddInts,AddIntsRequest,AddIntsResponse
# from plumbing_server_client.srv import *

def doNum(request):
    num1 = request.num1
    num2 = request.num2
    sum = num1 + num2
    response = AddIntsResponse()
    response.sum = sum
    rospy.loginfo(f"num1 = {num1},num2 = {num2},sum = {sum}")
    return response

if __name__ == "__main__":
    rospy.init_node("AddServer")
    server = rospy.Service("addInts",AddInts,doNum)
    rospy.loginfo("Server Start...")
    rospy.spin()