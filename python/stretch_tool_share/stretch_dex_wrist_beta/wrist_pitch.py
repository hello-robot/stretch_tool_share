from stretch_body.dynamixel_hello_XL430 import DynamixelHelloXL430
from stretch_body.hello_utils import *
import logging

class WristPitch(DynamixelHelloXL430):
    """
    API to the Stretch RE1 wrist pitch joint
    """
    def __init__(self, chain=None):
        DynamixelHelloXL430.__init__(self,'wrist_pitch',chain)
        self.logger = logging.getLogger('robot.wrist_pitch')
        self.poses = {'up': deg_to_rad(56.0), 'forward': deg_to_rad(0.0), 'down': deg_to_rad(-90.0)}
        self.sentry_active=False

    def home(self):
        """
        Home to hardstops
        """
        pass

    def pose(self,p,v_r=None,a_r=None):
        """
        p: Dictionary key to named pose (eg 'forward')
        v_r: velocityfor trapezoidal motion profile (rad/s).
        a_r: acceleration for trapezoidal motion profile (rad/s^2)
        """
        self.move_to(self.poses[p],v_r,a_r)

    def step_sentry(self,robot):
        """
        This sentry attempts to prevent the wrist servo from overheating
        if it is pushing against an object for too long
        It works by backing off the commanded position from the current position
        so as to lower the steady state error of the PID controller
        """
        if self.robot_params['robot_sentry']['wrist_pitch_overload']:
            if self.status['stall_overload']:
                if self.status['effort']>0:
                    self.move_by(self.params['stall_backoff'])
                    self.logger.info('Backoff at stall overload')
                else:
                    self.move_by(-1*self.params['stall_backoff'])
                    self.logger.info('Backoff at stall overload')
