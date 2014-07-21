# File: CalculatePI.py

# Description: A program to calculate pi using a Monte Carlo Algorithm

# Student Name: Paul Benefiel

# Student UT EID: phb337

# Course Name: CS 303E

# Unique Number: 90110

# Date Created: July 20th, 2014

# Date Last Modified: July 20th, 2014

##############################################################################

from random import uniform
import math

def computePI ( numThrows ):

    # Set counter for number of positions inside the circle to zero
    numInsideCircle = 0
    # Begin iteration through number of desired iterations
    for iteration in range (numThrows):

        # Get random positions
        xPos = uniform (-1.0, 1.0)
        yPos = uniform (-1.0, 1.0)

        # Calculate distance from origin
        distance = math.hypot (xPos, yPos)

        # If inside the circle, add one to inside circle counter
        if distance < 1:
            numInsideCircle += 1
    
    # Ratio of inside circle to number of throws is pi/4, so multiply by 4
    computedPI = numInsideCircle / numThrows * 4

    return computedPI

def main():

    # computePI is first called for 100 iterations
    iterations = 100
    maxIterations = 10000000

    # Loop is run until max iterations is reached
    while (iterations <= maxIterations):

        computedPI = computePI (iterations)
        
        # difference between computed pi and "true" pi
        difference = math.pi - computedPI

        # The difference string is made depending on if it's positive or negative
        if difference >= 0:
            differenceStr = "+" + format (difference, "8.6f")
        else:
            differenceStr = format (difference, "8.6f")

        # The string to be printed to the terminal is composed
        outStr = format ("num = ", "<6s") + format (iterations, "<8d") + "  " \
                 + "Calculated PI = " + format (computedPI, "8.6f") + "  " \
                 + "Difference = " + differenceStr

        print (outStr)
        
        # Define the next number of iterations
        iterations *= 10

main()


