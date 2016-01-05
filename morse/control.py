import pygatt.backends
import time
import logging
import struct
from colour import Color

logging.getLogger().setLevel(logging.DEBUG)

DEVICE_HANDLE = 19
COMMANDS={
    "neck_color":0x03,
    "eye_brightness":0x08,
    "eye":0x09,
    "left_ear_color":0x0b,
    "right_ear_color":0x0c,
    "head_color":0x0d,
    "head_pitch":0x07,
    "head_yaw":0x06
}

def one_byte_array(value):
    return bytearray(struct.pack(">B", value))

def two_byte_array(value):
    return bytearray(struct.pack(">H", value))

def color_byte_array(color_value):
    color = Color(color_value)
    return bytearray([
        int(color.get_red()*255),
        int(color.get_green()*255),
        int(color.get_blue()*255),
    ])

def angle_array(angle):
    if angle < 0:
        angle = (abs(angle) ^ 0xff) + 1
    return bytearray([angle & 0xff])

class WonderControl(object):
    def __init__(self, address):
        adapter = pygatt.backends.GATTToolBackend()
        adapter.start()
        self.device = adapter.connect(address, address_type='random')

    def command(self, command_name, command_values):
        message = bytearray([COMMANDS[command_name]]) + command_values
        logging.debug([hex(byte) for byte in message])
        self.device.char_write_handle(DEVICE_HANDLE, message)

    def eye(self, value):
        self.command("eye", two_byte_array(value))

    def eye_brightness(self, value):
        self.command("eye_brightness", one_byte_array(value))

    def neck_color(self, color):
        self.command("neck_color", color_byte_array(color))

    def left_ear_color(self, color):
        self.command("left_ear_color", color_byte_array(color))

    def right_ear_color(self, color):
        self.command("right_ear_color", color_byte_array(color))

    def ear_color(self, color):
        self.left_ear_color(color)
        self.right_ear_color(color)

    def head_color(self, color):
        self.command("head_color", color_byte_array(value))

    def head_yaw(self, angle):
        """
        Angle range is from -53 to 53
        """
        if angle <- 53:
           angle = -53
        if angle > 53:
            angle = 53
        self.command("head_yaw", angle_array(angle))

    def head_pitch(self, angle):
        """
        Angle range is from -5 to 10
        """
        if angle <- 5:
            angle = -5
        if angle > 10:
            angle = 10
        self.command("head_pitch", angle_array(angle))


if __name__ == "__main__":
    wc = WonderControl("C0:F0:84:3C:51:FA")

