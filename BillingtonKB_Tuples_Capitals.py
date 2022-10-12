# File Name: Tuples_Capitals
# Name: Kristina Billington
# Date: 19 SEP 2022


print('*' * 75)

# print report header - State Capital Listing

print('State Capitals Listing \n')

# create dictionary of key-value pairs of state and capital (lowercase):

state_capitals = {
    'texas': 'austin', 
    'florida' : 'tallahassee',
    'colorado' : 'denver',
    'georgia' : 'atlanta',
    }

# use for in Loop to show state and capital detail line (title case):

for key, value in state_capitals.items():
    print(f"The capital of {key.title()} is {value.title()}.")

# show number of states using len() function:

print(f"\nNumber of states in this report:", len(state_capitals),"\n")

# delete one state(georgia) and show number of states again:

#print('Deleting', {state_capitals[-1]},".")
state_capitals.pop
print(f"\nNumber of states in this report:", len(state_capitals),"\n")


# add one state (Wyoming) to the dictionary:

print('\nAdding Wyoming and relisting\n')

dict1 = {'wyoming' : 'cheyenne'}
state_capitals.update(dict1)

# relist dictionary using for loop:

for key, value in state_capitals.items():
    print(f"The capital of {key.title()} is {value.title()}.")

# show number of states again:
print(f"\nNumber of states in this report:", len(state_capitals),"\n")
