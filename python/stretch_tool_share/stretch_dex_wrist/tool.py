from stretch_body.end_of_arm import EndOfArm


class ToolStretchDexWrist(EndOfArm):
    def __init__(self, name='tool_stretch_dex_wrist'):
        print('stretch_tool_share.tool.ToolStretchDexWrist is now deprecated')
        print('See PR https://github.com/hello-robot/stretch_tool_share/pull/20')
        return
        # EndOfArm.__init__(self, name)

    def stow(self):
        # Fold in wrist and gripper
        print('--------- Stowing ToolStretchDexWrist ----')
        self.move_to('wrist_pitch', self.params['stow']['wrist_pitch'])
        self.move_to('wrist_roll', self.params['stow']['wrist_roll'])
        self.move_to('wrist_yaw', self.params['stow']['wrist_yaw'])
        self.move_to('stretch_gripper', self.params['stow']['stretch_gripper'])

    def home(self):
        self.motors['stretch_gripper'].home()
        self.motors['wrist_pitch'].move_to(0)
        self.motors['wrist_roll'].move_to(0)
        self.motors['wrist_yaw'].home()
