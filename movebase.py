#!/usr/bin/env python

import rospy 
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client():
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = -1.0
    goal.target_pose.pose.position.y = 1.0

    goal.target_pose.pose.orientation.w = 1.0

    client.send_goal(goal)
    wait = client.wait_for_result()

    if not wait:
        rospy.logerr("Not Available")
        rospy.signal_shutdown("Action not available")
    else:
        return client.get_result()

if __name__ == '__main__':
    try:
        rospy.init_node('movebase')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal reached")
    except rospy.ROSInterruptException:
        rospy.loginfo("Finished")
