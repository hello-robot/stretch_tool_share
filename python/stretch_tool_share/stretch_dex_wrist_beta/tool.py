from stretch_body.end_of_arm import EndOfArm


class ToolStretchDexWrist(EndOfArm):
    def __init__(self):
        EndOfArm.__init__(self)
        self.name = 'tool_stretch_dex_wrist' #override default name
        self.joints = []
        self.motors = {}
        self.add_joints(self.robot_params[self.name])
        self.overwrite_params(self.params,self.robot_params[self.name])
    def stow(self):
        # Fold in wrist and gripper
        print '--------- Stowing ToolStretchDexWrist ----'
        self.move_to('wrist_pitch', self.params['stow']['wrist_pitch'])
        self.move_to('wrist_roll', self.params['stow']['wrist_roll'])
        self.move_to('wrist_yaw', self.params['stow']['wrist_yaw'])
        self.move_to('stretch_gripper', self.params['stow']['stretch_gripper'])
    def home(self):
        self.motors['stretch_gripper'].home()
        if self.motors['wrist_pitch'].status['pos']<0:
            self.motors['wrist_pitch'].move_to(0)
        self.motors['wrist_yaw'].home()