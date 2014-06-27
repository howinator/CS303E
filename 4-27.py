def main():
    x1, y1 = eval (input ("Enter x, y coords: "))
    # This finds the x and y points on the hypotenuse that form a 
    # perpindicular line with the specified points, x1 and y1.
    x2 = (2 * x1 + 100 - y1) / 2.5
    y2 = -x2 / 2 + 100
    if (x1 > x2 or y1 > y2):
        print ("The point is not in the triangle")
    else:
        print ("The point is in the triangle")

main()
