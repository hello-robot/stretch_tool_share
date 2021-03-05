


params = {
    "tool_stretch_dex_wrist": {
        'py_class_name': 'ToolStretchDexWrist',
        'py_module_name': 'stretch_tool_share.stretch_dex_wrist_beta.tool',
        'baud': 115200,
        'stow': {
            'arm': 0.0,
            'lift': 0.5,
            'stretch_gripper': 0.0,
            'wrist_pitch': 0.0,
            'wrist_roll': 0.0,
            'wrist_yaw': 3.4
        },
        'devices': {
            'stretch_gripper': {
                'py_class_name': 'StretchGripper',
                'py_module_name': 'stretch_body.stretch_gripper',
            },
            'wrist_pitch': {
                'py_class_name': 'WristPitch',
                'py_module_name': 'stretch_tool_share.stretch_dex_wrist_beta.wrist_pitch',
                'ros_py_class_name': 'WristPitchCommandGroup',
                'ros_py_module_name': 'stretch_tool_share.stretch_dex_wrist_beta.command_groups'
            },
            'wrist_roll': {
                'py_class_name': 'WristRoll',
                'py_module_name': 'stretch_tool_share.stretch_dex_wrist_beta.wrist_roll',
                'ros_py_class_name': 'WristRollCommandGroup',
                'ros_py_module_name': 'stretch_tool_share.stretch_dex_wrist_beta.command_groups'
            },
            'wrist_yaw': {
                'py_class_name': 'WristYaw',
                'py_module_name': 'stretch_body.wrist_yaw',
            },
        },
        'collision_models': ['collision_stretch_dex_wrist']
    },
    "collision_stretch_dex_wrist": {
        'arm_palm_beyond_base': 0.07,
        'enabled': 1,
        'lift_fingertip_above_base': 0.2,
        'lift_palm_above_base': 0.085,
        'py_class_name': 'CollisionStretchDexWrist',
        'py_module_name': 'stretch_tool_share.stretch_dex_wrist_beta.collision_model',
        'r_gripper_tips': 0.24,
        'r_puller': 0.08
    },
    "wrist_pitch": {
        'flip_encoder_polarity': 0,
        'gr': 1.0,
        'id': 15,
        'max_voltage_limit': 15,
        'min_voltage_limit': 11,
        'motion': {
            'default': {'accel': 8.0, 'vel': 3.0},
            'fast': {'accel': 10.0, 'vel': 5.0},
            'max': {'accel': 12, 'vel': 8},
            'slow': {'accel': 4.0, 'vel': 1.0}
        },
        'pid': [400, 0, 200],
        'pwm_homing': [0, 0],
        'pwm_limit': 885,
        'range_t': [650, 2048],
        'req_calibration': 0,
        'return_delay_time': 0,
        'stall_backoff': 0.017,
        'stall_max_effort': 10.0,
        'stall_max_time': 1.0,
        'stall_min_vel': 0.1,
        'temperature_limit': 72,
        'usb_name': '/dev/hello-dynamixel-wrist',
        'use_multiturn': 0,
        'zero_t': 1024,
        'baud':115200,
        'retry_on_comm_failure':1
    },
    "wrist_roll": {
        'flip_encoder_polarity': 0,
        'gr': 1.0,
        'id': 16,
        'max_voltage_limit': 16,
        'min_voltage_limit': 9,
        'motion': {
            'default': {'accel': 8.0, 'vel': 3.0},
            'fast': {'accel': 10.0, 'vel': 5.0},
            'max': {'accel': 12, 'vel': 8},
            'slow': {'accel': 4.0, 'vel': 1.0}
        },
        'pid': [800, 0, 0],
        'pwm_homing': [0, 0],
        'pwm_limit': 885,
        'range_t': [0, 4095],
        'req_calibration': 0,
        'return_delay_time': 0,
        'stall_backoff': 0.017,
        'stall_max_effort': 10.0,
        'stall_max_time': 1.0,
        'stall_min_vel': 0.1,
        'temperature_limit': 80,
        'usb_name': '/dev/hello-dynamixel-wrist',
        'use_multiturn': 0,
        'zero_t': 2048,
        'baud': 115200,
        'retry_on_comm_failure': 1
    }
}
