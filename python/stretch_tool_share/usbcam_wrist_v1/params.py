params = {
    "tool_usbcam_wrist": {
        'py_class_name': 'ToolUSBCamWrist',
        'py_module_name': 'stretch_tool_share.usbcam_wrist_v1.tool',
        'use_group_sync_read': 1,
        'baud': 57600,
        'dxl_latency_timer': 64,
        'retry_on_comm_failure': 1,
        'verbose':0,
        'stow': {'wrist_yaw': 3.4},
        'devices': {
            'wrist_yaw': {
                'py_class_name': 'OffsetWristYaw',
                'py_module_name': 'stretch_tool_share.usbcam_wrist_v1.offset_wrist_yaw',
                'ros_py_class_name': 'OffsetWristYawCommandGroup',
                'ros_py_module_name': 'stretch_tool_share.usbcam_wrist_v1.command_groups'
            }
        }
    }
}
