def main():
    import time

    time = time.time()

    year, month, days, hours, minutes, seconds = convert_seconds(time)

    print ("Current date and time is ", month, " ", days, ", ", year, hours, ":", 
            minutes, ":", seconds)

def convert_seconds (time):

    secondsInYear = 365 * 24 * 60 * 60

    numYears = time // secondsInYear
    time -= time * numYears
    numYears += 1970


    if time < 2678400:
        month = "January"
        time -= 2678400
    elif (time < 5097600):
        month = "February"
        time -= 5097600
    elif (time < 7776000):
        month = "March"
        time -= 7776000
    elif (time < 10368000):
        time -= 10368000
        month = "April"
    elif (time < 13046400):
        time -= 13046400
        month = "May"
    elif (time < 15638400):
        time -= 15638400
        month = "June"
    elif (time < 18316800):
        time -= 18316800
        month = "July"
    elif (time < 20995200):
        time -= 20995200
        month = "August"
    elif (time < 23587200):
        time -= 23587200
        month = "September"
    elif (time < 26265600):
        time -= 26265600
        month = "October"
    elif (time < 28857600):
        time -= 28857600
        month = "November"
    elif (time < 31536000):
        time -= 31536000
        month = "December"
   
    numDays = time // (24 * 60 * 60)
    time -= numDays * (24 * 60 * 60)

    numHours = time // (60 * 60)
    time -= numHours * 60 * 60

    numMinutes = time // 60
    time -= numMinutes * 60

    return numYears, month, numDays, numHours, numMinutes, time

main()
