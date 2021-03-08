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
        ww={
            'pitch_up_thresh':-0.1,
            'limit_pitch_up_palm_down': {'pitch': [-0.45, None], 'yaw': [-0.50, 3.14]},
            'limit_pitch_up_palm_side': {'pitch': [-0.45, None], 'yaw': [-0.50, 3.14]},
            'limit_pitch_up_palm_up': {'pitch': [0, None], 'yaw': [None, 3.14]},
            'py_class_name': 'CollisionStretchDexWristToSelf',
            'py_module_name': 'stretch_tool_share.stretch_dex_wrist_beta.collision_model',
        }
        x_roll=status['end_of_arm']['wrist_roll']['pos']
        x_pitch = status['end_of_arm']['wrist_pitch']['pos']
        x_yaw = status['end_of_arm']['wrist_yaw']['pos']

        if x_pitch<ww['pitch_up_thresh']:
            if x_roll<=deg_to_rad(-135) or x_roll>=deg_to_rad(135): #Servo body up
                workspace='limit_pitch_up_palm_up'
            if (x_roll<=deg_to_rad(135) and x_roll>=deg_to_rad(45)) or (x_roll>=deg_to_rad(-135) and x_roll<=deg_to_rad(-45)): #Servo body sideqays
                workspace='limit_pitch_up_palm_side'
            if x_roll<=deg_to_rad(45) and x_roll>=deg_to_rad(-45): #Servo body down
                workspace='limit_pitch_up_palm_down'
            #print('----------------------------')
            #print('Roll %f'%x_roll)
            #print('Pitch %f' % x_pitch)
            #print('Yaw %f' % x_yaw)

            #print('Workspace %s'%workspace)

            w={ 'wrist_yaw':ww[workspace]['yaw'],'wrist_pitch':ww[workspace]['pitch'],'wrist_roll':[None, None]}
            #print('Yaw',w['wrist_yaw'])
            #print('Pitch',w['wrist_pitch'])
            #print self.collision_manager.robot.end_of_arm.motors['wrist_pitch'].soft_motion_limits
        #print('Yaw limit %f to %f'%(rad_to_deg(w['wrist_yaw'][0]), rad_to_deg(w['wrist_yaw'][1])))
        #print('Pitch limit %f to %f' % (rad_to_deg(w['wrist_pitch'][0]), rad_to_deg(w['wrist_pitch'][1])))
            return w
        else:
            return  {'wrist_yaw':[None,None],'wrist_pitch':[None,None],'wrist_roll':[None, None]}