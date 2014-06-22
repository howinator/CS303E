def main():
    ta = eval(input("Enter the temperature in Fahrenheit between -58 and 41: "
        ))
    v = eval(input("Enter the windspeed in miles per hour above 2 mph: "))

    twc = 35.74 + 0.6215 * ta - 35.75 * v ** .16 + 0.4275 * ta * v ** .16

    print("The wind chill index is", twc)

main()
