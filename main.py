from LedDriver import set_brightness, LEDPaths, Brightness, set_colour, Colour

if __name__ == "__main__":
    LEDs = LEDPaths

    brightness = Brightness(100)
    side_colour = Colour(green=100)

    set_brightness(LEDs.power_button_brightness, brightness)
    set_colour(LEDs.power_button_color, side_colour)
    set_colour(LEDs.rightCol, side_colour)
    set_colour(LEDs.leftCol, side_colour)

    # colour = Colour(white=100)
    # set_colour(LEDs.power_button_color, colour)
