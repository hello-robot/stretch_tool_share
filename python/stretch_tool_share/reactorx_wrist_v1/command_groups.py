from hello_helpers.simple_command_group import SimpleCommandGroup


class ReactorPitchCommandGroup(SimpleCommandGroup):
    def __init__(self, range_rad, robot=None):
        if (range_rad is None and robot is not None and robot.end_of_arm is not None
            and robot.end_of_arm.is_tool_present('ReactorWrist')
            and robot.end_of_arm.joints['reactor_wrist'].motors.get('reactor_pitch') is not None):
            range_ticks = robot.end_of_arm.motors['reactor_wrist'].params['range_t']
            range_rad = (robot.end_of_arm.motors['reactor_wrist'].ticks_to_world_rad(range_ticks[1]),
                         robot.end_of_arm.motors['reactor_wrist'].ticks_to_world_rad(range_ticks[0]))
        SimpleCommandGroup.__init__(self, 'joint_reactor_pitch', range_rad)

    def init_execution(self, robot, robot_status, **kwargs):
        if self.active:
            robot.end_of_arm.joints['reactor_wrist'].move_by('reactor_pitch',
                                     self.update_execution(robot_status)[1],
                                     v_r=self.goal['velocity'],
                                     a_r=self.goal['acceleration'])

    def update_execution(self, robot_status, **kwargs):
        self.error = None
        if self.active:
            self.error = self.goal['position'] - robot_status.end_of_arm.joints['reactor_wrist'].motors['reactor_pitch'].status['pos']
            return self.name, self.error

        return None

    def joint_state(self, robot_status, **kwargs):
        pitch_status = robot_status['end_of_arm']['reactor_wrist']
        return (pitch_status['pos'], pitch_status['vel'], pitch_status['effort'])


class ReactorRollCommandGroup(SimpleCommandGroup):
    def __init__(self, range_rad, robot=None):
        if (range_rad is None and robot is not None and robot.end_of_arm is not None
            and robot.end_of_arm.is_tool_present('ReactorWrist')
            and robot.end_of_arm.joints['reactor_wrist'].motors.get('reactor_roll') is not None):
            range_ticks = robot.end_of_arm.motors['reactor_wrist'].params['range_t']
            range_rad = (robot.end_of_arm.motors['reactor_wrist'].ticks_to_world_rad(range_ticks[1]),
                         robot.end_of_arm.motors['reactor_wrist'].ticks_to_world_rad(range_ticks[0]))
        SimpleCommandGroup.__init__(self, 'joint_reactor_roll', range_rad)

    def init_execution(self, robot, robot_status, **kwargs):
        if self.active:
            robot.end_of_arm.joints['reactor_wrist'].move_by('reactor_roll',
                                     self.update_execution(robot_status)[1],
                                     v_r=self.goal['velocity'],
                                     a_r=self.goal['acceleration'])

    def update_execution(self, robot_status, **kwargs):
        self.error = None
        if self.active:
            self.error = self.goal['position'] - robot_status.end_of_arm.joints['reactor_wrist'].motors['reactor_roll'].status['pos']
            return self.name, self.error

        return None

    def joint_state(self, robot_status, **kwargs):
        pitch_status = robot_status['end_of_arm']['reactor_wrist']
        return (pitch_status['pos'], pitch_status['vel'], pitch_status['effort'])


class ReactorGripperCommandGroup(SimpleCommandGroup):
    def __init__(self, range_rad, robot=None):
        if (range_rad is None and robot is not None and robot.end_of_arm is not None
            and robot.end_of_arm.is_tool_present('ReactorWrist')
            and robot.end_of_arm.joints['reactor_wrist'].motors.get('stretch_gripper') is not None):
            range_ticks = robot.end_of_arm.motors['reactor_wrist'].params['range_t']
            range_rad = (robot.end_of_arm.motors['reactor_wrist'].ticks_to_world_rad(range_ticks[1]),
                         robot.end_of_arm.motors['reactor_wrist'].ticks_to_world_rad(range_ticks[0]))
        SimpleCommandGroup.__init__(self, 'joint_reactor_gripper', range_rad)

    def init_execution(self, robot, robot_status, **kwargs):
        if self.active:
            robot.end_of_arm.joints['reactor_wrist'].move_by('reactor_gripper',
                                     self.update_execution(robot_status)[1],
                                     v_r=self.goal['velocity'],
                                     a_r=self.goal['acceleration'])

    def update_execution(self, robot_status, **kwargs):
        self.error = None
        if self.active:
            self.error = self.goal['position'] - robot_status.end_of_arm.joints['reactor_wrist'].motors['reactor_gripper'].status['pos']
            return self.name, self.error

        return None

    def joint_state(self, robot_status, **kwargs):
        pitch_status = robot_status['end_of_arm']['reactor_wrist']
        return (pitch_status['pos'], pitch_status['vel'], pitch_status['effort'])
