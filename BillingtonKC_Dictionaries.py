# Chapter 7: While Loops Lab
# Name: Kristina Billington
# Date: 23 SEP 2022

# Stage 1 & 2- Gather Student information and Build Dictionary 

students = {}
quiz_running = True
while quiz_running:
    name = input("What is the student's last name? ")
    if students.get(name.lower()):
        print("Student last name already in use. Please add first initial.")
        continue
    student = input("What is the student's GPA: ")
    students[name]=float(student)
    repeat = input('Would you like to add another student? Yes or No? ')
    repeat = repeat.upper()
    if repeat =='NO':
        quiz_running = False



# Stage 3:

print(f'\nI have', (len(students)), 'students in my class.\n') 
print("List of Students:")
for key, value in sorted(students.items()): 
    print(key.title())

# Stage 4:

print('\nGPA Average:')
average = sum(students.values()) / len(students)                             
average2 = round(average,2)
print(average2)