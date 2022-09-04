import random


no_is = random.randint(1,100)
guess_no=int(input(" Guess the No closest no : "))
attempt=1
while(True):
    if guess_no > no_is:
          guess_no = int(input("guess no is to high enter a low value"))
          attempt +=1
    elif guess_no < no_is:
          guess_no = int(input("guess no is too low  enter a high value"))
          attempt +=1
    else:
         print(f"You Guess right in {attempt} Now Write the value")
         break

def sum(a,b):
    c= a+b
    return c
