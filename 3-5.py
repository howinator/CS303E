def main():
    import math
    n = eval (input ("Sides: "))
    s = eval (input ("Length: "))

    area = n * s * s / ( 4 * math.tan( math.pi / n ))

    print("Area is", area)

main()
