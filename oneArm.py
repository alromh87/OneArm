#!/usr/bin/env python
#Bradford Johnson

import rospy
import moveit_commander
import sys
import geometry_msgs.msg
import moveit_msgs.msg
import random   

print "Imported and running!"

rob = moveit_commander.RobotCommander()
one_arm = moveit_commander.MoveGroupCommander("manipulator")

def goto(goal):
  print "Trying to get to:"
  print goal
  one_arm.set_pose_target(goal)
  plan1 = one_arm.plan()
  one_arm.go(wait=True)
  rospy.sleep(1)

def main():
    print "Hi"
    
    rob = moveit_commander.RobotCommander()
    one_arm = moveit_commander.MoveGroupCommander("manipulator")
    print "I've got you!"
    
    #print rob.get_current_state()
    
    goal = geometry_msgs.msg.Pose()
    goal = one_arm.get_current_pose().pose
    goal.orientation.w =  0.00890861352435 
    goal.orientation.x =  0.999909755666
    goal.orientation.y =  0.00706809305747
    goal.orientation.z = -0.0071525653066

    print "--------------Initial pose-------------------"
    print one_arm.get_current_pose().pose

    margin = 0.1
    size = 0.164690864
    z_up = 0.4166802733582
    z_down = 0.2166802733582
    x_start = 0.805600268636
#    y_start = 0.801180714226
    y_start = -0.753538976022
    offset_x = 0
    offset_y = 0

#    for x in range(0,1):
#        goal.position.x = 1.13498199609
#        goal.position.y = 0.801180714226
#        goal.position.z = z_up
#        goto(goal)

#        goal.position.x = 0.805600268636
#        goal.position.y = -0.753538976022
#        goto(goal)


    goal.position.z = z_up
    goto(goal)

    #N
    offset_y += 1;
    goal.position.y = y_start+size*(offset_y+margin)
    goal.position.x = x_start+size*((1+offset_x)-margin)
    goto(goal)
    goal.position.z = z_down
    goto(goal)
    goal.position.x = x_start+size*(offset_x+margin)
    goto(goal)
    goal.position.y = y_start+size*((1+offset_y)-margin)
    goal.position.x = x_start+size*((1+offset_x)-margin)
    goto(goal)
    goal.position.x = x_start+size*(offset_x+margin)
    goto(goal)
    goal.position.z = z_up
    goto(goal)

    #E
    offset_y += 1;
    goal.position.y = y_start+size*((1+offset_y)-margin)
    goal.position.x = x_start+size*(offset_x+margin)
    goto(goal)
    goal.position.z = z_down
    goto(goal)
    goal.position.y = y_start+size*(offset_y+margin)
    goto(goal)
    goal.position.x = x_start+size*((1+offset_x)-margin)
    goto(goal)
    goal.position.y = y_start+size*((1+offset_y)-margin)
    goto(goal)
    goal.position.z = z_up
    goto(goal)
    goal.position.y = y_start+size*(offset_y+margin)
    goal.position.x = x_start+size*(offset_x+0.5)
    goto(goal)
    goal.position.z = z_down
    goto(goal)
    goal.position.y = y_start+size*((1+offset_y)-margin)
    goto(goal)
    goal.position.z = z_up
    goto(goal)

    #A
    offset_y = 0;
    offset_x += 1;
    goal.position.y = y_start+size*(offset_y+margin)
    goal.position.x = x_start+size*((1+offset_x)-margin)
    goto(goal)
    goal.position.z = z_down
    goto(goal)
    goal.position.y = y_start+size*(offset_y+0.5)
    goal.position.x = x_start+size*(offset_x+margin)
    goto(goal)
    goal.position.y = y_start+size*((1+offset_y)-margin)
    goal.position.x = x_start+size*((1+offset_x)-margin)
    goto(goal)
    #TODO enahance A
    goal.position.y = y_start+size*(offset_y+margin)
    goal.position.x = x_start+size*(offset_x+0.5)
    goto(goal)
    goal.position.z = z_up
    goto(goal)

    #R
    offset_y += 1;
    goal.position.y = y_start+size*(offset_y+margin)
    goal.position.x = x_start+size*((1+offset_x)-margin)
    goto(goal)
    goal.position.z = z_down
    goto(goal)
    goal.position.x = x_start+size*(offset_x+margin)
    goto(goal)
    goal.position.y = y_start+size*((1+offset_y)-margin)
    goal.position.x = x_start+size*(offset_x+((0.5-margin)/2))
    goto(goal)
    goal.position.y = y_start+size*(offset_y+margin)
    goal.position.x = x_start+size*(offset_x+.5)
    goto(goal)
    goal.position.y = y_start+size*((1+offset_y)-margin)
    goal.position.x = x_start+size*((1+offset_x)-margin)
    goto(goal)
    goal.position.z = z_up
    goto(goal)

    #M
    offset_y += 1;
    goal.position.y = y_start+size*(offset_y+margin)
    goal.position.x = x_start+size*((1+offset_x)-margin)
    goto(goal)
    goal.position.z = z_down
    goto(goal)
    goal.position.x = x_start+size*(offset_x+margin)
    goto(goal)
    goal.position.y = y_start+size*(offset_y+.5)
    goal.position.x = x_start+size*(offset_x+.5)
    goto(goal)
    goal.position.x = x_start+size*(offset_x+margin)
    goto(goal)
    goal.position.y = y_start+size*((1+offset_y)-margin)
    goal.position.x = x_start+size*((1+offset_x)-margin)
    goto(goal)
    goal.position.z = z_up
    goto(goal)



#        one_arm.set_pose_target(goal)
#        plan1 = one_arm.plan()
#        one_arm.go(wait=True)
#        print "----------------Pose:-------------------"
#        print one_arm.get_current_pose().pose

        
if __name__ == '__main__':
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('goalsender')
    main()
