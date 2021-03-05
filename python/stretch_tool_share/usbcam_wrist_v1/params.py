params = {
    "tool_usbcam_wrist": {
        'py_class_name': 'ToolUSBCamWrist',
        'py_module_name': 'stretch_tool_share.usbcam_wrist_v1.tool',
        'baud': 57600,
        'stow': {'offset_wrist_yaw': 3.4},
        'devices': {
            'offset_wrist_yaw': {
                'py_class_name': 'OffsetWristYaw',
                'py_module_name': 'stretch_tool_share.usbcam_wrist_v1.offset_wrist_yaw',
                'ros_py_class_name': 'OffsetWristYawCommandGroup',
                'ros_py_module_name': 'stretch_tool_share.usbcam_wrist_v1.command_groups'
            }
        }
    },
    "offset_wrist_yaw": {
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
