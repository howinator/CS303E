def main():
    inp = eval(input("Enter the monthly saving amount: "))

    savings = inp
    rate = 1.00417

    savings *= rate
    savings += inp
    savings *= rate
    savings += inp
    savings *= rate
    savings += inp
    savings *= rate
    savings += inp
    savings *= rate
    savings += inp
    savings *= rate

    print("After the sixth month, the account value is", savings)

main()
