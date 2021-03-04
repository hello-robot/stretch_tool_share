from stretch_body.end_of_arm import EndOfArm


class ToolUSBCamWrist(EndOfArm):
    def __init__(self, name='tool_usbcam_wrist'):
        EndOfArm.__init__(self, name)

    def take_picture(self):
        raise NotImplementedError()

    def return_stream(self):
        raise NotImplementedError()
