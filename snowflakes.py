import cng as cng
import random as rdn
import time
from lib_bresenham import *

#classes definition
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.identifier = 0

    # Fonction qui permet de calculer les nouvelles coordonnées du point projeté dans la viewport
    def compute_values(self):
        global viewport_x
        global viewport_y
        computed_x = (self.x * (viewport_width/window_width) + self.y*0 + 1 * (viewport_x * window_width - window_x * viewport_width)/window_width)
        computed_y = (self.x * 0 + self.y * (viewport_height/window_height) + 1 * (viewport_y - (viewport_height * window_y)/viewport_height))
        return (computed_x, computed_y)

    # Fonction qui permet de dessiner un point à l'écran
    def draw(self):
        (computed_x, computed_y) = self.compute_values()
        #print(computed_x, computed_y)
        self.id = cng.circle(computed_x, computed_y, 1)

    # Fonction qui permet de bouger un point (appelle la fonction de recalcul de ses coordonnées)
    def move(self):
        (point_x, point_y) = cng.obj_get_position(self.id)
        (computed_x, computed_y) = self.compute_values()
        cng.obj_move(self.id, computed_x - point_x, computed_y - point_y)

class Window:
    def __init__(self, x_origin, y_origin, width, height):
        self.x_origin = x_origin
        self.y_origin = y_origin
        self.width = width
        self.height = height

#Variables globales
array_points_snowflake = [ Point(50,50), Point(50,100), Point(50,80), Point(30,100), Point(50,80), Point(70,100) ]
positionXRectangle=None
positionYRectangle=None
rectangleID=None
point=None
viewport=None
window=None
draw_point=None
global viewport_x
global viewport_y

window_width, window_height = 1280, 720
window_x, window_y = 0, 0
viewport_width, viewport_height = 1000, 600
viewport_x, viewport_y = 200, 20

points = []

def drawSnowflake():
    bresenham(array_points_snowflake[0], array_points_snowflake[1])
    bresenham(array_points_snowflake[3], array_points_snowflake[2])
    bresenham(array_points_snowflake[4], array_points_snowflake[5])

# Fonction pour projeter un point
def projection_point(x2 , y2):
    point = Point(x2, y2)
    points.append(point)
    point.draw()

# Fonction pour projeter un ensemble de points
def projection_points(points):
    for point in points:
        projection_point(point.x, point.y)

def main():
    cng.init_window('Snowflakes', window_width, window_height)
    viewport = cng.rectangle(viewport_x, viewport_y, viewport_x + viewport_width, viewport_y + viewport_height)
    pass

if __name__ == "__main__":
    main()
    drawSnowflake()
    projection_points(array_points_snowflake)
    cng.main_loop()
