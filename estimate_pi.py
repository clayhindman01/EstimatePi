#Program that uses random points between 0-1 to estimate pi

import random
import math

#Places n number of points into the square
def place_points(n):

    #Initialize local variables for how many points are in the circle and in the square
    points_in_circle = 0
    counter = 0

    #Add n number of points to the sqare
    while counter != n:
        x = random.random()
        y = random.random()
        distance_from_origin = calculate_distance(0, 0, x, y)
        
        #Checks if the point is within the circle with a radius of 1
        if distance_from_origin <= 1:
            points_in_circle += 1
        counter += 1

    return points_in_circle

#Calculates the distance from a point to the origin
def calculate_distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

"""
Calculate pi using the ratio of the points in the circle / total points 
Area of circle = pi(r) ** 2
Area of square = (2 * r) ** 2
pi = 4 * points_in_circle / total_points
"""
def calculate_pi(points_in_circle, total_points):
    pi = (4 * points_in_circle) / total_points
    return pi

#Driver Program
def main():
    n = int(input("How many points do you want?"))
    points_in_circle = place_points(n)
    print(calculate_pi(points_in_circle, n))

main()