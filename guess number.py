

import random

number= random.randrange(10, 101,10)
attempts = 0
print("welcom to number gessing Game ")
print("Enter any number in between 1 and 100")

while True:
    guess = int (input ("Enteer youer Guess : "))
    attempts += 1
    if guess % 10 != 0:
       print("Plese enter number in multiples of 10 !")
       continue
    if  guess < number:
        print("Guess is low ")
    
    elif guess > number:

        print("Guess is high ")
    
    else: 
        print("congratulation,you guess the number",number)
        print("Attempts : ",attempts)
        
        break
    
     