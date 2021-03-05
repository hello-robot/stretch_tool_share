from stretch_body.end_of_arm import EndOfArm

class ToolReactorWrist(EndOfArm):
    def __init__(self):
        EndOfArm.__init__(self)
        self.name = 'tool_reactor_wrist' #override default name
        self.joints = []
        self.motors = {}
        self.add_joints(self.robot_params[self.name])
        self.overwrite_params(self.params,self.robot_params[self.name])

    def stow(self):
        # Fold in wrist and gripper
        print('--------- Stowing Wrist Yaw ----')
        self.move_to('wrist_yaw', self.params['stow']['wrist_yaw'])
        print('--------- Stowing Reactor ----')
        self.motors['reactor_wrist'].pose('stow')
