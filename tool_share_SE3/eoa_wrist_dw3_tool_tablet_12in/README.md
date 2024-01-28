To install:

Add the following to your user yaml:


robot:
  tool: eoa_wrist_dw3_tool_tablet_12in

params:
  - stretch_tool_share_se3.eoa_wrist_dw3_tool_tablet_12in.params



Copy mesh and xacro data to ~/repos/stretch_urdf/stretch_urdf/<ROBOT_MODEL>

Make a new top level xacro under stretch_urdf, eg:

stretch_description_SE3_eoa_wrist_dw3_tool_tablet_12in.xacro

<?xml version="1.0"?>
<robot xmlns:xacro="http://www.ros.org/wiki/xacro" name="stretch">

  <xacro:include filename="stretch_main.xacro" />
  <xacro:include filename="stretch_aruco.xacro" />
  <xacro:include filename="stretch_d435i.xacro" />
  <xacro:include filename="stretch_laser_range_finder.xacro" />
  <xacro:include filename="stretch_base_imu.xacro" />
  <xacro:include filename="stretch_respeaker.xacro" />
  <xacro:include filename="stretch_wrist_dw3.xacro" />
  <xacro:include filename="stretch_tool_tablet_12in.xacro" />
  <xacro:include filename="stretch_head_nav_cam.xacro" />
</robot>



Then run ~/repos/stretch_urdf/urdf_generate.py to create a new URDF that matches your tool
Then copy the URDF and meshes to 

pkg = str(importlib_resources.files("stretch_urdf"))  # .local/lib/python3.10/site-packages/stretch_urdf)

Then copy the URDF and meshes for ROS2...


Note: Need to copy mesh and urdf files to the PKG install place
 1298  cd ~/repos/stretch_tool_share/tool_share_SE3/eoa_wrist_dw3_tool_tablet_12in
 1300  cp meshes/*.STL ~/repos/stretch_urdf/stretch_urdf/SE3/meshes/
 1301  cp xacro/stretch_tool_tablet_12in.xacro ~/repos/stretch_urdf/stretch_urdf/SE3/xacro/

 cp stretch_urdf/SE3/*.urdf ~/.local/lib/python3.10/site-packages/stretch_urdf/SE3/
 1319  ./stretch_urdf/tools/stretch_urdf_viz.py 
 1320  cp stretch_urdf/SE3/meshes/*tablet* ~/.local/lib/python3.10/site-packages/stretch_urdf/SE3/meshes/
 1321  ./stretch_urdf/tools/stretch_urdf_viz.py 
 1322  ls
 1323  cd stretch_urdf/
 1324  pip3 install -e .
 1329  pip3 list | grep stretch

Verify that new tool shows up here
 1330  ./stretch_urdf/tools/stretch_urdf_viz.py 
