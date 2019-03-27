#!/usr/bin/env python
#Bradford Johnson

import rospy
import moveit_commander
import sys
import geometry_msgs.msg
import moveit_msgs.msg
import random
import math
import copy

print "Imported and running!"

rob = moveit_commander.RobotCommander()
one_arm = moveit_commander.MoveGroupCommander("manipulator")

def goto(goal):
  print "Trying to get to:"
  print goal
  one_arm.set_pose_target(goal)
  plan1 = one_arm.plan()
  one_arm.go(wait=True)

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
    z_up = 0.20 #+.1 #Add for debug
    z_down = 0.170273358 #+.1 #Add for debug
    x_start = 0.790600268636
    y_start = -0.753538976022
    offset_x = 0
    offset_y = 0


    goal.position.z = z_up
    goto(goal)

    waypoints = []
    waypoints.append(copy.deepcopy(goal))
#Margins
#        goal.position.x = 1.13498199609
#        goal.position.y = 0.801180714226
#        waypoints.append(copy.deepcopy(goal))
#        goal.position.x = 0.805600268636
#        goal.position.y = -0.753538976022
#        waypoints.append(copy.deepcopy(goal))

    #O
    fn = 20
    goal.position.z = z_down
    for n in range(0,fn):
      goal.position.x = x_start+size*(offset_x+.5-(math.sin(2*n*math.pi/(fn-1))/2)-margin)
      goal.position.y = y_start+size*(offset_y+.5-(math.cos(2*n*math.pi/(fn-1))/2)-margin)
      waypoints.append(copy.deepcopy(goal))

    goal.position.z = z_up
    waypoints.append(copy.deepcopy(goal))

    #N
    offset_y += 1;
    goal.position.y = y_start+size*(offset_y+margin)
    goal.position.x = x_start+size*((1+offset_x)-margin)
#    waypoints.append(copy.deepcopy(goal))
    goal.position.z = z_down
    waypoints.append(copy.deepcopy(goal))
    goal.position.x = x_start+size*(offset_x+margin)
    waypoints.append(copy.deepcopy(goal))
    goal.position.y = y_start+size*((1+offset_y)-margin)
    goal.position.x = x_start+size*((1+offset_x)-margin)
    waypoints.append(copy.deepcopy(goal))
    goal.position.x = x_start+size*(offset_x+margin)
    waypoints.append(copy.deepcopy(goal))
    goal.position.z = z_up
    waypoints.append(copy.deepcopy(goal))

    #E
    offset_y += 1;
    goal.position.y = y_start+size*((1+offset_y)-margin)
    goal.position.x = x_start+size*(offset_x+margin)
#    waypoints.append(copy.deepcopy(goal))
    goal.position.z = z_down
    waypoints.append(copy.deepcopy(goal))
    goal.position.y = y_start+size*(offset_y+margin)
    waypoints.append(copy.deepcopy(goal))
    goal.position.x = x_start+size*((1+offset_x)-margin)
    waypoints.append(copy.deepcopy(goal))
    goal.position.y = y_start+size*((1+offset_y)-margin)
    waypoints.append(copy.deepcopy(goal))
    goal.position.z = z_up
    waypoints.append(copy.deepcopy(goal))
    goal.position.y = y_start+size*(offset_y+margin)
    goal.position.x = x_start+size*(offset_x+0.5)
    waypoints.append(copy.deepcopy(goal))
    goal.position.z = z_down
    waypoints.append(copy.deepcopy(goal))
    goal.position.y = y_start+size*((1+offset_y)-margin)
    waypoints.append(copy.deepcopy(goal))
    goal.position.z = z_up
    waypoints.append(copy.deepcopy(goal))

    #A
    offset_y = 0;
    offset_x += 1;
    goal.position.y = y_start+size*(offset_y+margin)
    goal.position.x = x_start+size*((1+offset_x)-margin)
 #   waypoints.append(copy.deepcopy(goal))
    goal.position.z = z_down
    waypoints.append(copy.deepcopy(goal))
    goal.position.y = y_start+size*(offset_y+0.5)
    goal.position.x = x_start+size*(offset_x+margin)
    waypoints.append(copy.deepcopy(goal))
    goal.position.y = y_start+size*((1+offset_y)-margin)
    goal.position.x = x_start+size*((1+offset_x)-margin)
    waypoints.append(copy.deepcopy(goal))
    #TODO enahance A
    goal.position.y = y_start+size*(offset_y+margin)
    goal.position.x = x_start+size*(offset_x+0.5)
    waypoints.append(copy.deepcopy(goal))
    goal.position.z = z_up
    waypoints.append(copy.deepcopy(goal))

    #R
    offset_y += 1;
    goal.position.y = y_start+size*(offset_y+margin)
    goal.position.x = x_start+size*((1+offset_x)-margin)
#    waypoints.append(copy.deepcopy(goal))
    goal.position.z = z_down
    waypoints.append(copy.deepcopy(goal))
    goal.position.x = x_start+size*(offset_x+margin)
    waypoints.append(copy.deepcopy(goal))
    goal.position.y = y_start+size*((1+offset_y)-margin)
    goal.position.x = x_start+size*(offset_x+((0.5-margin)/2))
    waypoints.append(copy.deepcopy(goal))
    goal.position.y = y_start+size*(offset_y+margin)
    goal.position.x = x_start+size*(offset_x+.5)
    waypoints.append(copy.deepcopy(goal))
    goal.position.y = y_start+size*((1+offset_y)-margin)
    goal.position.x = x_start+size*((1+offset_x)-margin)
    waypoints.append(copy.deepcopy(goal))
    goal.position.z = z_up
    waypoints.append(copy.deepcopy(goal))

    #M
    offset_y += 1;
    goal.position.y = y_start+size*(offset_y+margin)
    goal.position.x = x_start+size*((1+offset_x)-margin)
#    waypoints.append(copy.deepcopy(goal))
    goal.position.z = z_down
    waypoints.append(copy.deepcopy(goal))
    goal.position.x = x_start+size*(offset_x+margin)
    waypoints.append(copy.deepcopy(goal))
    goal.position.y = y_start+size*(offset_y+.5)
    goal.position.x = x_start+size*(offset_x+.5)
    waypoints.append(copy.deepcopy(goal))
    goal.position.x = x_start+size*(offset_x+margin)
    goal.position.y = y_start+size*((1+offset_y)-margin)
    waypoints.append(copy.deepcopy(goal))
    goal.position.x = x_start+size*((1+offset_x)-margin)
    waypoints.append(copy.deepcopy(goal))
    goal.position.z = z_up
    waypoints.append(copy.deepcopy(goal))

    (plan, fraction) = one_arm.compute_cartesian_path(
                                   waypoints,   # waypoints to follow
                                   0.01,        # eef_step
                                   0.0)         # jump_threshold

    one_arm.execute(plan, wait=True)

#        print "----------------Pose:-------------------"
#        print one_arm.get_current_pose().pose

        
if __name__ == '__main__':
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('goalsender')
    main()
