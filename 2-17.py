def main():
    weight = eval(input("Enter weight in pounds: "))
    height = eval(input("Enter height in inches: "))

    weight *= 0.45359237
    height *= 0.0254

    bmi = weight / (height * height)

    print("BMI is", bmi)

main()
