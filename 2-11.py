def main():
    final = eval(input("Enter the final account value: "))
    annualrate = eval(input("Enter the anual interest rate in percent: "))
    numyears = eval(input("Enter the number of years: "))
    
    nummonths = numyears * 12
    monthlyrate = (annualrate / 12) / 100

    initial = final / ((1 + monthlyrate) ** nummonths)

    print ("Your initial deposit should be", initial)

main()
