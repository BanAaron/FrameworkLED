from LedDriver import set_brightness, LEDPaths, Brightness, Colour, set_colour

if __name__ == "__main__":
    LEDs = LEDPaths
    # set color
    red = Colour(red=100)
    set_colour(LEDs.power_button_color, red)
    # set brightness
    brightness = Brightness(50)
    set_brightness(LEDs.keyboard_backlight, brightness)
