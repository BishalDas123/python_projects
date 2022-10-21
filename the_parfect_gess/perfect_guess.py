# guess by the computer for a rendom no 1 to 10
import random
Computer_chosen_no_is = random.randint(1,100)


#input name :
name= input("Enter your name : ")
attempt = 1



# first loop is handelling the error:
#for the 2nd it handeling function of game
while(True):
    try:
        guess_no =int(input(" Guess the closest no : "))
    except Exception as e :
          print("Enter a number only please")
    while(True):
        if guess_no > Computer_chosen_no_is:
                   guess_no = int(input(f"guess no is to high enter a *********** LOW value then {guess_no} : "))
                   attempt +=1
        elif guess_no < Computer_chosen_no_is:
                  guess_no = int(input(f"guess no is too low  enter a ************ HIGH value then {guess_no} : "))
                  attempt +=1
        else:
                 print(f"You Guess right in {attempt} attampts Now Write the value")
                 break
    break


# reading the high score
with open ("score_of_p_guess.txt","r") as f:
    high= f.read()
high_core = ""
for line in high:
    for i in line:
        if i.isdigit() == True:
            high_core += i

high_score = int(high_core)

#recording high score in txt file 
if attempt<high_score:
      with open ("score_of_p_guess.txt","w") as f:
           new_score= f.write(f"highest scorer name is : {name} and score is : {attempt}")
else:
    pass



# giving out-put 
with open ("score_of_p_guess.txt","r") as f:
    high= f.read()
if attempt>high_score:
     print(f"{high}\n\t your score is : {attempt} try next time")
else:
     print(f" your score is : {attempt} \n New Record set by {name} : score = {attempt}")





