print("⭐️ Day 57: Factorial Finder ⭐️")
def factorial(value):
  if value == 1:
    return 1
  else:
    return value * factorial(value - 1)

input = int(input("Input a number > "))
factorial(input)
print(f"The factorial of {input} is {factorial(input)}")
