from stretch_body.end_of_arm_tools import ToolNone


class ToolUSBCamWrist(ToolNone):
    def __init__(self):
        ToolNone.__init__(self, 'tool_usbcam_wrist')

    def take_picture(self):
        raise NotImplementedError()

    def return_stream(self):
        raise NotImplementedError()
