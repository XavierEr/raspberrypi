import math
from random import randint
from time import sleep
# from sense_hat import SenseHat
from sense_emu import SenseHat

sense = SenseHat()
sense.clear()
sense.low_light = True

black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
yellow = [255, 255, 0]

leftZeroPixelPositions = [0, 1, 2, 8, 10, 16, 18, 24, 26, 32, 33, 34]
rightZeroPixelPositions = [4, 5, 6, 12, 14, 20, 22, 28, 30, 36, 37, 38]

leftOnePixelPositions = [1, 9, 17, 25, 33]
rightOnePixelPositions = [5, 13, 21, 29, 37]

leftTwoPixelPositions = [0, 1, 2, 10, 16, 17, 18, 24, 32, 33, 34]
rightTwoPixelPositions = [4, 5, 6, 14, 20, 21, 22, 28, 36, 37, 38]

leftThreePixelPositions = [0, 1, 2, 10, 16, 17, 18, 26, 32, 33, 34]
rightThreePixelPositions = [4, 5, 6, 14, 20, 21, 22, 30, 36, 37, 38]

leftFourPixelPositions = [0, 2, 8, 10, 16, 17, 18, 26, 34]
rightFourPixelPositions = [4, 6, 12, 14, 20, 21, 22, 30, 38]

leftFivePixelPositions = [0, 1, 2, 8, 16, 17, 18, 26, 32, 33, 34]
rightFivePixelPositions = [4, 5, 6, 12, 20, 21, 22, 30, 36, 37, 38]

leftSixPixelPositions = [0, 1, 2, 8, 16, 17, 18, 24, 26, 32, 33, 34]
rightSixPixelPositions = [4, 5, 6, 12, 20, 21, 22, 28, 30, 36, 37, 38]

leftSevenPixelPositions = [0, 1, 2, 10, 18, 26, 34]
rightSevenPixelPositions = [4, 5, 6, 14, 22, 30, 38]

leftEightPixelPositions = [0, 1, 2, 8, 10, 16, 17, 18, 24, 26, 32, 33, 34]
rightEightPixelPositions = [4, 5, 6, 12, 14, 20, 21, 22, 28, 30, 36, 37, 38]

leftNinePixelPositions = [0, 1, 2, 8, 10, 16, 17, 18, 26, 32, 33, 34]
rightNinePixelPositions = [4, 5, 6, 12, 14, 20, 21, 22, 30, 36, 37, 38]

leftNumberPixelPositions = [
    leftZeroPixelPositions,
    leftOnePixelPositions,
    leftTwoPixelPositions,
    leftThreePixelPositions,
    leftFourPixelPositions,
    leftFivePixelPositions,
    leftSixPixelPositions,
    leftSevenPixelPositions,
    leftEightPixelPositions,
    leftNinePixelPositions
]

rightNumberPixelPositions = [
    rightZeroPixelPositions,
    rightOnePixelPositions,
    rightTwoPixelPositions,
    rightThreePixelPositions,
    rightFourPixelPositions,
    rightFivePixelPositions,
    rightSixPixelPositions,
    rightSevenPixelPositions,
    rightEightPixelPositions,
    rightNinePixelPositions
]


def fillPixel(pixelPositions, color):
    pixels = []

    for i in range(0, 64):
        if i in pixelPositions:
            pixels.append(color)
        else:
            pixels.append(black)

    sense.set_pixels(pixels)


def fillLoadingDot(rgbArgs):
    sense.set_pixel(0, 6, rgbArgs)
    sense.set_pixel(1, 6, rgbArgs)
    sense.set_pixel(0, 7, rgbArgs)
    sense.set_pixel(1, 7, rgbArgs)


def fillDecimalDot(decimalValue, rgbArgs):
    if decimalValue == 1:
        sense.set_pixel(3, 7, rgbArgs)
    elif decimalValue == 2:
        sense.set_pixel(3, 7, rgbArgs)
        sense.set_pixel(4, 7, rgbArgs)
    elif decimalValue == 3:
        sense.set_pixel(3, 7, rgbArgs)
        sense.set_pixel(4, 7, rgbArgs)
        sense.set_pixel(5, 7, rgbArgs)
    elif decimalValue == 4:
        sense.set_pixel(3, 7, rgbArgs)
        sense.set_pixel(4, 7, rgbArgs)
        sense.set_pixel(5, 7, rgbArgs)
        sense.set_pixel(5, 6, rgbArgs)
    elif decimalValue == 5:
        sense.set_pixel(3, 7, rgbArgs)
        sense.set_pixel(4, 7, rgbArgs)
        sense.set_pixel(5, 7, rgbArgs)
        sense.set_pixel(5, 6, rgbArgs)
        sense.set_pixel(6, 7, rgbArgs)
    elif decimalValue == 6:
        sense.set_pixel(3, 7, rgbArgs)
        sense.set_pixel(4, 7, rgbArgs)
        sense.set_pixel(5, 7, rgbArgs)
        sense.set_pixel(5, 6, rgbArgs)
        sense.set_pixel(6, 7, rgbArgs)
        sense.set_pixel(6, 6, rgbArgs)
    elif decimalValue == 7:
        sense.set_pixel(3, 7, rgbArgs)
        sense.set_pixel(4, 7, rgbArgs)
        sense.set_pixel(5, 7, rgbArgs)
        sense.set_pixel(5, 6, rgbArgs)
        sense.set_pixel(6, 7, rgbArgs)
        sense.set_pixel(6, 6, rgbArgs)
        sense.set_pixel(7, 7, rgbArgs)
    elif decimalValue == 8:
        sense.set_pixel(3, 7, rgbArgs)
        sense.set_pixel(4, 7, rgbArgs)
        sense.set_pixel(5, 7, rgbArgs)
        sense.set_pixel(5, 6, rgbArgs)
        sense.set_pixel(6, 7, rgbArgs)
        sense.set_pixel(6, 6, rgbArgs)
        sense.set_pixel(7, 7, rgbArgs)
        sense.set_pixel(7, 6, rgbArgs)
    elif decimalValue == 9:
        sense.set_pixel(3, 7, rgbArgs)
        sense.set_pixel(4, 7, rgbArgs)
        sense.set_pixel(5, 7, rgbArgs)
        sense.set_pixel(5, 6, rgbArgs)
        sense.set_pixel(6, 7, rgbArgs)
        sense.set_pixel(6, 6, rgbArgs)
        sense.set_pixel(7, 7, rgbArgs)
        sense.set_pixel(7, 6, rgbArgs)
        sense.set_pixel(7, 5, rgbArgs)
    else:
        sense.set_pixel(3, 7, rgbArgs)
        sense.set_pixel(4, 7, rgbArgs)
        sense.set_pixel(5, 7, rgbArgs)
        sense.set_pixel(6, 7, rgbArgs)
        sense.set_pixel(7, 7, rgbArgs)
        sense.set_pixel(5, 6, rgbArgs)
        sense.set_pixel(6, 6, rgbArgs)
        sense.set_pixel(7, 6, rgbArgs)
        sense.set_pixel(7, 5, rgbArgs)


while True:
    temperature = sense.get_temperature_from_humidity()

    stringTemperature = '%.1f' % temperature
    splitedStringTemperature = stringTemperature.split('.')

    stringWholeTemperature = splitedStringTemperature[0]

    formattedTemperature = ''

    if temperature >= 0:
        formattedTemperature = stringWholeTemperature.zfill(2)
    else:
        formattedTemperature = stringWholeTemperature[1:len(
            stringWholeTemperature)].zfill(2)

    firstNumber = formattedTemperature[0]
    secondNumber = formattedTemperature[1]
    color = blue if temperature < 26 else red if temperature > 31 else white

    fillPixel(leftNumberPixelPositions[int(
        firstNumber)] + rightNumberPixelPositions[int(secondNumber)], color)

    fillDecimalDot(
        int(splitedStringTemperature[1]), black if int(splitedStringTemperature[1]) == 0 else color)

    fillLoadingDot(black)
    sleep(0.5)
    fillLoadingDot([randint(0, 255), randint(0, 255), randint(0, 255)])
    sleep(1)
