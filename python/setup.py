import setuptools

setuptools.setup(
    name="hello_robot_stretch_tool_share",
    version='0.0.1',
    author="Hello Robot Inc.",
    author_email="support@hello-robot.com",
    description="Stretch RE1 end of arm tool interfaces",
    url="https://github.com/hello-robot/stretch_tool_share",
    packages=['stretch_tool_share',
              'stretch_tool_share.dexterous_wrist_vbeta',
              'stretch_tool_share.reactorx_wrist_v1',
              'stretch_tool_share.usbcam_wrist_v1'],
    classifiers=[
        "Programming Language :: Python :: 2",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)"
    ]
)
