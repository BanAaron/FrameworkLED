from dataclasses import dataclass
from enum import StrEnum
from os import path


class LEDPaths(StrEnum):
    backlight_brightness = "/sys/class/leds/chromeos::kbd_backlight/brightness"
    capslock = "/sys/class/leds/input2::capslock/brightness"
    power_button_brightness = "/sys/class/leds/chromeos:multicolor:power/brightness"
    power_button_color = "/sys/class/leds/chromeos:multicolor:power/multi_intensity"
    rightCol = "/sys/class/leds/chromeos:multicolor:right/multi_intensity"
    rightBri = "/sys/class/leds/chromeos:multicolor:right/brightness"
    leftCol = "/sys/class/leds/chromeos:multicolor:left/multi_intensity"
    leftBri = "/sys/class/leds/chromeos:multicolor:left/brightness"


class Brightness(int):
    def __new__(cls, value=100):
        if value < 0:
            return 0
        elif value > 100:
            return 100
        return value


@dataclass
class Colour:
    red: int = 0
    green: int = 0
    blue: int = 0
    yellow: int = 0
    white: int = 0
    amber: int = 0

    def __post_init__(self):
        if sum(self.__dict__.values()) == 0:
            self.white = 100

    def __str__(self):
        return f"{self.red} {self.green} {self.blue} {self.yellow} {self.white} {self.amber}"


def write_value(sys_path: str, value: Brightness | Colour) -> str:
    if not path.exists(sys_path):
        raise Exception(f"Path does not exist: {sys_path}")
    with open(sys_path, "w") as write_file:
        write_file.write(str(value))
    with open(sys_path, "r") as read_file:
        res = read_file.read()
    return res


def set_brightness(sys_path: str, brightness: Brightness) -> str:
    return write_value(sys_path, brightness)


def set_colour(sys_path: str, colour: Colour) -> str:
    return write_value(sys_path, colour)


if __name__ == "__main__":
    pass
