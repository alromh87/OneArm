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
    
    for x in range(0,5):
        goal.position.x = .7
        goal.position.y = 0
        goal.position.z = 1
        
        print goal
        
        one_arm.set_pose_target(goal)
        plan1 = one_arm.plan()
        one_arm.go(wait=True)
        
#        #rospy.sleep(5)
#        
#        goal.position.x+=.29
#        goal.position.y-=.415
#        goal.position.z-=.87
#        one_arm.set_pose_target(goal)
#        print "ya"
#        plan1 = one_arm.plan()
#        one_arm.go(wait=True)
#        
#        goal.position.x = .7
#        goal.position.y = 0
#        goal.position.z = 1
#        one_arm.set_pose_target(goal)
#        plan1 = one_arm.plan()
#        one_arm.go(wait=True)
        
        goal.position.x = random.uniform(.7,1.1)
        goal.position.y = random.uniform(-.4,.4)
        goal.position.z = .2
        one_arm.set_pose_target(goal)
        print "goal = (" + str(goal.position.x) + ", " + str(goal.position.y) + ")"
        plan1 = one_arm.plan()
        one_arm.go(wait=True)
        
        goal.position.z = .13
        one_arm.set_pose_target(goal)
        plan1 = one_arm.plan()
        one_arm.go(wait=True)
        
        goal.position.z = .2
        one_arm.set_pose_target(goal)
        plan1 = one_arm.plan()
        one_arm.go(wait=True)

        
#    for x in range(0,4):
#        goal.position.z-=.15
#        one_arm.set_pose_target(goal)
#        print "ya"
#        plan1 = one_arm.plan()
#        one_arm.go(wait=True)

    goal.position.x = .7
    goal.position.y = 0
    goal.position.z = 1
    
    print goal
    
    one_arm.set_pose_target(goal)
    plan1 = one_arm.plan()
    one_arm.go(wait=True)
        
    print one_arm.get_current_pose().pose

if __name__ == '__main__':
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('goalsender')
    main()
