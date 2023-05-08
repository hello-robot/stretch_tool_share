#! /usr/bin/env python

from stretch_body.robot_collision import *
from stretch_body.hello_utils import *
import math


class CollisionStretchDexWristToSelf(RobotCollisionModel):
    """
    NOTE: Experimental. You may want to turn this off in the params (enable=0)
    Manage collisions of the standard Stretch Gripper tool with the
    ground and the base
    """

    def __init__(self, collision_manager):
        RobotCollisionModel.__init__(self, collision_manager, 'collision_stretch_dex_wrist_to_self')

    def step(self, status):
        x_roll=status['end_of_arm']['wrist_roll']['pos']
        x_pitch = status['end_of_arm']['wrist_pitch']['pos']
        x_yaw = status['end_of_arm']['wrist_yaw']['pos']

        if x_pitch>self.params['pitch_up_thresh']:
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

class CollisionStretchDexWristToBase(RobotCollisionModel):
    """
    NOTE: Experimental. You may want to turn this off in the params (enable=0)
    Manage collisions of the standard Stretch Gripper tool with the
    ground and the base
    """

    def __init__(self, collision_manager):
        RobotCollisionModel.__init__(self, collision_manager, 'collision_stretch_dex_wrist_to_base')
        self.fk=EndOfArmForwardKinematics()

    def step(self, status):
        cfg = {
            'joint_wrist_yaw': status['end_of_arm']['wrist_yaw']['pos'],
            'joint_wrist_pitch': status['end_of_arm']['wrist_pitch']['pos'],
            'joint_wrist_roll': status['end_of_arm']['wrist_roll']['pos'],
            'joint_gripper_finger_left':0.0
        }
        pose = self.fk.tool_fk(cfg, 'link_gripper_fingertip_left')
        forward = pose[0][3]  # Forward, pos is towards wheels
        height = pose[1][3]  # Height , pos is up, pad out
        extension = pose[2][3]  # Extension, pos is reach
        if 0:
            print('------')
            print('Forward', forward)
            print('Height' ,height)
            print('Extension', extension)
            print('Lift',status['lift']['pos'])
            print('Arm', status['arm']['pos'])
            print("Wrist pitch",rad_to_deg(status['end_of_arm']['wrist_pitch']['pos']))


        wrist_yaw_fwd = deg_to_rad(90.0) #tool pointing to the front
        tool_clear_of_base = (status['end_of_arm']['wrist_yaw']['pos'] < wrist_yaw_fwd) and (status['arm']['pos'] > self.params['arm_clear_base'])
        tool_to_floor=max(0, status['lift']['pos']+self.params['base_to_floor_offset']+height)


        if tool_clear_of_base:
            lift_lower_limit = min(max(0,status['lift']['pos']-tool_to_floor), status['lift']['pos'])  # Only low it to reduce the ROM
        else:
            lift_lower_limit = min(max(self.params['palm_height'], -1*height), status['lift']['pos'])  # Only low it to reduce the ROM

        pitch_lower_limit = None
        if status['lift']['pos']>self.params['palm_height'] and status['lift']['pos']<self.params['lift_up']:
            if status['arm']['pos']<self.params['arm_clear_base']:
                q = -1*math.atan2(status['lift']['pos'],self.params['arm_clear_base'])  # How far pitch can fold back before hitting base
                pitch_lower_limit= min(status['end_of_arm']['wrist_pitch']['pos'],q)  # Only allow pitch to fold back further as lift raises, when lowering limit lift descent

        return {'lift': [lift_lower_limit, None], 'arm': [None, None], 'wrist_yaw': [None, None], 'wrist_pitch': [pitch_lower_limit, None], 'wrist_roll': [None, None]}



