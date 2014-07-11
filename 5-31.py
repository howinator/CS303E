def main():

    year = eval (input ("Enter the year: "))
    firstDayOfYear = eval (input ("Enter the first day of the year: "))

    yearString = str (year)

    month = "January"
    monthHeader = make_month_head (month, yearString)

    spacesBeforeFirstDay = " " * firstDayOfYear * 4
    monthString = spacesBeforeFirstDay


    monthBody = make_month_body (31, monthString)

    wholeMonth = monthHeader + monthBody
    print (wholeMonth)

def make_month_body (numDays, monthString):

    numDays += 1

    for day in range (1, numDays):

        if (day < 10):
            dayString = " " * 2 + str (day)
        else:
            dayString = " " * 1 + str (day)

        monthString = monthString + dayString + " "

        if (len (monthString) % 28 == 0):
            monthString = monthString + "\n"

    return monthString
        


def make_month_head (month, year):

    monthString = month + " " + year
    lengthOfMonthString = len (monthString)
    spacesAfterMonthString = 28 - 8 - lengthOfMonthString
    monthHeader = " " * 8 + monthString + " " * spacesAfterMonthString + "\n"
    monthHeader = monthHeader + "-" * 28 + "\n"
    monthHeader = monthHeader + "Sun Mon Tues Wed Thu Fri Sat \n"

    return monthHeader

main()
