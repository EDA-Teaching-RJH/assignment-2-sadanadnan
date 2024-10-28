### Part Two -- your code goes here. 
print("welcome to guessing game")
import random
print("pick a number b/w 1-100")
number = random.randint(1, 100)

while True:
    val = int(input("your guess is:"))
    if number > val:
        print("you guessed a number too low")

    elif number < val:
        print("you guess a number too high")
    
    else: 
        print(val, "is the right number!!! good job, you guessed it!!")
        break