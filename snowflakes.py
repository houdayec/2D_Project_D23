# -*- coding: utf-8 -*-
import cng as cng
import random as rdn
import time
import math
from lib_bresenham import *

#classes definition
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.id = 0

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

    def moveFall(self):
        (point_x, point_y) = cng.obj_get_position(self.id)
        (computed_x, computed_y) = self.compute_values()
        cng.obj_move(self.id, (computed_x - point_x), (computed_y - point_y)-100)
    def moveTo(self, x, y):
        (point_x, point_y) = cng.obj_get_position(self.id)
        (computed_x, computed_y) = self.compute_values()
        cng.obj_move(self.id, (computed_x - point_x) + x, (computed_y - point_y) + y)

class Window:
    def __init__(self, x_origin, y_origin, width, height):
        self.x_origin = x_origin
        self.y_origin = y_origin
        self.width = width
        self.height = height

#Variables globales
positionXRectangle=None
positionYRectangle=None
rectangleID=None
point=None
viewport=None
window=None
draw_point=None
global viewport_x
global viewport_y

window_width, window_height = 1000, 600
window_x, window_y = 0, 0
viewport_width, viewport_height = 600, 400
viewport_x, viewport_y = 200, 20
viewport_min_x = viewport_width - viewport_x
viewport_max_x = viewport_width + viewport_x
viewport_min_y = viewport_height - viewport_y
viewport_max_y = viewport_height + viewport_y
height_snowflake = 40
width_snowflake = 40
angle_rotation_snowflake = 1.0472

array_points_branch_snowflake = [
Point(viewport_max_x/2,viewport_max_y-(height_snowflake/2)), # Base de la tige centrale du flocon
Point(viewport_max_x/2,viewport_max_y+(height_snowflake/2)), # Haut de la tige centrale du flocon
Point(viewport_max_x/2,viewport_max_y+(height_snowflake/2) - 20), # Début branche gauche
Point((viewport_max_x/2) - 20,viewport_max_y+(height_snowflake/2)), # Fin branche gauche
Point(viewport_max_x/2,viewport_max_y+(height_snowflake/2) - 20), # Début branche droite
Point((viewport_max_x/2) + 20,viewport_max_y+(height_snowflake/2)) ] # Fin branche droite
points = []
array_points_snowflake = []

def drawSnowflake():
    k = 0
    point_to_draw = array_points_branch_snowflake
    for k in range(0,6):
        if(k != 0): # S'il ne s'agit pas de la première branche, on applique une rotation
            point_to_draw = rotate_branch(point_to_draw)
        i = 0
        for i in range(0,5):
                print(point_to_draw[i].x, point_to_draw[i].y)
                print(point_to_draw[i+1].y, point_to_draw[i+1].y)
                array_points_snowflake.append(bresenham(point_to_draw[i], point_to_draw[i+1]))
                i = i + 2
    for list_points in array_points_snowflake:
        projection_points(list_points)

# Fonction pour projeter un point
def projection_point(point):
    points.append(point)
    point.draw()
    #print(point.id)

# Fonction pour projeter un ensemble de points
def projection_points(points):
    for point in points:
        projection_point(point)

def main():
    cng.init_window('Snowflakes', window_width, window_height)
    viewport = cng.rectangle(viewport_x, viewport_y, viewport_x + viewport_width, viewport_y + viewport_height)
    pass

def rotate_branch(array_points):
    new_points = []
    for point in array_points:
        new_points.append(rotate(array_points_branch_snowflake[0], point, angle_rotation_snowflake))
    return new_points

def fall_snowflake():
    for list_points in array_points_snowflake:
        for point in list_points:
            point.moveFall()
            point.moveTo(50,50)

# Méthode de rotation d'un point par rapport à l'origin d'un certain angle
def rotate(origin, point, angle):
    print("origin ", origin.x, " ", origin.y, "point ", point.x, " ",point.y, "angle ", angle)
    ox, oy = origin.x, origin.y
    px, py = point.x, point.y

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)

    point = Point(qx,qy)
    return point

if __name__ == "__main__":
    main()
    drawSnowflake()
    for point in array_points_branch_snowflake:
        print(point.x, " ", point.y)
    #projection_points(array_points_branch_snowflake)
    fall_snowflake()
    cng.main_loop()
