import random
def game(Computer , my_input):
    if Computer == my_input:
        return None
    elif Computer == "rock":
        if my_input == "paper":
            return True
        elif my_input == "scissor" :
            return False
    elif Computer == "paper":
        if my_input== "scissor" :
            return True
        elif my_input == "rock":
            return False
    elif Computer == "scissor":
        if my_input == "rock":
            return True
        elif my_input == "paper":
            return False


random = random.randint(1,3)
if random == 1:
    computer = "rock"
elif random == 2:
    computer = "paper"
elif random == 3:
    computer ="scissor"


my_input = input("Enter rock ,paper or scissor : ")
print("Computer prints : ", computer)
a= game(computer , my_input)
if a ==None:
    print("Its a tie!!!!")
elif a==True:
    print('''You Win 
          *
         ***
        *****
       *******''')
elif a==False:
    print ("You Lose")


