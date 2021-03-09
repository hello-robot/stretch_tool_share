#! /usr/bin/env python

from stretch_body.robot_collision import *
from stretch_body.hello_utils import *


# #############################################
class CollisionStretchDexWristToBase(RobotCollisionModel):
    """
    Manage collisions of the standard Stretch Gripper tool with the
    ground and the base
    """

    def __init__(self, collision_manager):
        RobotCollisionModel.__init__(self, collision_manager, 'collision_stretch_dex_wrist_to_base')

    def step(self, status):
        return { 'lift':[None, None], 'arm':[None, None], 'wrist_yaw':[None, None],'wrist_pitch':[None, None],'wrist_roll':[None, None]}

class CollisionStretchDexWristToSelf(RobotCollisionModel):
    """
    Manage collisions of the standard Stretch Gripper tool with the
    ground and the base
    """

    def __init__(self, collision_manager):
        RobotCollisionModel.__init__(self, collision_manager, 'collision_stretch_dex_wrist_to_self')

    def step(self, status):
        x_roll=status['end_of_arm']['wrist_roll']['pos']
        x_pitch = status['end_of_arm']['wrist_pitch']['pos']
        x_yaw = status['end_of_arm']['wrist_yaw']['pos']

        if x_pitch<self.params['pitch_up_thresh']:
            if x_roll<=deg_to_rad(-135) or x_roll>=deg_to_rad(135): #Servo body up
                workspace='limit_pitch_up_palm_up'
            if (x_roll<=deg_to_rad(135) and x_roll>=deg_to_rad(45)) or (x_roll>=deg_to_rad(-135) and x_roll<=deg_to_rad(-45)): #Servo body sideqays
                workspace='limit_pitch_up_palm_side'
            if x_roll<=deg_to_rad(45) and x_roll>=deg_to_rad(-45): #Servo body down
                workspace='limit_pitch_up_palm_down'
            w={ 'wrist_yaw':self.params[workspace]['yaw'],'wrist_pitch':self.params[workspace]['pitch'],'wrist_roll':[None, None]}
            return w
        else:
            return  {'wrist_yaw':[None,None],'wrist_pitch':[None,None],'wrist_roll':[None, None]}

class CollisionStretchDexWristToSelf(RobotCollisionModel):
    """
    Manage collisions of the standard Stretch Gripper tool with the
    ground and the base
    """

    def __init__(self, collision_manager):
        RobotCollisionModel.__init__(self, collision_manager, 'collision_stretch_dex_wrist_to_self')
        self.fk=EndOfArmForwardKinematics()

    def step(self, status):
        x_roll = status['end_of_arm']['wrist_roll']['pos']
        x_pitch = status['end_of_arm']['wrist_pitch']['pos']
        x_yaw = status['end_of_arm']['wrist_yaw']['pos']

        cfg = {
            'joint_wrist_yaw': x_yaw,
            'joint_wrist_pitch': x_pitch,
            'joint_wrist_roll': x_roll,
            'joint_gripper_finger_left':0.0
        }
        pose = self.fk.tool_fk(cfg, 'link_gripper_fingertip_left')
        tx = pose[0][3]  # Forward
        ty = pose[1][3]  # Height
        tz = pose[2][3]  # Extension direction
        #print('------')
        #print('Forward', tx)
        #print('Height' ,ty)
        #print('Extension', tz)

        w=  {'wrist_yaw':[None,None],'wrist_pitch':[None,None],'wrist_roll':[None, None]}

        return w
