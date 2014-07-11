def main():
    for mult in range (1, 11):
        pi = 0
        maxi = mult * 10000
        for i in range (1, (maxi + 1)):
            pi = pi + 4 * ( (-1)  ** (i + 1) / (2 * i - 1) )
        print (pi)

main()
