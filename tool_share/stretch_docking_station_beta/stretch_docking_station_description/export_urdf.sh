#!/bin/bash
echo "Copy the mesh files and the  URDF file to the exported URDF."
echo "cp ./meshes/* $HELLO_FLEET_PATH/$HELLO_FLEET_ID/exported_urdf"
cp ./meshes/* $HELLO_FLEET_PATH/$HELLO_FLEET_ID/exported_urdf/meshes/
echo "cp ./urdf/* $HELLO_FLEET_PATH/$HELLO_FLEET_ID/exported_urdf"
cp ./urdf/* $HELLO_FLEET_PATH/$HELLO_FLEET_ID/exported_urdf
echo ""
