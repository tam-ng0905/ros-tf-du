#!/usr/bin/env python
import roslib
roslib.load_manifest('project2_tam_nguyen')
import rospy
import math
import tf

class FrontierFinder:

    def __init__(self):
        rospy.init_node('my_tf', anonymous=True)
        self.pos = [0,0,0] 
        self.ori = [0,0,0]
        self.listener = tf.TransformListener()
        while not rospy.is_shutdown():
            try:
                (self.pos, self.ori) = self.listener.lookupTransform('/map', '/base_footprint', rospy.Time(0))
                rospy.loginfo("Logging %s %s:",self.pos, self.ori)
            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException) as e:
                rospy.logwarn(e)
                rospy.sleep(0.5)
if __name__ == '__main__':
    try:
        x = FrontierFinder()
    except rospy.ROSInterruptException: pass
