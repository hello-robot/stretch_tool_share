
from stretch_body.dynamixel_hello_XL430 import DynamixelHelloXL430
from stretch_body.hello_utils import *
from stretch_body.dynamixel_X_chain import DynamixelXChain

"""
To use this class, include in stretch_re1_user_params.yaml:

end_of_arm:
  devices:
    reactor_wrist: {py_class_name: ReactorWrist, py_module_name: reactor_wrist}
    
Ensure reactor_wrist.py is on the PYTHONPATH

Ensure that stretch_re1_tool_params.yaml include entries for:
-- reactor_gripper
-- reactor_pitch
-- reactor_roll

"""
class ReactorWrist(DynamixelXChain):
    def __init__(self):
        DynamixelXChain.__init__(self,'/dev/hello-dynamixel-wrist')
        pitch=DynamixelHelloXL430('reactor_pitch',self)
        self.add_motor(pitch)
        roll=DynamixelHelloXL430('reactor_roll',self)
        self.add_motor(roll)
        gripper = DynamixelHelloXL430('reactor_gripper', self)
        self.add_motor(gripper)
        self.poses = {'stow': [deg_to_rad(-90), deg_to_rad(0)],
                      'tool_ahead_0': [deg_to_rad(0), deg_to_rad(0)],
                      'tool_ahead_90': [deg_to_rad(0), deg_to_rad(90)],
                      'tool_ahead_-90': [deg_to_rad(0), deg_to_rad(-90)]}

    # ###################################################
    def move_to(self, joint, x_r, v_r=None, a_r=None):
        """
        joint: Name of the joint to move ('reactor_pitch' or 'reactor_roll' or 'reactor_gripper')
        x_r: commanded absolute position (radians).
        v_r: velocity for trapezoidal motion profile (rad/s).
        a_r: acceleration for trapezoidal motion profile (rad/s^2)
        """
        self.motors[joint].move_to(x_r,v_r,a_r)

    def move_by(self, joint,  x_r, v_r=None, a_r=None):
        """
        joint: Name of the joint to move ('reactor_pitch' or 'reactor_roll' or 'reactor_gripper')
        x_r: commanded incremental motion (radians).
        v_r: velocity for trapezoidal motion profile (rad/s).
        a_r: acceleration for trapezoidal motion profile (rad/s^2)
        """
        self.motors[joint].move_by(x_r,v_r,a_r)


    def pose(self, p):
        """
        p: Dictionary key to named pose (eg 'stow'). Doesn't do gripper.
        """
        self.move_to('reactor_pitch', self.poses[p][0])
        self.move_to('reactor_roll', self.poses[p][1])