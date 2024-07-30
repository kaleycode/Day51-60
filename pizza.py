
pizza = {}
def prettyPrint():
  print(f"\tName\tTopping\t\tSize(in)")
  print()
  for key, value in pizza.items():
    print(f"""{key:^10}|{value["topping"]:^10}|{value["size"]:^10}""")
    print()
    print()
    print("And your total is going to be", total, "dollars")
    print()
while True:
  print()
  print("🌟Dave's Dodgy Pizzas🌟")
  print()
  print("What is your name and order? ")
  print()
  name = input("Name > ").title()
  topping = input("Topping > ").title()
  size = int(input("Size in inches(6, 8, 12, 16, 24, 30) > "))
  quantity = int(input("How many pizzas are you ordering? > "))
  total = size * quantity
  pizza[name] = { "topping": topping, "size": size, "quantity": quantity}
  print("-----------------------")
  print()
  prettyPrint()