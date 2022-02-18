import math
import modules.practical_example

def triangle(base, height):
    return 1/2*base*height

def circle(radius):
    return math.pi*radius**2

def donut(r1, r2):
    return math.pi*(r2**2 - r1**2)