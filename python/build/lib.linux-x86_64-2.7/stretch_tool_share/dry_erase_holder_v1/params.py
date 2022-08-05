params = {
    "tool_dry_erase_holder_v1": {
        'py_class_name': 'ToolDryEraseHolderV1',
        'py_module_name': 'stretch_tool_share.dry_erase_holder_v1.tool',
        'use_group_sync_read': 1,
        'baud': 57600,
        'retry_on_comm_failure': 1,
        'dxl_latency_timer': 64,
        'verbose':0,
        'stow': {'wrist_yaw': 3.4},
        'devices': {
            'wrist_yaw': {
                'py_class_name': 'WristYaw',
                'py_module_name': 'stretch_body.wrist_yaw',
                'ros_py_class_name': 'WristYawCommandGroup',
                'ros_py_module_name': 'stretch_tool_share.dry_erase_holder_v1.command_groups'
            }
        }
    }
}
