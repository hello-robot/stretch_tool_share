params = {
    "tool_dexterous_wrist": {
        'py_class_name': 'ToolDexterousWrist',
        'py_module_name': 'stretch_tool_share.dexterous_wrist_vbeta.dexterous_wrist_tool',
        'baud': 57600,
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
                'py_module_name': 'stretch_tool_share.dexterous_wrist_vbeta.wrist_pitch',
                'ros_py_class_name': 'WristPitchCommandGroup',
                'ros_py_module_name': 'stretch_tool_share.dexterous_wrist_vbeta.dexterous_command_group'
            },
            'wrist_roll': {
                'py_class_name': 'WristRoll',
                'py_module_name': 'stretch_tool_share.dexterous_wrist_vbeta.wrist_roll',
                'ros_py_class_name': 'WristRollCommandGroup',
                'ros_py_module_name': 'stretch_tool_share.dexterous_wrist_vbeta.dexterous_command_group'
            },
            'wrist_yaw': {
                'py_class_name': 'WristYaw',
                'py_module_name': 'stretch_body.wrist_yaw',
            },
        },
        'collision_models': ['collision_tool_dexterous_wrist']
    },
    "collision_tool_dexterous_wrist": {
        'arm_palm_beyond_base': 0.07,
        'enabled': 1,
        'lift_fingertip_above_base': 0.2,
        'lift_palm_above_base': 0.085,
        'py_class_name': 'CollisionToolDexterousWrist',
        'py_module_name': 'stretch_tool_share.beta_dexterous_wrist_vbeta.collision_model',
        'r_gripper_tips': 0.24,
        'r_puller': 0.08
    },
    "wrist_pitch": {
        'flip_encoder_polarity': 1,
        'gr': 2.4,
        'id': 13,
        'max_voltage_limit': 15,
        'min_voltage_limit': 11,
        'motion': {
            'default': {'accel': 8.0, 'vel': 3.0},
            'fast': {'accel': 10.0, 'vel': 5.0},
            'max': {'accel': 12, 'vel': 8},
            'slow': {'accel': 4.0, 'vel': 1.0}
        },
        'pid': [640, 0, 0],
        'pwm_homing': [-300, 300],
        'pwm_limit': 885,
        'range_t': [0, 9340],
        'req_calibration': 1,
        'return_delay_time': 0,
        'stall_backoff': 0.017,
        'stall_max_effort': 20.0,
        'stall_max_time': 1.0,
        'stall_min_vel': 0.1,
        'temperature_limit': 72,
        'usb_name': '/dev/hello-dynamixel-wrist',
        'use_multiturn': 1,
        'zero_t': 7175
    },
    "wrist_roll": {
        'flip_encoder_polarity': 1,
        'gr': 2.4,
        'id': 13,
        'max_voltage_limit': 15,
        'min_voltage_limit': 11,
        'motion': {
            'default': {'accel': 8.0, 'vel': 3.0},
            'fast': {'accel': 10.0, 'vel': 5.0},
            'max': {'accel': 12, 'vel': 8},
            'slow': {'accel': 4.0, 'vel': 1.0}
        },
        'pid': [640, 0, 0],
        'pwm_homing': [-300, 300],
        'pwm_limit': 885,
        'range_t': [0, 9340],
        'req_calibration': 1,
        'return_delay_time': 0,
        'stall_backoff': 0.017,
        'stall_max_effort': 20.0,
        'stall_max_time': 1.0,
        'stall_min_vel': 0.1,
        'temperature_limit': 72,
        'usb_name': '/dev/hello-dynamixel-wrist',
        'use_multiturn': 1,
        'zero_t': 7175
    }
}
