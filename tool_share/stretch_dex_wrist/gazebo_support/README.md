![](../../../images/banner.png) 
## Stretch Dex Wrist - Gazebo Support
**Created by**: Hello Robot Inc

The Stretch RE1 robot with the Dex Wrist can also be simulated with [Gazebo](https://gazebosim.org/) simulator. The information on Stretch robot's Gazebo implementation can be found here [stretch_gazebo](https://github.com/hello-robot/stretch_ros/tree/master/stretch_gazebo).

To add the Dex Wrist to Stretch with Gazebo support:
```bash
cd ~/catkin_ws/src/stretch_ros/
git pull

cd ~/repos
git clone https://github.com/hello-robot/stretch_tool_share

cd stretch_tool_share/tool_share/stretch_dex_wrist
cp stretch_description/urdf/stretch_dex_wrist.xacro ~/catkin_ws/src/stretch_ros/stretch_description/urdf
cp stretch_description/urdf/stretch_description.xacro ~/catkin_ws/src/stretch_ros/stretch_description/urdf
cp stretch_description/meshes/*.STL ~/catkin_ws/src/stretch_ros/stretch_description/meshes

cp gazebo_support/stretch_gazebo.urdf.xacro ~/catkin_ws/src/stretch_ros/stretch_gazebo/urdf
cp gazebo_support/dex_wrist.yaml ~/catkin_ws/src/stretch_ros/stretch_gazebo/config
cp gazebo_support/cp gazebo.launch ~/catkin_ws/src/stretch_ros/stretch_gazebo/launch
```
During the Gazebo simulation with Dex Wrist, the wrist's Roll and Pitch can be controlled using the spawned "stretch_dex_wrist_controller" of type [position_controllers/JointTrajectoryController](http://wiki.ros.org/joint_trajectory_controller) 

**Note**: Still there is no planned support to run MoveIt with Stretch Dex Wrist in Gazebo.