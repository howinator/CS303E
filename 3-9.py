def main():
    name = input ("Employee Name: ")
    hours = eval (input ("Hours worked: "))
    rate = eval (input ("Pay rate: "))
    fed = eval (input ("Federal withholding rate: "))
    state = eval (input ("State withholding rate: "))

    gross = rate * hours
    fedgross = int(gross * fed * 100) / 100.0
    stategross = int(gross * state * 100) / 100.0
    totalded = fedgross + stategross
    net = gross - totalded

    print("")
    print("Employee Name:", name)
    print("Hours Worked:", hours * 1.0)
    print("Pay Rate: $", rate, sep='')
    print("Gross Pay: $", gross, sep='')
    print("Deductions:")
    print("  Federal Withholding (", fed * 100.0, "%): $", fedgross, sep='')
    print("  State Withholding (", state * 100.0, "%): $", stategross, sep='')
    print("  Total Deduction: $", totalded, sep='')
    print("Net Pay: $", net, sep='')

main()
