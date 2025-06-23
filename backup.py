bl = "/sys/class/leds/chromeos::kbd_backlight/brightness"
caps = "/sys/class/leds/input2::capslock/brightness"
rightCol = "/sys/class/leds/chromeos:multicolor:right/multi_intensity"
rightBri = "/sys/class/leds/chromeos:multicolor:right/brightness"
leftCol = "/sys/class/leds/chromeos:multicolor:left/multi_intensity"
leftBri = "/sys/class/leds/chromeos:multicolor:left/brightness"
powerCol = "/sys/class/leds/chromeos:multicolor:power/multi_intensity"
powerBri = "/sys/class/leds/chromeos:multicolor:power/brightness"


def getCurrentState():
    fullSet = []
    for i in [bl, caps, rightCol, rightBri, leftCol, leftBri, powerCol, powerBri]:
        file = open(i, "r")
        fullSet.append(file.read())
        file.close()
    return fullSet


def setKbBrightness(brightness):
    brightness = int(brightness)
    if brightness >= 0:
        if brightness <= 100:
            file = open(bl, "w+")
            file.write(str(brightness))
            file.close()


def setPowerBrightness(brightness):
    brightness = int(brightness)
    if brightness >= 0:
        if brightness <= 100:
            file = open(powerBri, "w+")
            file.write(str(brightness))
            file.close()


def setCapsBrightness(brightness):
    brightness = int(brightness)
    if brightness >= 0:
        if brightness <= 1:
            file = open(caps, "w+")
            file.write(str(brightness))
            file.close()


def setCol(led, color, intensity):
    if led == "left":
        path = leftCol
    if led == "right":
        path = rightCol
    if led == "power":
        path = powerCol

    if intensity <= 100 and intensity >= 0:
        file = open(path, "w+")

        colorFilter = ["red", "green", "blue", "yellow", "white", "amber"]
        colorWriteList = [0, 0, 0, 0, 0, 0]
        index = 0
        for i in colorFilter:
            if i == color:
                colorWriteList[index] = intensity
                break
            index += 1
        colorString = ""
        for i in colorWriteList:
            colorString += str(i) + " "
        file.write(colorString)
        file.close()


def setSideBrightness(led, brightness):
    if led == "right":
        path = rightBri
    if led == "left":
        path = leftBri
    brightness = int(brightness)
    if brightness <= 1 and brightness >= 0:
        file = open(path, "w+")
        file.write(str(brightness))
        file.close()


if __name__ == "__main__":
    import time

    setCol("right", "red", 100)
    setCol("left", "green", 100)
    setCol("power", "white", 100)
    print(getCurrentState())
    while True:
        for i in range(3):
            setKbBrightness(100)
            setCapsBrightness(1)
            setSideBrightness("right", 1)
            setSideBrightness("left", 1)
            setPowerBrightness(100)
            time.sleep(1)
            setKbBrightness(0)
            setCapsBrightness(0)
            setSideBrightness("right", 0)
            setSideBrightness("left", 0)
            setPowerBrightness(0)
            time.sleep(1)
        setSideBrightness("right", 1)
        setSideBrightness("left", 1)
        setPowerBrightness(100)
        cl = ["red", "green", "blue", "yellow", "white", "amber"]
        for i in range(5):
            setCol("right", cl[i], 100)
            setCol("left", cl[i], 100)
            setCol("power", cl[i], 100)
            setKbBrightness(int(((i + 1) * 1 / 6) * 100))
            time.sleep(0.5)
        setCol("left", "white", 100)
        setCol("right", "white", 100)
