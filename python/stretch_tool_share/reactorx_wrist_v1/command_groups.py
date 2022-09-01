from hello_helpers.simple_command_group import SimpleCommandGroup



class WristPitchCommandGroup(SimpleCommandGroup):
    def __init__(self, range_rad=None, node=None):
        SimpleCommandGroup.__init__(self, 'joint_wrist_pitch', range_rad, node=node)

    def update_joint_range(self, joint_range, node=None):
        if joint_range is not None:
            self.range = joint_range
            return

        if node is None:
            return # cannot calculate range without Stretch Body handle
        range_ticks = node.robot.end_of_arm.motors['wrist_pitch'].params['range_t']
        range_rad = (node.robot.end_of_arm.motors['wrist_pitch'].ticks_to_world_rad(range_ticks[1]),
                     node.robot.end_of_arm.motors['wrist_pitch'].ticks_to_world_rad(range_ticks[0]))
        self.range = range_rad

    def init_execution(self, robot, robot_status, **kwargs):
        if self.active:
            robot.end_of_arm.move_by('wrist_pitch',
                                     self.update_execution(robot_status)[1],
                                     v_r=self.goal['velocity'],
                                     a_r=self.goal['acceleration'])

    def update_execution(self, robot_status, **kwargs):
        self.error = None
        if self.active:
            self.error = self.goal['position'] - robot_status['end_of_arm']['wrist_pitch']['pos']
            return self.name, self.error

        return None

    def joint_state(self, robot_status, **kwargs):
        pitch_status = robot_status['end_of_arm']['wrist_pitch']
        return (pitch_status['pos'], pitch_status['vel'], pitch_status['effort'])


class WristRollCommandGroup(SimpleCommandGroup):
    def __init__(self, range_rad=None, node=None):
        SimpleCommandGroup.__init__(self, 'joint_wrist_roll', range_rad, node=node)

    def update_joint_range(self, joint_range, node=None):
        if joint_range is not None:
            self.range = joint_range
            return

        if node is None:
            return # cannot calculate range without Stretch Body handle
        range_ticks = node.robot.end_of_arm.motors['wrist_roll'].params['range_t']
        range_rad = (node.robot.end_of_arm.motors['wrist_roll'].ticks_to_world_rad(range_ticks[0]),
                     node.robot.end_of_arm.motors['wrist_roll'].ticks_to_world_rad(range_ticks[1]))
        self.range = range_rad

    def init_execution(self, robot, robot_status, **kwargs):
        if self.active:
            robot.end_of_arm.move_by('wrist_roll',
                                     self.update_execution(robot_status)[1],
                                     v_r=self.goal['velocity'],
                                     a_r=self.goal['acceleration'])

    def update_execution(self, robot_status, **kwargs):
        self.error = None
        if self.active:
            self.error = self.goal['position'] - robot_status['end_of_arm']['wrist_roll']['pos']
            return self.name, self.error

        return None

    def joint_state(self, robot_status, **kwargs):
        roll_status = robot_status['end_of_arm']['wrist_roll']
        return (roll_status['pos'], roll_status['vel'], roll_status['effort'])



class ReactorGripperCommandGroup(SimpleCommandGroup):
    def __init__(self, range_rad=None, node=None):
        SimpleCommandGroup.__init__(self, 'joint_reactor_gripper', range_rad, node=node)

    def update_joint_range(self, joint_range, node=None):
        if joint_range is not None:
            self.range = joint_range
            return

        if node is None:
            return # cannot calculate range without Stretch Body handle
        range_ticks = node.robot.end_of_arm.motors['reactor_gripper'].params['range_t']
        range_rad = (node.robot.end_of_arm.motors['reactor_gripper'].ticks_to_world_rad(range_ticks[0]),
                     node.robot.end_of_arm.motors['reactor_gripper'].ticks_to_world_rad(range_ticks[1]))
        self.range = range_rad

    def init_execution(self, robot, robot_status, **kwargs):
        if self.active:
            robot.end_of_arm.move_by('reactor_gripper',
                                     self.update_execution(robot_status)[1],
                                     v_r=self.goal['velocity'],
                                     a_r=self.goal['acceleration'])

    def update_execution(self, robot_status, **kwargs):
        self.error = None
        if self.active:
            self.error = self.goal['position'] - robot_status['end_of_arm']['reactor_gripper']['pos']
            return self.name, self.error

        return None

    def joint_state(self, robot_status, **kwargs):
        roll_status = robot_status['end_of_arm']['reactor_gripper']
        return (roll_status['pos'], roll_status['vel'], roll_status['effort'])
