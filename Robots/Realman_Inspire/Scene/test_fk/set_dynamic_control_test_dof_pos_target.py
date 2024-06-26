from omni.isaac.dynamic_control import _dynamic_control
import random

dc = _dynamic_control.acquire_dynamic_control_interface()

art = dc.get_articulation("/World/Realman_Inspire_mimic/Realman_Inspire_R")

num_joints = dc.get_articulation_joint_count(art)
print(num_joints)

#  randomize target position of 6 dof of hand and 7 dof of arm
finger_angle_range = [0, 85]
thumb_yaw_angle_range = [0, 75]
thumb_pitch_angle_range = [-5, 35]
joint_angle_range = [-130, 130]

fk_angles = [ 1.2678,  0.2810,  1.2657,  1.4079,  0.1925,  0.5950,  0.5630,  1.8624,
         2.9764,  2.1511,  0.1759, -0.3144, -4.0239]

gt_angles = [ 0.8383,  1.2139,  1.0909,  0.1415,  0.3025,  0.2130,  1.3651,  1.5724,
         1.3709, -1.0596,  1.4615,  0.3371, -4.4066]
opt_angles = [ 0.8383,  1.2139,  1.0909,  0.1415,  0.3025,  0.2130,  1.2579,  1.7936,
         0.8709, -1.0596,  2.6379,  0.0529,  1.1513]
angles = fk_angles        

index_pos = angles[0]
middle_pos = angles[1]
ring_pos = angles[3]
pinky_pos = angles[2]
thumb_yaw_pos = angles[5]+0.1
thumb_pitch_pos = angles[4]+0.1
joint1_pos = angles[6]
joint2_pos = angles[7]
joint3_pos = angles[8]
joint4_pos = angles[9]
joint5_pos = angles[10]
joint6_pos = angles[11]
joint7_pos = angles[12]

# dynamic control to move to target position
index_dof_ptr = dc.find_articulation_dof(art, "R_index_proximal_joint")
dc.wake_up_articulation(art)
dc.set_dof_position_target(index_dof_ptr, index_pos)	

middle_dof_ptr = dc.find_articulation_dof(art, "R_middle_proximal_joint")
dc.wake_up_articulation(art)
dc.set_dof_position_target(middle_dof_ptr, middle_pos)	

ring_dof_ptr = dc.find_articulation_dof(art, "R_ring_proximal_joint")
dc.wake_up_articulation(art)
dc.set_dof_position_target(ring_dof_ptr, ring_pos)	

pinky_dof_ptr = dc.find_articulation_dof(art, "R_pinky_proximal_joint")
dc.wake_up_articulation(art)
dc.set_dof_position_target(pinky_dof_ptr, pinky_pos)	

thumb_yaw_dof_ptr = dc.find_articulation_dof(art, "R_thumb_proximal_yaw_joint")
dc.wake_up_articulation(art)
dc.set_dof_position_target(thumb_yaw_dof_ptr, thumb_yaw_pos)	

thumb_pitch_dof_ptr = dc.find_articulation_dof(art, "R_thumb_proximal_pitch_joint")
dc.wake_up_articulation(art)
dc.set_dof_position_target(thumb_pitch_dof_ptr, thumb_pitch_pos)	

arm_joint1 = dc.find_articulation_dof(art, "joint1")
dc.wake_up_articulation(art)
dc.set_dof_position_target(arm_joint1, joint1_pos)	

arm_joint2 = dc.find_articulation_dof(art, "joint2")
dc.wake_up_articulation(art)
dc.set_dof_position_target(arm_joint2, joint2_pos)	

arm_joint3 = dc.find_articulation_dof(art, "joint3")
dc.wake_up_articulation(art)
dc.set_dof_position_target(arm_joint3, joint3_pos)	

arm_joint4 = dc.find_articulation_dof(art, "joint4")
dc.wake_up_articulation(art)
dc.set_dof_position_target(arm_joint4, joint4_pos)	

arm_joint5 = dc.find_articulation_dof(art, "joint5")
dc.wake_up_articulation(art)
dc.set_dof_position_target(arm_joint5, joint5_pos)	

arm_joint6 = dc.find_articulation_dof(art, "joint6")
dc.wake_up_articulation(art)
dc.set_dof_position_target(arm_joint6, joint6_pos)	

arm_joint7 = dc.find_articulation_dof(art, "joint7")
dc.wake_up_articulation(art)
dc.set_dof_position_target(arm_joint7, joint7_pos)	

# print dof state
dof_state = dc.get_dof_state(index_dof_ptr, _dynamic_control.STATE_ALL)
print(dof_state)




