def main():
    minutes = eval(input("Enter the number of minutes: "))

    hours = minutes / 60
    days = hours // 24

    years = int(days // 365)
    daysinyear = int(days % 365)

    print(minutes, "minutes is approximately", years, "years and", 
            daysinyear, "days")

main()
