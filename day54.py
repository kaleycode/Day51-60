import csv 

print("⭐️ Shop $$ Tracker ⭐️")
print()
with open("Day54Totals.csv") as file: 
  reader = csv.DictReader(file) 
  for row in reader:
    cost = float(row["Cost"])
    quantity = float(row["Quantity"])
    total = cost * quantity
    print(f"Your shop took £{round(total,2)} today.")
print()

total = 0.0
with open("Day54Totals.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    total += float(row["Quantity"]) * float(row["Cost"])
print(f"Total: ${round(total,2)}")