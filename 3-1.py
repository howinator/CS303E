def main():
  import math
  r = eval (input ("Enter length: "))
  s = 2 * r * math.sin(math.pi / 5)
  area = 3 * math.sqrt(3) / 2 * s * s
  print("Area is:", area)

main()
