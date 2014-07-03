def main():
    cntr = 0
    for num in range(100,201):
        if ((num % 5 == 0 or num % 6 == 0) and (num % 30 != 0)):
            cntr += 1
            if (cntr > 10):
                print ("")
                cntr = 1
            print (num, end = " ")
    print ("")

main()

