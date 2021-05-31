from stretch_body.wrist_yaw import WristYaw
from stretch_body.hello_utils import *


class OffsetWristYaw(WristYaw):
    """
    API to the Stretch RE1 wrist yaw joint with an artificial 90 degree offset
    """
    def __init__(self, chain=None):
        WristYaw.__init__(self, chain)


    def home(self):
        """
        Home to hardstops
        """
        WristYaw.home(self, single_stop=True, move_to_zero=False)
        self.move_to(deg_to_rad(90.0))
        self.push_command()

