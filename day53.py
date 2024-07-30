import os, time

inventory = []
try:
  f = open("inventory.txt", "r")
  inventory = eval(f.read())
  f.close()
except:
  pass

def addItem():
  time.sleep(1.5)
  os.system("clear")
  print("INVENTORY")
  print("=========")
  print()
  item = input("Item to add > ").capitalize()
  inventory.append(item)
  print("Your item was added to your inventory.")

def viewItem():
  time.sleep(1)
  os.system("clear")
  print("INVENTORY")
  print("=========")
  seen = []
#short way: 
  seen = set(inventory)
  for item in seen:
    print(f"{item}:\nYou have {inventory.count(item)} of this item")
    time.sleep(1.5)
# or the longer way:
#  seen = []
# for item in inventory:
    #if item not in seen:
      #print(f"{item} {inventory.count(item)}")
     #seen.append(item)
   
def removeItem():
  time.sleep(1.5)
  os.system("clear")
  print("INVENTORY")
  print("=========")
  print()
  item = input("Item to remove > ").capitalize()
  if item in inventory:
    inventory.remove(item)
    print("Your item was removed from your inventory.")
  elif item == "all":
    inventory.clear()
    print("Your inventory was cleared.")
  else:
    print("You do not have that item.")

while True:
  time.sleep(1)
  os.system("clear")
  print("Day 53:")
  print("INVENTORY")
  print("=========")
  menu = input("Enter 1 to add\nEnter 2 view\nEnter 3 to remove\n> ")
  if menu == "1":
    addItem()
  elif menu == "2":
   viewItem()
  elif menu == "3":
   removeItem()
  f = open("inventory.txt", "w")
  f.write(str(inventory))
  f.close()
