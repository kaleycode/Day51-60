import os, time

def palindrome(word):
  if len(word)<=1:
    return True
  if word[0] != word[-1]:
    return False
  return palindrome(word[1:-1])
while True:
  print("⭐️ Palindrome Checker ⭐️")
  print()
  word = input("Enter a word: ").lower()
  print()
  if palindrome(word) == True:
    print(f"{word} is a palindrome! Yay!")
    print()
    time.sleep(2)
    os.system("clear")
  else:
    print(f"{word} is not a palindrome. Sorry!")
    print()
    time.sleep(2)
    os.system("clear")