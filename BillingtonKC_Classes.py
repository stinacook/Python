# Chapter 9: Classes Lab Assignment
# Name: Kristina Billington
# Date: 12 OCT 2022

import datetime

# Creating parent class of "Employee" and 2 Child Classes- Salary and Hourly:

class Employee:
    """A simple representation of an employee"""
    def __init__(self, ID, last_name, first_name):
        """Initializes demograhic attributes"""
        self.ID = int(ID)
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.date_of_birth = None
    
    def full_name(self):
        """Describe full name from given first and last names"""
        self.full_name = (f"{self.first_name} { self.last_name}")
        return self.full_name

    def date_intialized(self):
        """Generate a value for the date record created"""
        self.date_intialized = datetime.datetime.now()
        return self.date_intialized

    def set_date_of_birth(self, year, month, day):
        format = '%Y%m%d'
        self.date_of_birth = datetime.datetime.strptime(f"{year}{month}{day}", format)
    
    def get_date_of_birth(self):
        output_format = '%B %d, %Y'
        return self.date_of_birth.strftime(output_format)


class Hourly_Employee(Employee):
    """Initialize an hourly employee profile"""
    def __init__(self, ID, last_name, first_name, hours_worked, hour_rate):
        super().__init__(ID, last_name, first_name)
        self.hours_worked = float(hours_worked)
        self.hour_rate = float(hour_rate)

    def calculate_payroll(self):
        """Calculate payroll for an hourly employee"""
        return self.hours_worked * self.hour_rate
    
    def get_pay(self):
        return self.calculate_payroll()


class Salary_Employee(Employee):
    """Initialize a salary employee profile"""
    def __init__(self, ID, last_name, first_name, weekly_salary):
        super().__init__(ID, last_name, first_name)
        self.weekly_salary = float(weekly_salary)

    def calculate_salary(self):
        """Calculate payroll for a salary employee given weekly amount"""
        return self.weekly_salary

    def get_pay(self):
        return self.calculate_salary()



# Print header
print('-' * 75)       

employee1 = Salary_Employee('1', 'smith', 'john', '1200')
employee1.set_date_of_birth(year='1980', month='01', day='06')

employee2 = Salary_Employee('2', 'brenna', 'valerie','4200')
employee2.set_date_of_birth(year='1980', month='01', day='06')

employee3 = Hourly_Employee('3', 'poppins', 'mary', '40', '27.50')
employee3.set_date_of_birth(year='1983', month='02', day='23')

employee4 = Hourly_Employee('4', 'bacon', 'kevin','45', '25.75' )
employee4.set_date_of_birth(year='1958', month='07', day='08')

# Print payroll report for listed employees:

for employee in [employee1, employee2, employee3, employee4]:
    print(f"Payroll for: {employee.ID} - {employee.full_name()} - Born: {employee.get_date_of_birth()}")
    print(f"\t- Check amount: ${employee.get_pay()}")

print('-' * 75) 