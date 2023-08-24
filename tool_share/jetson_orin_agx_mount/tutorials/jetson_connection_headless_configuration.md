# Jetson Connection Via Headless Configuration
!note If you didn't configure your Jetson with the SDK Manager because of the Ubuntu versions then maybe this could be of great help for you.

As always there are several ways to enter your Jetson with only a terminal for the first one you can read it in the [documentation](https://developer.nvidia.com/embedded/learn/get-started-jetson-agx-orin-devkit) that NVIDIA has or read it below:

## Connecting via screen command
!note To check the hardware layout of the Jetson AGX Orin click [here](https://developer.nvidia.com/embedded/learn/jetson-agx-orin-devkit-user-guide/developer_kit_layout.html).
1. First you will need to connect in the USB micro-B port ( **9** ) the micro USB cable into one of Stretch's USB ports. If you want to connect an ethernet cable is completly optional.
2. Then connect the included power supply into the USB Type-C™ port above the DC jack ( **4** ).
3. Your developer kit should automatically power on, and the white LED near the power button will light. If not, press the Power button ( **1** ).
4. Wait up to 1 minute.
5. On your computer, use a serial terminal application to connect via host serial port to the developer kit

Now that you have done this steps it's time to connect to our Jetson, you can use a Windows, Mac or Linux computer for this, the next steps are going to be in Linux:

First you will need to locate the **tty** device in your terminal, to do this you can write down

```{.bash .shell-prompt}
dmesg | grep --color 'tty'
```

If you didn't have your Jetson connected with the micro usb you can connect it and try again and see what's different it should appear something like this:
```{.bash .shell-prompt}
[ xxxx.xxxxxx] cdc_acm 1-3.3.4:1.1: ttyACM3: USB ACM device
```

In case you want to check it better you can input the command
```{.bash .shell-prompt}
ls -l /dev/ttyACM3   # In our case was ACM3
```

And it should output the general information of the ttyACM3 device
```{.bash .shell-prompt}
crw-rw---- 1 root dialout 166, 3 Aug 24 10:42 /dev/ttyACM3
```

Now for the connection part, if you don't have installed the screen program in Linux you can install it writing down this in the terminal:
```{.bash .shell-prompt}
sudo apt-get install -y screen
```

Now with the device name discover in the previous step you can use it to input the screen command:
```{.bash .shell-prompt}
sudo screen /dev/ttyACM3 115200
```
And now in your terminal you will have to login in your ubuntu account that you have on the jetson.

<p align="center">
  <img src="https://github.com/hello-robot/stretch_tool_share/assets/141784078/21aaee55-eae1-48b4-9525-691c78f3a88b"/>
</p>

!note If you didn't configure your Jetson with the SDK Manager you can complete the CUI-based "Jetson Initial configuration" (oem-config) using your PC's keyboard. Read the NVIDIA [documentation](https://developer.nvidia.com/embedded/learn/get-started-jetson-agx-orin-devkit).

## Connecting via SSH
For this type of connection first we need to know what's our board IP Adress. This is for the ones that have a serial console access, use the ifconfig command to get the required information in the Jetson terminal: 
```{.bash .shell-prompt}
hello-robot@ubuntu:~$ ifconfig

...

eth0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
    	inet 10.1.10.205  netmask 255.255.255.0  broadcast 10.1.10.205

wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
    	inet 10.1.10.205  netmask 255.255.255.0  broadcast 10.1.10.205
    	
```
This will show you all the connections that your Jetson has and you can have 2 output options with the IP address, the first one is if you have your Jetson connected to the internet via ethernet cable, with this the IP address will show up in the ethernet section, the second one is if you don't have an ethernet cable connected and instead you are connected via normal internet connection then the IP address will show up in the wlan0 section. With this now you can conncect your Jetson via SSH, if you have your Jetson connected to a monitor and you want to try it on Stretch follow the assembly instructions and then from your Stretch terminal just input the next command:
```{.bash .shell-prompt}
ssh jetson-username@ip-address
```
And now you will need to write the password that you configure and that's it, see below the output after you write down your password:
```{.bash .shell-prompt}
jetson-username@ip-address password:

Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.10.120-tegra aarch64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

Expanded Security Maintenance for Applications is not enabled.

9 updates can be applied immediately.
9 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable

35 additional security updates can be applied with ESM Apps.
Learn more about enabling ESM Apps service at https://ubuntu.com/esm

Last login: Thu Aug 24 10:21:30 2023
```
Now you can create your own projects using the Jetson of your preference!
