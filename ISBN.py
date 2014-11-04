# File: IBN.py

# Description: A program to check the validity of a book's ISBN

# Student Name: Paul Benefiel

# Student UT EID: phb337

# Course Name: CS 303E

# Unique Number: 90110

# Date Created: July 30th, 2014

# Date Last Modified: July 30th, 2014

##############################################################################

def main():

    # Open the two files
    readFile = open('isbn.txt', 'r')
    writeFile = open('isbnOut.txt', 'w')

    # Start readings strings from files
    line = readFile.readline()
    while line:
        strIsValid = valid_string(line)
        line = line[:-1]

        # Proceed to algorithmic validity test if the string is correct
        if strIsValid:
            # change of variable names
            isbnList = strIsValid

            isAllValid = valid_isbn(isbnList)
            
            # Write output based on result of algorithm
            if isAllValid:
                writeFile.write(line + "  valid\n")
            else:
                writeFile.write(line + "  invalid\n")

        # Write output if incorrect string
        else:
            writeFile.write(line + "  invalid\n")

        # Read next line
        line = readFile.readline()

    # Clean up
    readFile.close()
    writeFile.close()

def valid_isbn(isbnList):

    # This function implements the simple algorithm to test the ISBN. 
    # I decided not to implement the recursive version.
    s1 = []
    s2 = []

    # Give the first elements their proper values
    s1.append(isbnList[0])
    s2.append(s1[0])

    # Run algorithm
    for i in range(1, len(isbnList)):
        s1Appendage = s1[i - 1] + isbnList[i]
        s1.append(s1Appendage)

        s1Appendage = s2[i - 1] + s1[i]
        s2.append(s1Appendage)
        
    # Test for validity
    if (s2[9] % 11 == 0):
        isValid = True
    else:
        isValid = False

    return isValid


def valid_string(inStr):
    # This function checks the validity of the string input to make sure it has
    # 9 decminal digits, a trailing 'X' or 'x', and hyphen. It also converts
    # the string into a list.
    # It accomplishes this by first storing the string in a list then parsing 
    # the list for validity.

    # Convert string to list
    inList = list(inStr)
    inList.pop()

    # Create new list with hypens removed
    outList = []
    for ch in range(len(inList)):
        if (inList[ch] != '-'):
            outList.append(inList[ch])

    # Check outList for validity

    # Is it of proper length?
    if (len(outList) != 10):
        return False

    # Is the last digit correct?
    if (outList[9] == 'X' or outList[9] == 'x' or (outList[9] >= '0' and 
            outList[9] <= '9')):
        pass
    else:
        return False

    # If last digit is X, correct to 10
    if (outList[9] == 'X' or outList[9] == 'x'):
        outList[9] = 10

    # Are the first 9 characters digits?
    for ch in range(len(outList[:9])):
        if (outList[ch] < '0' or outList[ch] > '9'):
            return False

    # Convert first 9 characters froms strings to ints
    for ch in range(len(outList)):
        outList[ch] = int(outList[ch])

    # If it passed above three tests, it's a valid ISBN and the list will be
    # returned to the main program

    return outList


main()
