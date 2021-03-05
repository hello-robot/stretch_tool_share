from hello_helpers.simple_command_group import SimpleCommandGroup


class OffsetWristYawCommandGroup(SimpleCommandGroup):
    def __init__(self, range_rad, robot=None):
        if (range_rad is None and robot is not None and robot.end_of_arm is not None
            and robot.end_of_arm.is_tool_present('OffsetWristYaw')):
            range_ticks = robot.end_of_arm.motors['offset_wrist_yaw'].params['range_t']
            range_rad = (robot.end_of_arm.motors['offset_wrist_yaw'].ticks_to_world_rad(range_ticks[1]),
                         robot.end_of_arm.motors['offset_wrist_yaw'].ticks_to_world_rad(range_ticks[0]))
        SimpleCommandGroup.__init__(self, 'joint_offset_wrist_yaw', range_rad)

    def init_execution(self, robot, robot_status, **kwargs):
        if self.active:
            robot.end_of_arm.move_by('offset_wrist_yaw',
                                     self.update_execution(robot_status)[1],
                                     v_r=self.goal['velocity'],
                                     a_r=self.goal['acceleration'])

    def update_execution(self, robot_status, **kwargs):
        self.error = None
        if self.active:
            self.error = self.goal['position'] - robot_status['end_of_arm']['offset_wrist_yaw']['pos']
            return self.name, self.error

        return None

    def joint_state(self, robot_status, **kwargs):
        yaw_status = robot_status['end_of_arm']['offset_wrist_yaw']
        return (yaw_status['pos'], yaw_status['vel'], yaw_status['effort'])
