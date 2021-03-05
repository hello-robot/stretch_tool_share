from stretch_body.end_of_arm import EndOfArm


class ToolStretchDexWrist(EndOfArm):
    def __init__(self):
        EndOfArm.__init__(self)
        self.name = 'tool_stretch_dex_wrist' #override default name
        self.joints = []
        self.motors = {}
        self.add_joints(self.robot_params[self.name])
        self.overwrite_params(self.params,self.robot_params[self.name])
