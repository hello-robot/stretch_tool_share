![image](https://github.com/hello-robot/stretch_tool_share/blob/feature/jetson_tutorials/images/banner.png)

## Nvidia Jetson Orin AGX Setup

**Created by**: Hello Robot Inc

What you will need to start with this is the Jetson Orin AGX Dev kit, as we know there are several ways to make the same thing, but the easiest way is to download the SDK Manager that Nvidia has, you can download it from [here](https://developer.nvidia.com/sdk-manager), also what you will need is a computer with Ubuntu 20.04 because with Ubuntu 22.04 the SDK Manager will not work, you can work with the 18.04 version if you want but we would recommend 20.04 so that you can have the latest version of drivers according to this information:

![image](https://github.com/hello-robot/stretch_tool_share/assets/141784078/d643a978-af3d-4d99-9537-7237489c8236)

Also if you want to follow the steps for the SDK Manager from the NVIDIA Documentation you can read it from [here](https://docs.nvidia.com/sdk-manager/index.html). And we will recommend you to put your Jetson in Force Recovery mode, if you don’t know how to do this for the Jetson AGX Orin you can see this [page](https://developer.nvidia.com/embedded/learn/jetson-agx-orin-devkit-user-guide/howto.html) or follow the next steps:

## Force Recovery Mode
**Note** 
If you want to be sure that the buttons you are pressing are the correct ones make sure to see the [Hardware Layout](https://developer.nvidia.com/embedded/learn/jetson-agx-orin-devkit-user-guide/developer_kit_layout.html) page.

To enter in the Force Recovery mode first make sure that the buttons are facing you, then you need to check the state of your Jetson, if it's power on follow the next steps:
1. Press and hold down the Force Recovery Button (**2 arrows/middle one**).
2. Press and hold down the reset button (**1 arrow/right one**).
3. Release both buttons.

If your Jetson is power off then there are other steps that you will need to do :
1. Press and hold down the Force Recovery Button (**2 arrows/middle one**).
2. Plug in a DC power supply's USB Type-C plug into the USB Type-C port ( **4** ) above the DC jack, or plug a DC plug of a power supply into DC jack ( **5** ).
3. If the white LED is not lit, press the Power button (**Power symbol/left one**).
4. Release both buttons.

Perfect, now with this your Jetson has entered in the Force Recovery Mode, you can go and watch the next tutorials!
## Jetson Tutorials
|  | Tutorial                                                                        | Description                                        |
|--|---------------------------------------------------------------------------------|----------------------------------------------------|
| 1 | [Jetson Initial Setup](jetson_inital_setup.md)                                           | Initial Setup for Jetson using SDK Manager|
| 2 | [Jetson Connection Via Headless Configuration](jetson_connection_headless_configuration.md)                  | Ways to connect your Jetson using only CLI. |
