To install:

Add the following to your user yaml:


robot:
  tool: eoa_wrist_dw3_tool_tablet_12in

params:
  - stretch_tool_share_se3.eoa_wrist_dw3_tool_tablet_12in.params



Copy mesh and xacro data to ~/repos/stretch_urdf/stretch_urdf/<ROBOT_MODEL>
Then run ~/repos/stretch_urdf/urdf_generate.py to create a new URDF that matches your tool
Then copy the URDF and meshes to 

pkg = str(importlib_resources.files("stretch_urdf"))  # .local/lib/python3.10/site-packages/stretch_urdf)

Then copy the URDF and meshes for ROS2...