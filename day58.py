import random, os, time
totalAttempts = 0

def game():
  attempts = 0
  
  number = random.randint(1,100)
  while True:
    guess = int(input("Pick a number between 1 and 100: "))
    if guess > number:
      print("Too high")
      attempts+=1
    elif guess < number:
      print("Too low")
      attempts+=1
    else:
      print("Just right!")
      print(f"{attempts} attempts this round")
      return attempts

while True:
  menu = int(input("1: Guess the random number game\n2: Total Score\n3: Exit\n> "))
  if menu == 1:
    totalAttempts += game()
    time.sleep(2)
    os.system("clear")
  elif menu == 2:
    print(f"Total attempts: {totalAttempts}")
    time.sleep(2)
    os.system("clear")
  elif menu == 3:
    break 
  else:
    print("Invalid input")
    time.sleep(2)
    os.system("clear")
