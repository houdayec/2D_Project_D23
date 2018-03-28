import cng as cng
import random as rdn
import time


#classes definition
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Window:
    def __init__(self, x_origin, y_origin, width, height):
        self.x_origin = x_origin
        self.y_origin = y_origin
        self.width = width
        self.height = height

array_points = [ Point(500,500), Point(500,1000), Point(500,800), Point(300,1000), Point(500,800), Point(700,1000) ]
positionXRectangle=None
positionYRectangle=None
rectangleID=None
point=None
viewport=None
window=None
draw_point=None

def initWindow():
    global step, pointA, pointB, point, viewport, window

    temp = None
    cng.init_window("pgl : Snowflakes", color='white')
    step = 0.5

    point = Point(3,1)
    viewport = Window(480, 240, 1500, 1000)
    window = Window(-2,-1,6,5)

    rdn.seed(time.time())
    debut = time.time();
    #for x in range(0, 10000):
    #    pointA = Point(rdn.randint(0, 600),rdn.randint(0, 600))
    #    pointB = Point(rdn.randint(0, 800),rdn.randint(0, 800))
    #    bresenham(pointA, pointB)

        #bresenham(pt.x, pt.y)
    fin = time.time()
    print("With bresenham : ", fin - debut)

    rdn.seed(0)
    #y = pointA.x
    #debut = time.time();
    #for x in range(0, 10000):
    #    for x in range(pointA.x, pointB.x):
    #       drawPoint(x, y)
    #       x+=step
    #       y+=step
    #fin = time.time()

def bresenham(pointA, pointB):
    dx = pointB.x - pointA.x
    dy mvn -B archetype:generate \
   -DarchetypeGroupId=fr.univtln.bruno.archetype \
   -DarchetypeArtifactId=javaSimpleArchetype \
   -DarchetypeVersion=0.1.0-develop-6 \
   -DgroupId=fr.univtln.bruno.test \
   -DartifactId=monprojet \
   -Dversion=1.0-SNAPSHOT \
   -DprojectShortName=monprojet \
   -DgithubAccount=emmanuelbruno \
   -DUtlnEmail=emmanuel.bruno@univ-tln.fr= pointB.y - pointA.y
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
        print("dx : ", dx, "dy : ", dy, "dec : ", dec)

        print("x : ", x, " y : ", y)
        while(int(x) != int(pointB.x)):
            print(int(x), int(pointB.x))
            drawPoint(x,y)
            if(dec < 0):
                dec = dec + 2*abs(dx)
                y = y + signY
            dec = dec - 2*abs(dy)
            x = x + signX
    else :
        dec = abs(dy) - 2*abs(dx)
        while(int(y) != int(pointB.y)):
            print(int(y), int(pointB.y))
            drawPoint(x,y)
            if(dec < 0):
                dec = dec + 2*abs(dy)
                x = x + signX
            dec = dec - 2 * abs(dx)
            y = y + signY

def drawSnowflake():
    bresenham(array_points[0], array_points[1])
    bresenham(array_points[3], array_points[2])
    bresenham(array_points[4], array_points[5])

def drawRectangle():
    #draw a rectangle
    #screen specifications
    screen_width = cng.get_screen_width()
    screen_height = cng.get_screen_height()
    print('Width : ', screen_width, ' Height : ', screen_height)
    positionXRectangle=(screen_width/4)
    positionYRectangle=(screen_height/4)
    return cng.rectangle(viewport.x_origin,viewport.y_origin,viewport.width,viewport.height, 2)


def drawPoint(x,y):
    global draw_point
    draw_point = cng.circle(x, y, 1,1)

def main():
    #last instruction in program
    cng.main_loop()

initWindow()
rectangleID = drawRectangle()
drawSnowflake()
main()
