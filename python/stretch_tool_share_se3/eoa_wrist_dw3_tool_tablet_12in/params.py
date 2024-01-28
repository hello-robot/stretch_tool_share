
params = {
    "eoa_wrist_dw3_tool_tablet_12in": {
        'py_class_name': 'EOA_Wrist_DW3_Tool_Tablet_12in',
        'py_module_name': 'stretch_tool_share_se3.eoa_wrist_dw3_tool_tablet_12in.tool',
        'use_group_sync_read': 1,
        'retry_on_comm_failure': 1,
        'baud': 115200,
        'dxl_latency_timer': 64,
        'stow': {
            'arm': 0.0,
            'lift': 0.3,
            'wrist_pitch': -0.52,
            'wrist_roll': 0.0,
            'wrist_yaw': 3.0
        },
        'collision_mgmt': {
            'k_brake_distance': {'wrist_pitch': 0.25, 'wrist_yaw': 0.25, 'wrist_roll': 0.25},
            'collision_pairs': {
                'link_wrist_pitch_TO_base_link': {'link_pts': 'link_wrist_pitch', 'link_cube': 'base_link',
                                                  'detect_as': 'pts'},
                'link_wrist_yaw_bottom_TO_base_link': {'link_pts': 'link_wrist_yaw_bottom', 'link_cube': 'base_link',
                                                       'detect_as': 'pts'}},
            'joints': {'lift': [{'motion_dir': 'neg', 'collision_pair': 'link_wrist_pitch_TO_base_link'},
                                {'motion_dir': 'neg', 'collision_pair': 'link_wrist_yaw_bottom_TO_base_link'}],
                       'wrist_pitch': [],
                       'wrist_roll': [],
                       'wrist_yaw': []}},

        'devices': {
            'wrist_pitch': {
                'py_class_name': 'WristPitch',
                'py_module_name': 'stretch_body.wrist_pitch'
            },
            'wrist_roll': {
                'py_class_name': 'WristRoll',
                'py_module_name': 'stretch_body.wrist_roll'
            },
            'wrist_yaw': {
                'py_class_name': 'WristYaw',
                'py_module_name': 'stretch_body.wrist_yaw'
            }
        }}
}
