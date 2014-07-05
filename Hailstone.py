# File: Hailstone.py

# Description: An algorithm to find the cycle length of the hailstone sequence
#              across a given range

# Student Name: Paul Benefiel

# Student UT EID: phb337

# Course Name: CS 303E

# Unique Number: 90110

# Date Created: July 4th, 2014

# Date Last Modified: July 4th, 2014

def main():
    # Start by setting up loop to get good input
    inputCorrect = False
    while ( not inputCorrect ):
        start = eval (input ("Enter starting number of the range: "))
        end = eval (input ("Enter ending number of the range: "))
        
        # Check for correct input - set input flag to true if correct
        if ( start > 0 and end > 0 and start < end ):
            inputCorrect = True
        else:
            print ("\nIncorrect input - please try again\n")

    # Now, we run the algorithm - keeping track of the cycle length of the
    # longest number along with the actual number
    longestCycleLength = 0
    for number in range (start, (end + 1)):
        thisIterNumber = number
        thisCycleLength = 0

        # Enter the loop that does the actual operations 
        while (number != 1):
            if ( number % 2 == 0 ):
                number = number // 2
            else:
                number = number * 3 + 1

            thisCycleLength += 1

            # if this cycle is longer than the longest thusfar, replace the 
            # longest with the length of this cycle
            if (thisCycleLength > longestCycleLength):
                longestCycleLength = thisCycleLength
                longestCycleNumber = thisIterNumber
    
    # Output result to screen
    print ("The number ", longestCycleNumber, 
            " has the longest cycle length of ", longestCycleLength, ".", 
            sep = "")

main()

