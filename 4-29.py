import math

def main():

    x1, y1, r1 = eval (input ("Enter x, y, radius circle 1: "))
    x2, y2, r2 = eval (input ("ditto: "))
    dist = math.sqrt( (x1 - x2) ** 2 + (y1 - y2) ** 2 )
    if (dist <= abs(r1 - r2)):
        print ("circle2 is inside circle1")
    elif (dist <= r1 + r2):
        print ("circle2 overlaps circle1")
    else:
        print ("circle 2 does not overlap circle1")

main()
