def sqrt (n):
    lastGuess = 1
    eps = 1
    while (eps > 0.0001):
        nextGuess = (lastGuess + (n / lastGuess)) / 2
        eps = abs (nextGuess - lastGuess)
        lastGuess = nextGuess
    return nextGuess

def main():
    num = eval (input ("Enter a number: "))
    result = sqrt (num)
    print (result)

main()
