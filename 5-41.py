def main():
    inNum = -999999999999999999999999999999999
    maxi = inNum
    count = 0
    while (inNum):
        inNum = eval (input ("Enter a number (0 to exit): "))
        if inNum > maxi:
            maxi = inNum
            count = 1
        elif (inNum == maxi):
            count += 1
    print ("The largest number is", maxi)
    print ("The occurrence of the largest number is", count)

main()
