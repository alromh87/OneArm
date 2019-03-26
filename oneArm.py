#!/usr/bin/env python
#Bradford Johnson

import rospy
import moveit_commander
import sys
import geometry_msgs.msg
import moveit_msgs.msg
import random   

print "Imported and running!"

def main():
    print "Hi"
    
    rob = moveit_commander.RobotCommander()
    one_arm = moveit_commander.MoveGroupCommander("manipulator")
    print "I've got you!"
    
    #print rob.get_current_state()
    
    goal = geometry_msgs.msg.Pose()
    goal = one_arm.get_current_pose().pose
#    goal.orientation.w = 0
#    goal.orientation.x = 0
#    goal.orientation.y = 0
#    goal.orientation.z = 1.57

    print "Initial pose:"
    print one_arm.get_current_pose().pose
    
    for x in range(0,1):
#        goal.position.x = .7
#        goal.position.y = 0
#        goal.position.z = 1
        goal.position.x = 0.817434355362
        goal.position.y = 0.0259007808625
        goal.position.z = 1.19833020259
        
        print "Trying to get to:"
        print goal
        
        one_arm.set_pose_target(goal)
        plan1 = one_arm.plan()
        one_arm.go(wait=True)
        print "Pose:"
        print one_arm.get_current_pose().pose

        
if __name__ == '__main__':
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('goalsender')
    main()
