def main():

    num = 2
    while num < 998:
        firstIsPrime = find_prime (num)
        if firstIsPrime:
            secondIsPrime = find_prime (num + 2)
        if secondIsPrime:
            print ( '(' + str(num) + ', ' + str(num + 2) + ')', sep='')
            secondIsPrime = False

        num += 1


def find_prime(number):

    isPrime = True

    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            isPrime = False
            break
        divisor += 1
    return isPrime

main()
