def main():
    tuition = 10000
    total = 0
    for year in range(1, 14):
        tuition  *= 1.05
        if (year == 10):
            print ("Tution in 10 years is", tuition)
        if (year >= 10):
            total += tuition
    print ("The total cost of tuition is", total)

main()
