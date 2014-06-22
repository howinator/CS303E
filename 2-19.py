def main():
    invstamnt = eval(input("Enter investment amount: "))
    anintrate = eval(input("Enter annual interest rate: "))
    numyears = eval(input("Enter number of years: "))

    nummonths = numyears * 12
    mointrate = anintrate / 12 / 100

    print("Accumulated value is", invstamnt * (1 + mointrate) ** nummonths)

main()
