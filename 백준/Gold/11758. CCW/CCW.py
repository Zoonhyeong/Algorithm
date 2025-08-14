# 11758 CCW
import sys

input = sys.stdin.readline

p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))
p3 = list(map(int, input().split()))

def ccw(p1_x, p1_y, p2_x, p2_y, p3_x, p3_y):
    # Calculate cross product
    cross_product = (p2_x - p1_x) * (p3_y - p1_y) - (p2_y - p1_y) * (p3_x - p1_x)
    if cross_product > 0:
        return 1  # Counter-clockwise
    elif cross_product < 0:
        return -1 # Clockwise
    else:
        return 0  # Collinear

# Use the revised function
print(ccw(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1]))