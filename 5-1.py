def main():
    inpt = 1
    pos = 0
    neg = 0
    total = 0
    avg = 0
    num = 0
    while (inpt):
        inpt = eval( input ("Enter integer, 0 to exit: "))
        if inpt > 0:
            pos += 1
            total += inpt
            num += 1
        elif inpt < 0:
            neg += 1
            total += inpt
            num += 1
        elif inpt == 0 and num == 0:
            print ("You didn't enter any number")
        else: 
            avg = total / num

    print ("The number of positives is", pos)
    print ("The number of negatives is", neg)
    print ("The total is", total)
    print ("The average is", avg)

main()
