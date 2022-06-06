#/bin/python

from time import sleep
from future import *
import math

P0 = MeowPin('P0', 'ANALOG')
P1 = MeowPin('P1', 'ANALOG')

screen.sync = 0


while True:
    sleep(0.1)
    screen.clear()
    rows = math.floor(P0.getAnalog(10) * 30 / 1023)
    cols = math.floor(P1.getAnalog(10) * 30 / 1023)
  
    height = rows * 3
    width = cols * 3
  
    if height == width:
        color = (255, 0, 0)
    else:
        color = (255, 255, 255)
  
    for x in range(0, height + 1, 3):
        screen.line(x, 0, x, width, color)
    
    for x in range(0, width + 1, 3):
        screen.line(0, x, height, x, color)
  
    screen.text(str(cols), 0, 101, 1, color)
    screen.text(str(rows), 101, 0, 1, color)
    screen.text(str(rows * cols), 101, 101, 1, color)
    
    screen.refresh()
