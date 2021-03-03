from stretch_body.dynamixel_hello_XL430 import DynamixelHelloXL430
from stretch_body.hello_utils import *
import time
import logging

class OffsetWristYaw(DynamixelHelloXL430):
    """
    API to the Stretch RE1 wrist yaw joint with an artificial 90 degree offset
    """
    def __init__(self, chain=None):
        DynamixelHelloXL430.__init__(self, 'offset_wrist_yaw', chain)
        self.logger = logging.getLogger('robot.offset_wrist_yaw')
        self.poses = {'side': deg_to_rad(90.0), 'forward': deg_to_rad(0.0), 'stow': deg_to_rad(180.0)}
        self.sentry_active=False

    def home(self):
        """
        Home to hardstops
        """
        DynamixelHelloXL430.home(self, single_stop=True, move_to_zero=False)
        self.move_to(deg_to_rad(90.0))
        time.sleep(3.0) #extra time to get back
        # TODO: Doesn't create 90.0 offset as expected...
        # self.motor.disable_torque()
        # self.motor.zero_position(verbose=True)
        # self.motor.enable_torque()
        # self.motor.enable_pos()

    def pose(self,p,v_r=None,a_r=None):
        """
        p: Dictionary key to named pose (eg 'forward')
        v_r: velocityfor trapezoidal motion profile (rad/s).
        a_r: acceleration for trapezoidal motion profile (rad/s^2)
        """
        self.move_to(self.poses[p],v_r,a_r)

    def step_sentry(self):
        """
        This sentry attempts to prevent the wrist yaw servo from overheating
        if it is pushing against an object for too long
        It works by backing off the commanded position from the current position
        so as to lower the steady state error of the PID controller
        """
        if self.status['stall_overload']:
            if self.status['effort']>0:
                self.move_by(self.params['stall_backoff'])
                self.logger.info('Backoff at stall overload')
            else:
                self.move_by(-1*self.params['stall_backoff'])
                self.logger.info('Backoff at stall overload')
