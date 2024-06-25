from omni.isaac.dynamic_control import _dynamic_control
dc = _dynamic_control.acquire_dynamic_control_interface()

art = dc.get_articulation("/World/R_inspire/R_inspire")

num_joints = dc.get_articulation_joint_count(art)
print(num_joints)

dof_ptr = dc.find_articulation_dof(art, "R_index_proximal_joint")

dof_state = dc.get_dof_state(dof_ptr, _dynamic_control.STATE_ALL)
print(dof_state)

dc.wake_up_articulation(art)
dc.set_dof_position_target(dof_ptr, 50/180*3.14)	

