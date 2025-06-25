from LedDriver import set_brightness, LEDPaths, Brightness, Colour, set_colour

if __name__ == "__main__":
    LEDs = LEDPaths
    # set color
    green = Colour(green=100)
    set_colour(LEDs.power_button_color, green)
    # set brightness
    brightness = Brightness(69)
    set_brightness(LEDs.keyboard_backlight, brightness)
