# Chapter 7: User Input and While Loops
# Name: Kristina Billington
# Date: 22 SEP 2022

# 7-1 Rental Car

rental_vehicle = input('Hello, what vehicle would you like to rent? ')
print(f'Let me see if I can find you a', rental_vehicle.title())

print('*' * 75)

# 7-2. Restaurant Seating

active = True
while active:
    party_size = input("What is the size of your dinner party? ")
    party_size = int(party_size)
    if (party_size >8):
        print("You will have to wait to be seated.") 
        active = False  
    else:
        print("Your table is ready.")
        break

print('*' * 75)         

# 7-3. Multiples of Ten

number = input('Please provide a number: ')
number = int(number)
if(number % 10 == 0):
    print("Your number is a multiple of 10.")
else:
    print("Your number is not a multiple of 10.")

print('*' * 75) 

# 7-5: Movie Tickets

active = True
while active:
    age = input("Hello, what is your age? ")
    age = int(age)
    if (age <3):
        print("Your admisssion is free.") 
        active = False
    elif (age <12 or age <3):
        print("Your admisssion is $10.00.") 
        active = False 
    else: 
        print("Your admisssion is $15.00.") 
        break

print('*' * 75) 

# 7-8. Deli

sandwich_orders = ['Ham & Cheese', 'Turkey & Swiss', "Club", 'Reuben', 'tuna']
finished_sandwiches =[]

while sandwich_orders:
    ordered_sandwich = sandwich_orders.pop()
    print(f'I made your {ordered_sandwich.title()} sandwich.')
    finished_sandwiches.append(ordered_sandwich)


print(f'I have made the following sandwiches: {finished_sandwiches}')

print('*' * 75) 

#7-9 No Pastrami

sandwich_orders2 = ['Ham & Cheese', 'pastrami', 'Turkey & Swiss', 'pastrami', "Club", 'Reuben', 'pastrami','tuna']
print(sandwich_orders2)
print(f'\nThe deli has run out of pastrami.\n')
while 'pastrami' in sandwich_orders2:
    sandwich_orders2.remove('pastrami')
print(sandwich_orders2)

print('*' * 75) 