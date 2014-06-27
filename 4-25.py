def main():
    x1, y1, x2, y2, x3, y3, x4, y4 = eval (input ("Enter points: "))
    a = y1 - y2; b = - (x1 - x2); c = y3 - y4; d = - (x3 - x4)
    e = x1 * (y1 - y2) - y1 * (x1 - x2)
    f = x3 * (y3 - y4) - y3 * (x3 - x4)
    denom = a * d - b * c
    if denom == 0:
        print ("The two lines are parallel")
    else:
        x = (e * d - b * f) / denom
        y = (a * f - e * c) / denom
        print ("The intersecting point is at (", x, ", ", y, ")", sep="")

main()
