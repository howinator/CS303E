from math import sqrt

def main():
    sum = 0
    for i in range (1, 625):
        sum += 1 / (sqrt (i) + sqrt (i + 1))

main()
