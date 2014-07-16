def main():

    numEmirps = 100
    numEmirpsPerLine = 10
    count = 0
    num = 12
    
    while count < numEmirps:

        isPrime = find_prime (num)

        if isPrime:

            if find_emirp (num):
                count += 1

                print(format(num, "5d"), end = '')
                if count % numEmirpsPerLine == 0:
                    print()

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

def find_emirp(number):
    
    isEmirp = True
    numStr = str (number)
    rvrString = numStr[::-1]

    if numStr == rvrString:
        return False

    rvrInt = int (rvrString)

    if not find_prime(rvrInt):
        isEmirp = False

    return isEmirp
main()
