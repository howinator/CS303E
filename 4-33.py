def main():
    dec = eval (input ("Enter decimal value (0 to 15): "))
    if (dec <= 9 and dec >= 0):
        print ("The hex value is", dec)
    elif (dec == 10):
        print ("The hex value is A")
    elif (dec == 11):
        print ("The hex value is B")
    elif (dec == 12):
        print ("The hex value is C")
    elif (dec == 13):
        print ("The hex value is D")
    elif (dec == 14):
        print ("The hex value is E")
    elif (dec == 15):
        print ("The hex value is F")
    elif (dec <= 0 or dec > 15):
        print ("Invalid input")

main()
