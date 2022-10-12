from multiprocessing.sharedctypes import Value
import random

x =(random.randint(1,100))  
count = 0
while x:
    num1 = input("Please enter a number between 1 and 100.   ")
    num1 = int(num1)
    if num1 >  x:                                                    
        print("Your number is too high, please guess again.\n")
        count += 1
        continue 
    if num1 < x:
        print("your number is too low, please guess again.\n")
        count += 1
        continue
    else:
        print(f"\nYour guess of {x} is correct! You took {count} guesses.")
        break
    










