def main():
    lines = eval (input ("Enter the number of lines: "))

    pyramidstring = ""
    for line in range(1, (lines + 2)):
        thisline = " " * 3 * (lines - line + 1)
        
        for position in range((line - 1), 1, -1):
            positionstring = ""
            if position < 10:
                positionstring = " "
            positionstring = positionstring + str(position)
            thisline = thisline + positionstring + " "

        for position in range(1, line):
            positionstring = ""
            if position < 10:
                positiionstring = " "
            positionstring = positionstring + str(position)
            thisline = thisline + positionstring + " "

        thisline = thisline + "\n"
        pyramidstring = pyramidstring + thisline

    print (pyramidstring)
main()
