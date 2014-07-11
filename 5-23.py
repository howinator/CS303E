def main():

    loanAmount = eval (input ("Loan Amount: "))
    numYears = eval (input ("Number of Years: "))

    header = "Interest Rate   Monthly Payment   Total Payment"
    print (header, "\n")
    for interestIncrement in range (0, 25):
        monthlyRate = 5 + interestIncrement / 8
        
        monthlyRate = monthlyRate / 1200
        monthlyPayment = loanAmount * monthlyRate / ( 1 
                         - 1 / (1 + monthlyRate) ** (numYears * 12))
        totalPayment  = monthlyPayment * 12 * numYears
        
        yearlyRate = format (monthlyRate * 1200, "5.3f")
        monthlyPayment = format (monthlyPayment, "6.2f") 
        totalPayment = format (totalPayment, "9.2f")

        iString = str (yearlyRate) + "%"
        mString = str (monthlyPayment)
        tString = str (totalPayment)

        print (iString, " " * 8, mString, " " * 10, tString)

main()
