def main():
    today = eval (input ("Today: "))
    future = eval (input ("Future: "))
    if (today == 0):
        tostr = 'Sunday'
    elif (today == 1):
        tostr = 'Monday'
    elif (today == 2):
        tostr = 'Tuesday'
    elif (today == 3):
        tostr = 'Wednesday'
    elif (today == 4):
        tostr = 'Thursday'
    elif (today == 5):
        tostr = 'Friday'
    else:
        tostr = 'Saturday'

    future += today
    if (future >= 7):
        future %= 7

    if (future == 0):
        fustr = 'Sunday'
    elif (future == 1):
        fustr = 'Monday'
    elif (future == 2):
        fustr = 'Tuesday'
    elif (future == 3):
        fustr = 'Wednesday'
    elif (future == 4):
        fustr = 'Thursday'
    elif (future == 5):
        fustr = 'Friday'
    else:
        fustr = 'Saturday'

    print("Today is", tostr, "and the future day is", fustr)

main()
