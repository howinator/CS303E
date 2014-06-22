def main():
    number = eval(input("Please enter an integer: "))
    thousands = number // 1000
    number = number - thousands * 1000
    hundreds = number // 100
    number = number -  hundreds * 100
    tens = number // 10
    number = number - tens * 10

    print(number)
    print(tens)
    print(hundreds)
    print(thousands)

main()
