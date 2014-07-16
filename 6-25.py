def main():

    numEmirps = 50
    numEmirpsPerLine = 10
    count = 0
    num = 2

    while count < numEmirps:

        isPrime = find_prime (num)

        if isPrime:
            isEmirp

def find_prime(number):

    isPrime = True

    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            isPrime = False
            break
        divisor += 1

    return isPrime

def find_emirp(number):


