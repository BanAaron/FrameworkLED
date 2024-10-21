# frameworkLedDriverPython
a python module to control the LEDs on the framework 13 laptop

# methods

## getCurrentState()

returns a list of the current state of all files that the driver has access to

## setKbBrightness(brightness)

sets the keyboard brightness to a value between 0 and 100

## setPowerBrightness(brightness)

sets the power button led brightness to a value between 0 and 100

## setCapsBrightness(brightness)

sets the capslock light to on or off (1,0)

## setCol(led, color, intensity)

led: string name of the target led (left, right, power)

color: string name of the target color (red, green, blue, yellow, white, amber)

intensity: int (0 to 100) of target brightness of the color (this does not seem to have any effect, but it seems to have support. use setSideBrightness or setPowerBrightness instead)

## setSideBrightness(led, brightness)

led: string name of the target led (left, right)

brightness: int (0,100) value of the target brightness

# todo
add restore method to restore the state of the LEDs to what was captured by getCurrentState()

add RGB color mixing
