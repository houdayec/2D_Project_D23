import cng as cng
import random as rdn
import time

def bresenham(pointA, pointB):
    dx = pointB.x - pointA.x
    dy = pointB.y - pointA.y
    x = pointA.x
    y = pointA.y
    signY = 1
    signX = 1

    if(dy < 0):
        signY = -1
    if(dx < 0):
        signX = -1
    if(abs(dx) > abs(dy)):
        dec = abs(dx) - 2*abs(dy)

        while(int(x) != int(pointB.x)):
            #pointA.draw()
            drawPoint(x,y)
            if(dec < 0):
                dec = dec + 2*abs(dx)
                y = y + signY
            dec = dec - 2*abs(dy)
            x = x + signX
    else :
        dec = abs(dy) - 2*abs(dx)
        while(int(y) != int(pointB.y)):
            #pointA.draw()
            drawPoint(x,y)
            if(dec < 0):
                dec = dec + 2*abs(dy)
                x = x + signX
            dec = dec - 2 * abs(dx)
            y = y + signY

def drawPoint(x,y):
    global draw_point
    draw_point = cng.circle(x, y, 1,1)
