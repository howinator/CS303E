#  File: EasterSunday.py

#  Description: Uses algorithm by Gauss to find Easter Sunday for a given year.

#  Student Name: Paul Benefiel

#  Student UT EID: phb337

#  Course Name: CS 303E

#  Unique Number: 90110

#  Date Created: June 23rd, 2014

#  Date Last Modified: June 23rd, 2014

############################################################################

def main():
  # Gets the year from the user and assumes valid input
  y = eval ( input ( "Enter year: ") )

  # START OF ALGORITHM
  # Step 2
  a = y % 19

  # Step 3
  b = y // 100
  c = y % 100
  
  # Step 4
  d = b // 4
  e = b % 4
  
  # Step 5
  g = ( 8 * b + 13 ) // 25
  
  # Step 6
  h = ( 19 * a + b - d - g + 15) % 30
  
  # Step 7
  j = c // 4
  k = c % 4
  
  # Step 8
  m = ( a + 11 * h ) // 319
  
  # Step 9
  r = ( 2 * e + 2 * j - k - h + m + 32 ) % 7
  
  # Step 10
  n = ( h - m + r + 90) // 25
  
  # Step 11
  p = ( h - m + r + n + 19 ) % 32

  # END ALGORITHM
  # Now the result is output to the terminal

  if ( n == 3):
    print("In", y, "Easter Sunday is on", p, "March.")
  else:
    print("In", y, "Easter Sunday is on", p, "April.")

main()
