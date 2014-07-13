from math import sqrt

def main():
    mySum = 0
    for num in range (1, 625):
        mySum += 1 / (sqrt (num) + sqrt (num + 1))
    print (format (mySum, "5.2f"))

main()
