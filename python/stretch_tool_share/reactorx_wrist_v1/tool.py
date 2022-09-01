from stretch_body.end_of_arm import EndOfArm


class ToolReactorWrist(EndOfArm):
    def __init__(self, name='tool_reactor_wrist'):
        EndOfArm.__init__(self, name)

    def stow(self):
        # Fold in wrist and gripper
        print('--------- Stowing ToolReactorWrist ----')
        self.move_to('wrist_pitch', self.params['stow']['wrist_pitch'])
        self.move_to('wrist_roll', self.params['stow']['wrist_roll'])
        self.move_to('wrist_yaw', self.params['stow']['wrist_yaw'])
        self.move_to('reactor_gripper', self.params['stow']['reactor_gripper'])

    def home(self):
        #self.motors['reactor_gripper'].home()
        self.motors['reactor_gripper'].move_to(0)
        self.motors['wrist_pitch'].move_to(0)
        self.motors['wrist_roll'].move_to(0)
        self.motors['wrist_yaw'].home()
