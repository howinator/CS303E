from math import sqrt

def main():
    print ("Enter 10 numbers: ")
    straightSum = 0
    squareSum = 0
    for num in range (1, 11):
        inp = eval (input (""))
        straightSum += inp
        squareSum += inp ** 2
    mean = straightSum / 10
    dev = sqrt ( (squareSum - straightSum ** 2 / 10) / 9)

    print ("The mean is", mean)
    print ("The standard deviation is", dev)

main()
