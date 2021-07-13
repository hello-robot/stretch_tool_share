import setuptools
from os import listdir
from os.path import isfile, join

script_path='./bin'
tool_scripts={script_path+'/'+f for f in listdir(script_path) if isfile(join(script_path, f))}

setuptools.setup(
    name="hello_robot_stretch_tool_share",
    version='0.1.5',
    author="Hello Robot Inc.",
    author_email="support@hello-robot.com",
    description="Stretch RE1 end of arm tool interfaces",
    url="https://github.com/hello-robot/stretch_tool_share",
    scripts = tool_scripts,
    packages=['stretch_tool_share',
              'stretch_tool_share.stretch_dex_wrist_beta',
              'stretch_tool_share.stretch_dex_wrist',
              'stretch_tool_share.reactorx_wrist_v1',
              'stretch_tool_share.usbcam_wrist_v1',
              'stretch_tool_share.dry_erase_holder_v1'],
    classifiers=[
        "Programming Language :: Python :: 2",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)"
    ]
)

