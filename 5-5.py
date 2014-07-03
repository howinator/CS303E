def main():
    print ("Kilograms    Pounds    |    Pounds    Kilograms")
    for i in range(0, 100):
        kilosleft = 2 * i + 1
        poundsleft = kilosleft * 2.2
        poundsright = 5 * i + 20
        kilosright = poundsright / 2.2
        print (format (kilosleft, "<12d"), format (poundsleft, "<9.1f"), 
                "|    ", format (poundsright, "<9d"), 
                format(kilosright, "<8.2f") )



main()

