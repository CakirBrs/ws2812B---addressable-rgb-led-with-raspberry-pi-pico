import time
from neopixel import Neopixel

numpix = 3 # number of ws2812
strip = Neopixel(numpix, 0, 28, "RGB") # in third order we set data pin to 28

red = (255, 0, 0)
orange = (255, 50, 0)
yellow = (255, 100, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (100, 0, 90)
violet = (200, 0, 100)
colors_rgb = [red, orange, yellow, green, blue, indigo, violet]

strip.brightness(40)


while True:
    for x in range(len(colors_rgb)):
        strip.set_pixel(0,colors_rgb[x])
        strip.set_pixel(1,colors_rgb[(x+2)%7])
        strip.set_pixel(2,colors_rgb[(x+4)%7])
        strip.show()
        time.sleep(.3)