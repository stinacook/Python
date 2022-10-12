# Chapter 8: Functions
# Name: Kristina Billington
# Date: 28 SEP 2022

# Delivering Cookies!

# Import date time modules 
from datetime import date, datetime

# Create function count_cookie_boxes that returns dictionary value:

def count_cookie_result(qty_boxes, qty_cookies, type_cookies=""):
    """Return a dictionary of the cookie order"""
    order = {'boxes':qty_boxes, 'cookies':qty_cookies, 'type':type_cookies}
    return order

print('*' * 75) 
cookie_order = count_cookie_result(10, 12, 'oatmeal')
print(cookie_order)
print('*' * 75) 

# Input program to get user cookie order:

cookie_order = []
quiz_running = True
while quiz_running:
    type_cookies = input("What type of cookies do you have to deliver? ")
    type_cookies = type_cookies.title()
    qty_cookies = input("How many cookies in each box? ")
    qty_cookies = int(qty_cookies)
    if not qty_cookies > 0:                                                    
        print("Invalid user input. Please enter an integer more than 0.")
        continue 
    qty_boxes = input("How many boxes to you have? ")
    qty_boxes = int(qty_boxes)
    if not qty_boxes > 0:
        print("Invalid user input. Please enter an integer more than 0.")
        continue
    repeat = input('Do you have more cookies to deliver? Yes or No? ')
    
    repeat = repeat.upper()
    if repeat =='NO':
        quiz_running = False
    
    new_cookie_box = count_cookie_result(qty_boxes, qty_cookies, type_cookies)
    cookie_order.append(new_cookie_box)

print('*' * 75) 
#print(cookie_order)  #print dictionary to verify values are being stored
#print('*' * 75) 


# Function to generate printed order for user:

def report_Cookie_result(c_order):
    print('*' * 75) 

    # Calculate time and print values:
    today = date.today() 
    now = datetime.now()
    
    d2 = today.strftime("%B %d, %Y")
    print(f"COOKIE REPORT: {d2}\n")
    
    current_time = now.strftime("%H:%M")
    print(f'GENERATED: {current_time}\n')

    # Create format for Report Output:
    print('-' * 75)
    print("Cookie Type            Number of Boxes        Number of Cookies per Box\n")

    #Loops to iterate through dictionary and provide values:

    for i in c_order:
        print(f"{i['type']:<20}{i['boxes']:^24}{i['cookies']:^24}")

    x = 0
    for i in c_order:
        x = x + i['boxes']

    y = 0
    for i in c_order:
        y = y + i['cookies']
        z = y*x

    print('-' * 75)
    print(f"Total Number of Boxes: {x}\n")
    print(f'Total Number of Cookies: {z}\n')
    print("Have a Nice Day!")
    print('*' * 75) 

report_Cookie_result(cookie_order)