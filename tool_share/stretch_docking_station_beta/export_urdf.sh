#!/bin/bash
echo "Copy the mesh files and the  URDF file to the exported URDF."
echo "cp ./stretch_docking_station_description/meshes/* $HELLO_FLEET_PATH/$HELLO_FLEET_ID/exported_urdf"
cp ./stretch_docking_station_description/meshes/* $HELLO_FLEET_PATH/$HELLO_FLEET_ID/exported_urdf/meshes/
echo "cp ./stretch_docking_station_description/urdf/* $HELLO_FLEET_PATH/$HELLO_FLEET_ID/exported_urdf"
cp ./stretch_docking_station_description/urdf/* $HELLO_FLEET_PATH/$HELLO_FLEET_ID/exported_urdf
echo ""
