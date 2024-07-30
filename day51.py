import time, os

print("⭐️ Life Organizer To Do List ⭐️")
print()
print("Welcome to the life organizer.")
print()
toDoList = []
f = open("to.do", "r")
toDoList = eval(f.read())
f.close()
def prettyPrint():
  print()
  print(f"task: {task}")
  print(f"due by: {dueDate}")
  print(f"priority: {priority}")

while True:
  menu = input("What do you want to do: add, view, edit or remove? \n")
  if menu == "add":
    task = input("What is the task? ")
    dueDate = input("When is it due by? ")
    priority = input("What is the priority? ")
    toDoList.append(task)
    toDoList.append(dueDate)
    toDoList.append(priority)
    print("Thanks, this task has been added.")
    print()
  elif menu == "view":
    prettyPrint()
  elif menu == "edit":
    edit = input("What do you want to edit? ")
    if edit == "task":
      task = input("What is the task? ")
      toDoList.append(task)
    elif edit == "due date":
      dueDate = input("When is it due by? ")
      toDoList.append(dueDate)
    elif edit == "priority":
      priority = input("What is the priority? ")
      toDoList.append(priority)
    else:
      print("Invalid input.")
  elif menu == "remove":
    remove = input("What do you want to remove? ")
    if remove == "task":
      task = input("What is the task? ")
      toDoList.remove(task)

    elif remove == "due date":
      dueDate = input("When is it due by? ")
      toDoList.remove(dueDate)
    elif remove == "priority":
      priority = input("What is the priority? ")
      toDoList.remove(priority)
    else:
      print("Invalid input.")
  time.sleep(2.6)
  os.system("clear")
  f = open("to.do", "w")
  f.write(str(toDoList))
  f.close()