# Jetson Initial Setup Tutorial
!!! warning
    This is only if you are flashing the Jetson for the first time, because every data that you have in here will be erased completely, this is only for the first time.

!!! note
    The connection between the Jetson and the robot computer is by micro usb.

## Step 1
To begin with this tutorial you must have installed the NVIDIA SDK Manager and also have your Jetson in Force Recovery Mode, if you haven't done that you can go and see the [README](https://github.com/hello-robot/stretch_tool_share/blob/feature/jetson_tutorials/tool_share/jetson_orin_agx_mount/tutorials/README.md) file and then come back.

## Step 2
Once the SDK Manager it’s installed and already running you’ll need to select the appropriate login tab.

<p align="center">
<img src="https://github.com/hello-robot/stretch_tool_share/assets/141784078/c7490785-72f7-4f96-b39f-5713e5898d33" alt="image" height="600" />
</p>

## Step 3
Once you log in it will show you the step by step tutorial that you need to follow, we recommend that you have the latest version of jetpack installed and it depends if you want to disable the Host Machine button or the Additional SDKS button, then click the continue button.
<p align="center">
<img src="https://github.com/hello-robot/stretch_tool_share/assets/141784078/767d3b73-b9e7-46aa-a4cc-0aa1c3209358" alt="image" height="600" />
</p>

## Step 4
Don’t worry if it doesn’t detect your board you can check that later in step 2-3 from the SDK Manager, in those steps you will select, download and install the components that you want to have for your Jetson, this will take around 20-40 minutes to download depending on your internet connection and around 40-45 minute to install all the components.
<p align="center">
<img src="https://github.com/hello-robot/stretch_tool_share/assets/141784078/b51eb61e-df02-428a-b5cd-d065948348e8" alt="image" height="600" />
</p>

## Step 5
During the process of the installation the SDK Manager will show you up a dialog when it's ready to flash your Jetson, you’ll need to select the appropriate board, in our case the Jetson AGX Orin, but if you have another one like the AGX Xavier like the image from below it’s also fine!
<p align="center">
<img src="https://github.com/hello-robot/stretch_tool_share/assets/141784078/c636c145-aa31-4280-a7bd-be1d93092255" alt="image" height="600" />
</p>

You can see that there are 2 options, the automatic setup or the manual setup, we would recommend to use the manual setup and configure by your own the OEM Configuration and the Storage Device, if you have your board connected but the SDK Manager doesn’t detect it, at least for the Jetson Orin AGX, click the refresh button but if this doesn’t work you can watch the troubleshooting section below.

Once you have done all of this and everything is installed then you are finished, you can start to configure the Jetson, with a monitor is easier! Now you can check how to run docker with ROS2 in your Jetson and start your own projects for deep learning. 

If you want tu **shutdown** your Jetson you could input the command `sudo shutdown -h now` in your Jetson terminal, also you can do it via GUI but sometimes the Jetson's fan may still be working, so to avoid this it's better to do it the CLI way.

# Troubleshooting
!!! note
    To check the hardware layout of the Jetson AGX Orin click [here](https://developer.nvidia.com/embedded/learn/jetson-agx-orin-devkit-user-guide/developer_kit_layout.html).

If the SDK Manager isn’t detecting your board, at least with the AGX Orin, you’ll need to do the following steps:
1. Be sure that your Jetson is in Force Recovery mode
2. To be sure open a terminal (Ctrl + Alt + T) and write down lsusb
3. To determine whether the Dev Kit is in recovery mode once you write the lsusb command you’ll need to see Bus <bbb> Device <ddd>: ID 0955: <nnnn> Nvidia Corp. Which <bbb> and <ddd> is any 3 digit number and <nnnn> it’s a four digit number that represents the type of your Jetson module, for more information read the [NVIDIA documentation](https://docs.nvidia.com/jetson/archives/r35.4.1/DeveloperGuide/text/IN/QuickStart.html) all the way down.
4. If your <nnnn> doesn’t match the correct module name with the Jetson AGX Orin, for example instead of 7023 is 7045, you’ll need to unplug the micro USB and press the Force Recovery Button ( **2** ) + Reset Button( **3** ), with this you’ll be able to enter the Force Recovery mode, and just in case keep pressing the Force Recovery button and then plug in the micro USB again.
5. Now check with the command lsusb and it should appear the correct <nnnn>, in the case of our Jetson AGX Orin it was 7023.
6. Now continue with the installation in your SDK Manager and you are good to go.
