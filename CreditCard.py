# File: CreditCard.py

# Description: 1) Checks the validity of a credit card number.
#              2) If valid, the program returns the type of card

# Student Name: Paul Benefiel

# Student UT EID: phb337

# Course Name: CS 303E

# Unique Number: 90110

# Date Created: July 16th, 2014

# Date Last Modified: July 16th, 2014

##############################################################################

def is_valid (ccStr):
    ccSum = 0
    # Parse the string character by character
    for char in range (len (ccStr)):
        ccDigit = int (ccStr[char])
        
        # If it is odd, take care of the mulltiplicationa and addition of edits
        if ((char + 1) % 2 != 0):
            ccDigit *= 2

            # If the multiplication resulted in a 2 digit number, add digits
            if (len (str (ccDigit)) == 2):
                ccDigit = int (str (ccDigit)[0]) + int (str (ccDigit)[1])

        # Add the digit to the sum now that the odd case is taken care of
        ccSum = ccSum + ccDigit

        # Since this loop is parsing the string, grab the IIN from the first
        # four digit
        if char == 0:
            d15 = ccStr[char]
        elif char == 1:
            d14 = ccStr[char]
        elif char == 2:
            d13 = ccStr[char]
        elif char == 3:
            d12 = ccStr[char]
            
    if ccSum % 10 == 0:
        return True, d12, d13, d14, d15
    else:
        return False, d12, d13, d14, d15



def cc_type (d12, d13, d14, d15):

    # Make ints of the first two, three or four digits since 
    # those three numbers matter for checking
    first = int (d15)
    firstTwo = int (d15 + d14)
    firstThree = int (d15 + d14 + d13)
    firstFour = int (d15 + d14 + d13 + d12)

    if (firstTwo == 34 or firstTwo == 37):
        ccCompany = "American Express"
    elif (firstFour == 6011 or firstThree == 644 or firstTwo == 65):
        ccCompany = "Discover"
    elif (firstTwo >= 50 and firstTwo <= 55):
        ccCompany = "MasterCard"
    elif first == 4:
        ccCompany = "Visa"
    else:
        ccCompany = ""

    return ccCompany

def main():

    # Read in credit card number
    cardNumber = input ("Enter 15 or 16-digit credit card number: ")

    lengthCCNumber = len (cardNumber)
    # Check if 15 or 16 digit number
    if (lengthCCNumber < 15 or lengthCCNumber > 16):
        print ("Not a 15 or 16-digit number")
        return

    # Call validity checking class
    ccIsValid, d12, d13, d14, d15 = is_valid (cardNumber)

    # If the number is valid, find what type of card
    if ccIsValid:
        ccCompany = cc_type (d12, d13, d14, d15)
        if ccCompany == "":
            print (ccCompany)
        else:
            print ("Valid", ccCompany, "credit card number")
    else:
        print ("Invalid credit card number")



main()
