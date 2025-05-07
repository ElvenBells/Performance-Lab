import sys

circle_file = sys.argv[1]
dots_file = sys.argv[2]

with open('circle.txt', 'r') as f:
    x, y = map(float, f.readline().split())
    r = float(f.readline())

with open('dots.txt', 'r') as f:
    points = [tuple(map(float, line.split())) for line in f]

for px, py in points:
    distance = (px - x)**2 + (py - y)**2
    
    if abs(distance - r**2) < 1e-9:
        print(0)
    elif distance < r**2:
        print(1)
    else:
        print(2)
