# File: Books.py

# Description: A program to analyze the vocabulary expressed in a book

# Student Name: Paul Benefiel

# Student UT EID: phb337

# Course Name: CS 303E

# Unique Number: 90110

# Date Created: August 13th, 2014

# Date Last Modified: August 13th, 2014

###############################################################################

# Global variable for master list of words
word_dict = {}
def create_word_dict ():
    # This function creates the word dictionary from the master list of words
    # used by Scrabble players. The file with this master list is hard-coded
    # into the program as "words.txt".
    
    # Begin by opening the file and reading the first line
    masterFile = open ("words.txt", "r")
    line = masterFile.readline()

    # Go through the file line-by-line and add the words to the dictionary
    while line:
        line = line.rstrip()
        word_dict[line] = 1
        line = masterFile.readline()

    # The dictionary is now populated with a dictionary of the master list, 
    # so we close the file.

    masterFile.close()


def parse_string (inptStr):
    # This function is called exclusively by get_word_freq. It takes in a 
    # string, usually a line from the file and parses it to remove punctuation 
    # and the like. This function creates a blank string and adds characters 
    # from the input string according to the specification.

    outStr = ""
    lenStr = len (inptStr)

    # Strip the newline character
    inptStr.rstrip()

    # Replace all hyphens and dashes with a space - count is length of string
    inptStr.replace("-", " ", lenStr)

    # Check if line ends with ' or "'s"
    if inptStr.endswith("'"):
        inptStr = inptStr[:-1]
    elif inptStr.endswith("'s"):
        inptStr = inptStr[:-2]

    # Re-determine the length of the string
    lenStr = len (inptStr)

    # Go through string adding alphabetic characters, spaces, and valid 
    # apostrophes to the output string.
    for i in range (lenStr):
        ch = inptStr[i]
        nextCh = inptStr[i + 1]

        # Test for alphabetic character or space
        if ch.isalpha() or ch.isspace():
            outStr = outStr + ch
        # Check if aposrophe is proceeded by character besides s. If proceeded
        # by s, outStr has nothing added to it.
        elif ch == "'" and nextCh != "s":
            outStr = outStr + ch
        elif ch == "'" and nextCh == "s":
            outStr = outStr
        # Finally, anything else is replaces with a space.
        else:
            outStr = outStr + " "

    return outStr
    """
    # This loop goes through the string character-by-character. For each 
    # character, it sets an "output character" equal to a blank string if
    # the character is to be removed or to a space if it is to be replaced with 
    # a space.
    for i in range (inptStr):
        # Create black output character, make variables for the previous, 
        # current, and next characters.

        outChr = ""
        prevCh = inptStr[i - 1]
        ch = inptStr[i]
        nextCh = inptStr[i + 1]

        # Test if character is an alphabetic chacter. s is excluded because it
        # may be removed if it is preceded by an apostrophe and proceeded by a 
        # new-line character
        if (ch.isalpha() and ch != "s"):
            outChr = ch

        # Test if character is a space
        elif (ch.isspace()):
            outChr = ch

        # Test of character is a punctuiation mark besides an apostrophe
        elif ((ch >= "!" and ch <= "@" and ch != "'") 
                or (ch >= "[" and ch <= "`") or (ch >= "{" and ch <= "~")):
            outChr = " "

        # Run rules for apostrophes
        elif (ch == "'" and nextCh != "s"):
            outChr = ch
        elif (ch == "'" and (nextCh == "s" or nextCh == "\n")):
            outChr = ""

        # Run rules for an s
        elif (ch == "s" and prevCh == "'" and nextCh = "\n"):
            outChr = ""
        """
def get_word_freq (fileName):
    # This function is called directly from main and it in-turn calls 
    # parse_string. The function takes fileName as a formal parameter, which is
    # a string. As it reads through the file line-by-line, it passes the string 
    # for the line to parse_string. parse_string cleans it up, and passes the 
    # cleaned string back to this function.

    bookFile = open (fileName, "r")

    # Start reading through the file
    line = bookFile.readline()
    while line:
        line = parse_string (line)

def main():

    # Create word dictionary from master list of English words
    create_word_dict()

    # Enter the names of the two files which contain the two books
    book1 = input ("Enter name of first book: ")
    book2 = input ("Enter name of second book: ")
    print()

    # Enter the names of the two authors
    author1 = input ("Enter last name of first author: ")
    author2 = input ("Enter last name of second author: ")
    print()

    # Get the frequency of words used by the two authors
    wordFreq1 = getWordFreq (book1)
    wordFreq2 = getWordFreq (book2)

    # Compare the relative frequency of uncommon words used by the two authors
    wordComparison (author1, wordFreq1, author2, wordFreq2)

main()
