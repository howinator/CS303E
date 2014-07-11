def main():
    pyramidString = ""
    lines = 8

    for line in range (0, (lines + 1)):
        thisLine = " " * 4 * (lines - line)
        
        for place in range (0, line):
            thisPosition = str (2 ** place)

            nextPosition = 2 ** (place + 1)
            if (place == (line - 1)):
                thisPosition = thisPosition
            elif (nextPosition < 10):
                thisPosition = thisPosition + "   "
            elif (nextPosition >= 10 and nextPosition < 100):
                thisPosition = thisPosition + "  "
            else:
                thisPosition = thisPosition + " "

            thisLine = thisLine + thisPosition

        for place in range ((line - 1), 0, -1):
            thisPosition = str (2 ** (place - 1))
            
            thisPositionNum = 2 ** (place - 1)
            if (thisPositionNum < 10):
                thisPosition = "   " + thisPosition
            elif (thisPositionNum >= 10 and thisPositionNum < 100):
                thisPosition = "  " + thisPosition
            else:
                thisPosition = " " + thisPosition

            thisLine = thisLine + thisPosition


        thisLine = thisLine + "\n"
        pyramidString = pyramidString + thisLine

    print (pyramidString)

main()
