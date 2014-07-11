def main():
    """
    for num in range (1, 10001):
        divSum = 0
        if (num % 2 == 0):
            for div in range (1, (int (num / 2) + 1)):
                if (num % div == 0):
                    divSum += div

            if divSum == num:
                print (num)
    """
    p = 2
    perfect = 2 ** (p - 1) * (2 ** p - 1)
    while (perfect< 10000):
        isPrime = False
        for num in range (2, p):
            if (p % num == 0 and p != num):
                isPrime = True
        if (not isPrime):
            print (perfect, end = " ")
        p = p + 1
        perfect = 2 ** (p - 1) * (2 ** p - 1)
    print ("")
main()
