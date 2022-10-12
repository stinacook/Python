# Chapter 9: Classes
# Name: Kristina Billington
# Date: 5 OCT 2022

# 9-1. Restaurant

print('-' * 75)

class Restaurant:
    """A simple attempt to model a restaurant"""
    def __init__(self, name, cuisine_type):
        """Initialize restaurant attributes"""
        self.name = name.title()
        self.cuisine_type = cuisine_type.title()
    
    def describe_restaurant(self):
        """Description of the restaurant"""
        print(f"\n{self.name} has wonderful {self.cuisine_type} food!\n")
    
    def open_restaurant(self):
        """State that status of the restaurant"""
        print(f"{self.name} is open today!")
    

restaurant = Restaurant("bayou betty", "cajun")
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

print('-' * 75) 

# 9-2. Three Restaurants:

bayou_betty = Restaurant("bayou betty", "cajun")
bayou_betty.describe_restaurant()

pesky_pescado = Restaurant("pesky pescado", "dockside bistro")
pesky_pescado.describe_restaurant()

smor_smorgas = Restaurant("s'mor smorgas", "swedish sandwich")
smor_smorgas.describe_restaurant()

print('-' * 75) 

# 9-4: Number served-

class Restaurant2:
    """A simple attempt to model a restaurant"""
    def __init__(self, name, cuisine_type):
        """Initialize restaurant attributes"""
        self.name = name.title()
        self.cuisine_type = cuisine_type.title()
    
    def describe_restaurant(self):
        """Description of the restaurant"""
        print(f"\n{self.name} has wonderful {self.cuisine_type} food!\n")
    
    def open_restaurant(self):
        """State that status of the restaurant"""
        print(f"{self.name} is open today!")
    
    def number_served(self, number_served):
        """Describes the number of customers that have been served"""
        self.number_served = number_served
    
    def increment_number_served(self, additional_served):
        """adds additional customer count"""
        self.number_served += additional_served

restaurant = Restaurant2('pesky pescado', 'dockside bistro')
restaurant.describe_restaurant()

restaurant.number_served = (0)
print(f"\nNumber served initially: {restaurant.number_served}")

restaurant.number_served = (125)
print(f"Number served midday: {restaurant.number_served}")

restaurant.increment_number_served(150)
print(f"Number served end of day: {restaurant.number_served}")

print('-' * 75)

# 9-6 - Ice Cream Stand

class IceCreamStand(Restaurant2):
    """Define an Ice Cream Shop"""

    def __init__(self, name, cuisine_type = 'ice cream'):
        """Define and ice cream shop"""
        super().__init__(name, cuisine_type)
        self.flavors = []
    
    def list_flavors(self):
        """Show available flavors"""
        print(f"We have the following flavors available: ")
        for flavor in self.flavors:
            print(f" - {flavor.title()}")

shop = IceCreamStand("the big scoop")
shop.flavors = ['strawberry', 'pistachio', 'rocky road', 'cheesecake']

shop.describe_restaurant()
shop.list_flavors()

print('-' * 75)

# 9 -10: Imported Restaurant 

from KB_restaurant import Restaurant2

mexican_sugar = Restaurant2('mexican sugar', 'mexican')
mexican_sugar.describe_restaurant()
mexican_sugar.open_restaurant()

print('-' * 75)

# 9-3 Users

class User():
    """Create a user profile"""
    def __init__(self, last_name, first_name, city, email, age):
        """Create the user"""
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.city = city.title()
        self.email = email
        self.age = age
    
    def describe_user(self):
        """create summary of user's profile"""
        print(f"\n{self.first_name} {self.last_name} has the following information \n")
        print(f'Prefered contact: {self.email}')
        print(f'Age: {self.age}')
        print(f'Location: {self.city}')
    
    def greet_user(self):
        """prints greeting to the user"""
        print(f"Hello, {self.first_name}, we are excited you are joining us!")

user1 = User('smith', 'john', 'plymoth', 'mayflower@gmail.com', '35')
user1.describe_user()
user1.greet_user()

print('-' * 75)

# 9-5 Log in Attempts

class User2():
    """Create a user profile"""
    def __init__(self, last_name, first_name, city, email, age):
        """Create the user"""
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.city = city.title()
        self.email = email
        self.age = age
        self.login_attempts = 0
    
    def describe_user(self):
        """create summary of user's profile"""
        print(f"\n{self.first_name} {self.last_name} has the following information \n")
        print(f'Prefered contact: {self.email}')
        print(f'Age: {self.age}')
        print(f'Location: {self.city}')
    
    def greet_user(self):
        """prints greeting to the user"""
        print(f"Hello, {self.first_name}, we are excited you are joining us!")
    
    def increment_login_attempts(self):
        """Increment number of user log in attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """reset attempts to 0"""
        self.login_attempts = 0 

user1 = User2('smith', 'john', 'plymoth', 'mayflower@gmail.com', '35')
user1.describe_user()
user1.greet_user()

print('\nAttempting 4 logins:')
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"Login attempts: {user1.login_attempts}")
print(f'Resetting login attempts to 0')
user1.reset_login_attempts
print(f"showing no login attempts: {user1.login_attempts}")  # not sure why it didnt reset?

print('-' * 75)

# 9-7 Admin

class Admin(User2):
    """Creating a user with Administrative privliges"""
    def __init__(self, last_name, first_name, city, email, age):
        super().__init__(last_name, first_name, city, email, age)
        self.privliges = []
    
    def show_privileges(self):
        """List administrator's privileges"""
        print("User priviliges:")
        for i in self.privliges:
            print(f'\n* {i}')
    
user3 = Admin("Doe", "John", "Dallas", "jDoe@gmail.com", '50')
user3.privliges = ['can ban user', 'can delete posts', "can add posts"]
user3.describe_user()
user3.show_privileges()

print('-' * 75)

# 9-8 Privileges 

class Privileges():
    """Describe privileges of an administrative user"""
    def __init__(self, privliges=[]):
        self.privliges = Privileges()

    def display_privleges(self):
        print(f'\n User Priviliges:')
        if self.privliges:
            for i in self.privliges:
                print(f'* {i}')
            else:
                print(f"The requested user does not have priviliges.")

user3 = Admin("Doe", "John", "Dallas", "jDoe@gmail.com", '50')
user3.privliges = ['can ban user', 'can delete posts', "can add posts"]
user3.describe_user()
user3.show_privileges()






