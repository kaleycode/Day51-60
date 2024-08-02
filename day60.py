import datetime, time, os
today = datetime.date.today() 
print("🎉⭐️ Day 60: Event Countdown! ⭐️🎉")
print()

halloween = datetime.date(year = 2024, month = 10, day = 31) 
newYears = datetime.date(year = 2025, month = 1, day = 1)
christmas = datetime.date(year = 2024, month = 12, day = 25)
valentine = datetime.date(year = 2024, month = 2, day = 14)

print("Enter your birthday! ")
yourBirthYear = int(input("Year: "))
yourBirthMonth = int(input("Month: "))
yourBirthDay = int(input("Day: "))

yourbirthday=datetime.date(year=yourBirthYear,month= yourBirthMonth, day = yourBirthDay)

birthDiff = today - yourbirthday

if yourbirthday < today:
  print(f"You were born {birthDiff.days} days ago!")
  print()
else:
  print("Happy Birthday!")
  time.sleep(0.7)
print()

halloweenDiff = halloween - today
print(f"Halloween is in {halloweenDiff.days} days! 🎃👻")
print()
time.sleep(0.7)

newYearsDiff = newYears - today
print(f"New Years is in {newYearsDiff.days} days! 🎊🎉")
time.sleep(0.6)
print()
christmasDiff = christmas - today
print(f"Christmas is in {christmasDiff.days} days! 🎄🎅")
print()
time.sleep(0.7)

valentineDiff = today - valentine
print(f"Valentine's Day was {valentineDiff.days} days ago! I hope you had a great day! ❤️")
print()
time.sleep(0.6)

birthday = datetime.date(year = 2024, month= yourBirthMonth, day = yourBirthDay)
birth = today - birthday

nextBirthday = datetime.date(year = 2025, month= yourBirthMonth, day = yourBirthDay)
next = nextBirthday - today

if birthday == today:
  print("Happy Birthday!")
  print()
  time.sleep(0.6)
elif birthday > today:
  print(f"⏰ It's not your birthday yet! You have {birth.days} days left! ⏰")
  print()
  time.sleep(0.6)
else:
  print(f"Your last birthday was {birth.days} days ago! ⭐️")
  time.sleep(0.6)
  print()
  print(f"🎉 Your next birthday is in {next.days} days! 🎉")
