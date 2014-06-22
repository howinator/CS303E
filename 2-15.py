import math

def main():
    side = eval(input("Please enter the length of the side: "))
    area = 3 / 2 * math.sqrt(3) * side ** 2
    print("The area of the hexagon is", area)

main()
