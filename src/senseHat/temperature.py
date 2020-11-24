import math
from random import randint
from time import sleep
from sense_hat import SenseHat

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


def resetLoadingDot():
    sense.set_pixel(0, 6, black)
    sense.set_pixel(1, 6, black)
    sense.set_pixel(0, 7, black)
    sense.set_pixel(1, 7, black)


def fillLoadingDot():
    randomColor = (randint(0, 255), randint(0, 255), randint(0, 255))

    sense.set_pixel(0, 6, randomColor)
    sense.set_pixel(1, 6, randomColor)
    sense.set_pixel(0, 7, randomColor)
    sense.set_pixel(1, 7, randomColor)


while True:
    temperature = sense.get_temperature_from_humidity()

    if temperature >= 0 and temperature < 100:
        stringTemperature = str(math.ceil(temperature))
        formattedTemperature = stringTemperature.zfill(2)

        firstNumber = formattedTemperature[0]
        secondNumber = formattedTemperature[1]

        fillPixel(leftNumberPixelPositions[int(
            firstNumber)] + rightNumberPixelPositions[int(secondNumber)], white)
    else:
        stringTemperature = str(math.floor(temperature))
        formattedTemperature = stringTemperature[1:len(
            stringTemperature)].zfill(2)

        firstNumber = formattedTemperature[0]
        secondNumber = formattedTemperature[1]

        fillPixel(leftNumberPixelPositions[int(
            firstNumber)] + rightNumberPixelPositions[int(secondNumber)], blue)

    resetLoadingDot()
    sleep(0.5)
    fillLoadingDot()
    sleep(1)
