import random
import math

def estimate_pi(n):

    points_in_circle = 0
    points_in_square = 0
    counter = 0

    while counter != n:
        points_in_square += 1
        x = random.random()
        y = random.random()
        distance_from_origin = calculate_distance(0, 0, x, y)
        if distance_from_origin <= 1:
            points_in_circle += 1
        counter += 1
    return points_in_circle, points_in_square

def calculate_distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

def calculate_ratio(points_in_circle, points_in_square):
    pi = (4 * points_in_circle) / points_in_square
    return pi

def main():
    n = int(input("How many points do you want?"))
    points_in_circle, points_in_square = estimate_pi(n)
    print(calculate_ratio(points_in_circle, points_in_square))

main()