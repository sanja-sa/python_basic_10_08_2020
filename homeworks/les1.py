''' Homework for Lesson 1
'''


#1 Basic
print(f"Paragraph 1")
name = "Vasja"
surname = "Pupkin"
age = 90
print(f"My name is {name} {surname}. I am {age} old.")

print('Can you tell about yourself.')
name = ""
while not name:
   name = input("Your name:")
   if not name:
      print("Please enter correct Name ( 'Name' cannot be empty )")

surname = ""
while not surname:
   surname = input("Your surname:")
   if not surname:
      print("Please enter correct 'Surname' ( 'Surname' cannot be empty )")

age = 0
while age <= 0 or age >= 150:
   try:
      age = int(input("Your age:"))
   except:
      print("Please enter correct 'Age' ( 'Age; must be only digits )")
print(f"It's great, {name} {surname}. You are not very old (only {age})")


#2 Time Format
print(f"\n\nParagraph 2")
seconds = 0
notCorrect = True
while notCorrect:
   try:
      seconds = int(input("Can you tell me how many seconds you need to run 10 km? "))
      notCorrect = False
   except:
      print("Please enter correct seconds ( only digits )")

hours = int(seconds/3600)
seconds -= hours*3600
minuts = int(seconds/60)
seconds -= minuts*60
print(f"Not so bad {name}, only {hours:>02}:{minuts:>02}:{seconds:>02}")


#3 Summ **
print(f"\n\nParagraph 3")
inDigit = 0
notCorrect = True
while notCorrect:
   try:
      inDigit = int(input("Can you tell me your lovely digit, maybe it 7? "))
      notCorrect = False
   except:
      print("Please enter correct 'Lovely digit' ( only digits )")

#Can use generators
two, three = [inDigit**(n+1) for n in range(1,3)]
print(f"You lovely digit is {inDigit}, and my is {inDigit+two+three}")

#Or lambda
#print(f"{(lambda x: x+x*x+x*x*x) (inDigit)}")

#Or out in 'f' calculating
#print(f"You lovely digit is {lovelyDigit}, and my is {lovelyDigit+lovelyDigit*lovelyDigit+lovelyDigit*lovelyDigit*lovelyDigit}")


#4 Max digit in digit
print(f"\n\nParagraph 4")
inDigit = 0
while int(inDigit/10) <= 0:
   try:
      inDigit = int(input("Can you tell me any positive digit more than 9? I show you focus. "))
   except:
      print("Please enter correct digit ( only digits )")
      continue
   if inDigit <= 9:
      print("Digit must be positive and > 9")

maxDigit = 0
while inDigit:
   rem = inDigit%10
   if rem > maxDigit:
      maxDigit = rem
   inDigit = int(inDigit/10)
print(f"MM.. Focus pocus krokus the biggest digit in your digit, is {maxDigit}. Do you like, this?")


#5
print(f"\n\nParagraph 5")
print(f"I can calculate profit of the organization if you can tell me more.")
proceed = 0
expense = 0
notCorrect = True
while notCorrect:
   try:
      proceed = int(input("What is proceed your org? "))
      notCorrect = False
   except:
      print("Please enter correct digit ( only digits )")
      
notCorrect = True
while notCorrect:
   try:
      expense = int(input("What is expense your org? "))
      notCorrect = False
   except:
      print("Please enter correct digit ( only digits )")

profit = proceed - expense
outData = f"""
OK. Your financial result is:
Proceed: \t{proceed} $
Expense: \t{expense} $
Profit: \t{profit} $
"""

if profit>=0:
   outData += f"Efficiency:\t{int(100*profit/proceed)} %"
else:
   outData += "\nSorry, efficiency of you organization is negative."
print(outData)

cntCoWorkers = 0
while cntCoWorkers <= 0:
   try:
      cntCoWorkers = int(input("Can you tell me count of co-workers in you organization ( >0 )? "))
   except:
      print("Please enter correct digit ( only digits )")
      continue   

print(f"Profit per co-worker: \t{profit/cntCoWorkers:0.2f}$")


#6
print(f"\n\nParagraph 6")
notCorrect = True
while notCorrect:
   try:
      a, b = input("Enter 2 digits for Athlete running: First day distance and Max overall result at day: ").split()
      a=int(a)
      b=int(b)
      notCorrect = False
   except:
      print("Please enter correct digit ( only digits )")

stopDay = 1
while a<b:
   stopDay+=1
   a+=a*0.1
print(f"Athlete can run not less than {b} km at {stopDay} day")

