from omni.isaac.dynamic_control import _dynamic_control
import random
dc = _dynamic_control.acquire_dynamic_control_interface()

art = dc.get_articulation("/World/Realman_Inspire_R_final_5/Realman_Inspire_R")

num_joints = dc.get_articulation_joint_count(art)
print(num_joints)

#  randomize target position of 6 dof of hand and 7 dof of arm
finger_angle_range = [0, 85]
thumb_yaw_angle_range = [0, 75]
thumb_pitch_angle_range = [-5, 35]
joint_angle_range = [-130, 130]

index_pos = random.randint(finger_angle_range[0], finger_angle_range[1])
middle_pos = random.randint(finger_angle_range[0], finger_angle_range[1])
ring_pos = random.randint(finger_angle_range[0], finger_angle_range[1])
pinky_pos = random.randint(finger_angle_range[0], finger_angle_range[1])
thumb_yaw_pos = random.randint(thumb_yaw_angle_range[0], thumb_yaw_angle_range[1])
thumb_pitch_pos = random.randint(thumb_pitch_angle_range[0], thumb_pitch_angle_range[1])
joint1_pos = random.randint(joint_angle_range[0], joint_angle_range[1])
joint2_pos = random.randint(joint_angle_range[0], joint_angle_range[1])
joint3_pos = random.randint(joint_angle_range[0], joint_angle_range[1])
joint4_pos = random.randint(joint_angle_range[0], joint_angle_range[1])
joint5_pos = random.randint(joint_angle_range[0], joint_angle_range[1])
joint6_pos = random.randint(joint_angle_range[0], joint_angle_range[1])
joint7_pos = random.randint(joint_angle_range[0], joint_angle_range[1])

# dynamic control to move to target position
index_dof_ptr = dc.find_articulation_dof(art, "R_index_proximal_joint")
dc.wake_up_articulation(art)
dc.set_dof_position_target(index_dof_ptr, index_pos/180*3.14)	

middle_dof_ptr = dc.find_articulation_dof(art, "R_middle_proximal_joint")
dc.wake_up_articulation(art)
dc.set_dof_position_target(middle_dof_ptr, middle_pos/180*3.14)	

ring_dof_ptr = dc.find_articulation_dof(art, "R_ring_proximal_joint")
dc.wake_up_articulation(art)
dc.set_dof_position_target(ring_dof_ptr, ring_pos/180*3.14)	

pinky_dof_ptr = dc.find_articulation_dof(art, "R_pinky_proximal_joint")
dc.wake_up_articulation(art)
dc.set_dof_position_target(pinky_dof_ptr, pinky_pos/180*3.14)	

thumb_yaw_dof_ptr = dc.find_articulation_dof(art, "R_thumb_proximal_yaw_joint")
dc.wake_up_articulation(art)
dc.set_dof_position_target(thumb_yaw_dof_ptr, thumb_yaw_pos/180*3.14)	

thumb_pitch_dof_ptr = dc.find_articulation_dof(art, "R_thumb_proximal_pitch_joint")
dc.wake_up_articulation(art)
dc.set_dof_position_target(thumb_pitch_dof_ptr, thumb_pitch_pos/180*3.14)	

arm_joint1 = dc.find_articulation_dof(art, "joint1")
dc.wake_up_articulation(art)
dc.set_dof_position_target(arm_joint1, joint1_pos/180*3.14)	

arm_joint2 = dc.find_articulation_dof(art, "joint2")
dc.wake_up_articulation(art)
dc.set_dof_position_target(arm_joint2, joint2_pos/180*3.14)	

arm_joint3 = dc.find_articulation_dof(art, "joint3")
dc.wake_up_articulation(art)
dc.set_dof_position_target(arm_joint3, joint3_pos/180*3.14)	

arm_joint4 = dc.find_articulation_dof(art, "joint4")
dc.wake_up_articulation(art)
dc.set_dof_position_target(arm_joint4, joint4_pos/180*3.14)	

arm_joint5 = dc.find_articulation_dof(art, "joint5")
dc.wake_up_articulation(art)
dc.set_dof_position_target(arm_joint5, joint5_pos/180*3.14)	

arm_joint6 = dc.find_articulation_dof(art, "joint6")
dc.wake_up_articulation(art)
dc.set_dof_position_target(arm_joint6, joint6_pos/180*3.14)	

arm_joint7 = dc.find_articulation_dof(art, "joint7")
dc.wake_up_articulation(art)
dc.set_dof_position_target(arm_joint7, joint7_pos/180*3.14)	

# print dof state
dof_state = dc.get_dof_state(index_dof_ptr, _dynamic_control.STATE_ALL)
print(dof_state)