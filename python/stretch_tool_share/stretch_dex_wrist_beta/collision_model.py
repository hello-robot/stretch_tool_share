#! /usr/bin/env python

from stretch_body.robot_collision import *
from stretch_body.hello_utils import *


# #############################################
class CollisionStretchDexWrist(RobotCollisionModel):
    """
    Manage collisions of the standard Stretch Gripper tool with the
    ground and the base
    """

    def __init__(self, collision_manager):
        RobotCollisionModel.__init__(self, collision_manager, 'collision_stretch_dex_wrist')

    def step(self, status):
        wrist_yaw_limit = [None, None]
        wrist_pitch_limit = [None,None]
        wrist_roll_limit = [None, None]
        arm_limit=[None,None]
        lift_limit=[None,None]
        w={ 'lift':lift_limit, 'arm':arm_limit, 'wrist_yaw':wrist_yaw_limit,'wrist_pitch':wrist_pitch_limit,'wrist_roll':wrist_roll_limit}

        return w