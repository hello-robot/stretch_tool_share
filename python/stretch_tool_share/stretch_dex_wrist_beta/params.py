


params = {
    'robot_sentry': {
        'wrist_pitch_overload': 1,
        'wrist_roll_overload': 1},
    "tool_stretch_dex_wrist": {
        'py_class_name': 'ToolStretchDexWrist',
        'py_module_name': 'stretch_tool_share.stretch_dex_wrist_beta.tool',
        'use_group_sync_read': 1,
        'retry_on_comm_failure': 1,
        'baud':115200,
        'dxl_latency_timer': 64,
        'verbose':0,
        'stow': {
            'arm': 0.0,
            'lift': 0.38,
            'stretch_gripper': 0.0,
            'wrist_pitch': -1.57,
            'wrist_roll': 0.0,
            'wrist_yaw': 0.0
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
        'collision_models': ['collision_stretch_dex_wrist_to_self','collision_stretch_dex_wrist_to_base']
    },
    "collision_stretch_dex_wrist_to_base": {
        'enabled': 1,
        'py_class_name': 'CollisionStretchDexWristToBase',
        'py_module_name': 'stretch_tool_share.stretch_dex_wrist_beta.collision_model',
        'palm_height':0.12,
        'arm_clear_base':0.086,
        'base_to_floor_offset':0.16,
        'lift_up':0.37
    },
    "collision_stretch_dex_wrist_to_self": {
        'enabled': 1,
        'pitch_up_thresh': 0.1,
        'limit_pitch_up_palm_down': {'pitch': [None, 0.45], 'yaw': [-0.50, 3.14]},
        'limit_pitch_up_palm_side': {'pitch': [None, 0.45], 'yaw': [-0.50, 3.14]},
        'limit_pitch_up_palm_up': {'pitch': [None, 0], 'yaw': [None, 3.14]},
        'py_class_name': 'CollisionStretchDexWristToSelf',
        'py_module_name': 'stretch_tool_share.stretch_dex_wrist_beta.collision_model',
    },
    "wrist_pitch": {
        'flip_encoder_polarity': 1,
        'enable_runstop': 1,
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
        'retry_on_comm_failure':1,
        'verbose': 0
    },
    "wrist_roll": {
        'flip_encoder_polarity': 0,
        'enable_runstop': 1,
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
        'retry_on_comm_failure': 1,
        'verbose': 0
    }
}
