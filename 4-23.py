def main():
    x, y = eval (input ('Enter points: '))
    if ((x <= 5/2 and x >= -5/2) and (y <= 10/2 and y >= -10/2)):
        print ("Point (", x, ", ", y, ") is in the rectangle", sep = "")
    else:
        print ("Point (", x, ", ", y, ") is not in the rectangle", sep = "")

main()

