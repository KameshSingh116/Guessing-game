#Radhe Radhe
#Basic python program to guess the number chosen by the random function
import random
guess=random.randint(0,11)
print("You have 3 attempts only!!!")
print(guess)
tries=2
while tries>-1:
    your_guess=int(input("Enter your guess between from 0 to 10:"))
    tries-=1
    if(tries==0):
        print("Think Carefully ! This is your last chance!")
    if your_guess==guess:
        print("You got it right buddy!")
        break
    else:
        if tries==1 or tries==2:
              print("Try again you have %d tries left!" %tries)
        elif tries<0: 
            print("Better luck next time!")
#Radhe Radhe