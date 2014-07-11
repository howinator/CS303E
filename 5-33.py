def main():
    monthYield = eval (input ("Enter initial deposit amount: "))
    annualPercent = eval (input ("Enter annual percentage: "))
    period = eval (input ("Enter maturity period in months: "))

    print ("Month CD Value")
    for month in range (1, (period+1)):
        monthYield = monthYield + monthYield * annualPercent / 1200
        if month < 10:
            print (month, "   ", format (monthYield, "8.2f"))
        else:
            print (month, "  ", format (monthYield, "8.2f"))

main()
