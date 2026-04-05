import random
number= random.randrange(10, 101,10)
attempts = 0
print("Welcom to number guessing Game ")
print("Enter any number in between 1 to 100")

while True:
    guess = int (input ("Enter youer Guess : "))
    except ValueError:
     print("Invalid input! \n please enter an integer.")
     continue
    attempts += 1
    if guess % 10 != 0:
       print(f"Plese enter number in multiples of 10 !")
       continue
    if  guess < number:
        print("Guess is low ")
    
    elif guess > number:

        print("Guess is high ")
    
    else: 
        print("CongratulationS \nYou guess the number{number}")
        print("Attempts : ",attempts)
        
        break

if__name__== "_main_":
number_guessing_game()
    
     
