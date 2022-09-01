from stretch_body.dynamixel_hello_XL430 import DynamixelHelloXL430
import stretch_body.hello_utils as hu


class ReactorGripper(DynamixelHelloXL430):
    """
    API to the Stretch RE1 wrist pitch joint
    """
    def __init__(self, chain=None):
        DynamixelHelloXL430.__init__(self,'reactor_gripper',chain)
        self.poses = {'open': hu.deg_to_rad(90.0), 'zero': hu.deg_to_rad(0.0), 'close': hu.deg_to_rad(-90.0)}

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


