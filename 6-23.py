def convertMillis (millis):
    hours = millis // 3600000
    millis -= hours * 3600000

    minutes = millis // 60000
    millis -= minutes * 60000

    seconds = millis // 1000
    
    time = str (hours) + ":" + str (minutes) + ":" + str (seconds)

    return time

def main():
    mil = eval (input ("Enter the number of milliseconds: "))

    time = convertMillis (mil)

    print (time)

main()
