#  File: Day.py

#  Description: A method to determine the day of the week diven the date

#  Student Name: Paul Benefiel

#  Student UT EID:  phb337

#  Course Name: CS 303E

#  Unique Number: 90110

#  Date Created: July 2nd, 2014

#  Date Last Modified: July 2nd, 2014

###########################################################################

def main():
    year, month, day = getDay()

    # Modify input for algorithm
    a = month - 12
    if 

def getDay():

    # This just gets into the loop that tests for valid input
    year = -1
    month = -1
    dayflag = True

    
    # Loop to check for valid year input
    while ( (year < 1900) or (year > 2100) ):

        year = eval (input ("Enter year: "))
        if (year > 2100 or year < 1900):
            print ("Invalid year - try again.")
            print ("")

    while ( (month < 1) or (month > 12) ):

        month = eval (input ("Enter month: "))
        if ( month > 12 or month < 1 ):
            print ("Invalid month - try again.")
            print ("")

    while (dayflag):

        day = eval (input ("Enter day: "))
        # Checks for valid day in 31 day months and sets dayflag to False if valid
        if ( (month == 1 or month == 3 or month == 5 or month == 7 or 
              month == 8 or month == 10 or month == 12) and (day >= 1 and 
                  day <= 31)):
            dayflag = False

        # Checks for valid day in 30 day months and sets dayflag to False if valid
        elif ( (month == 4 or month == 6 or month == 9 or month == 11)
             and (day >= 1 and day <= 30) ):
            dayflag = False

        # Checks for Febuary
        elif ( month == 2 ):
            # Checks for leap year
            if ( (month % 4 == 0 and month % 100 != 0) or (month % 400 = 0) ):
                leapyear = True
            else:
                leapyear = False

            # Checks for valid input if leap year
            if ( leapyear and (day >= 1 and day <= 29) ):
                dayflag = False
            # Checks for valid input if year isn't leap year
            elif ( not leapyear and (day >= 1 and day <= 28) ):
                dayflag = False
        # If dayflag is false, print error message and start over
        if (not dayflag):
            print ("Invalid day - try again.")
            print ("")

    return year, month, day

    year
