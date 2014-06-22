def main():
    sub, rate = eval(input("Enter the subtotal and rate: "))

    rate = rate / 100
    gratuity = sub * rate
    total = sub + gratuity

    print("The gratuity is", int(gratuity * 100) / 100.0, "and the total is", 
            int(total * 100) / 100.0)

main()
