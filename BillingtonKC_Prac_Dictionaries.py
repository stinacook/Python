# Chapter 6. Dictionaries 
# Name: Kristina Billigton
# Date: 14 SEP 2022

# 6-1 Person

from re import I


known_person_info = {
    'first_name':'bob', 
    "last_name":'jones', 
    'age':'32', 
    'current_city':'gainesville, FL'
    }
print('*' * 75)

# Print each piece of information stored in dictionary:

for key, value in known_person_info.items():
    print(f"{key.title()}: {value.title()}")
  
print('*' * 75)

# 6-3 Glossary

python_glossary = {
    'method': 'a function that belongs to an object',
    'variable': 'a container for storing data values',
    'string': 'a collection of alphabets, words or other characters',
    'for_loop': 'used for iterating over a sequence',
    'tuple': 'an immutable list'
    }

for key, value in python_glossary.items():
    print(f"{key.title()}:\n- {value.capitalize()}.\n")

print('*' * 75)

# 6-5 Rivers

major_rivers = {
    'egypt': 'nile', 
    'brazil': 'amazon',
    'russia': 'lena',
    }

for key, value in major_rivers.items():
    print(f"The {value.title()} river runs through {key.capitalize()}.\n")

print('*' * 75)

for key, value in major_rivers.items():
    print(f"{value.title()}")

print('*' * 75)

for key, value in major_rivers.items():
    print(f"{key.title()}")

print('*' * 75)

# 6-8 Pets 

pets = [] 

fido = { 
    'name': 'fido',
    'type_of_animal': 'dog',
    'owner_name': 'bob'
    }
pets.append(fido)

kitty = {
    'name': 'kitty',
    'type_of_animal': 'cat',
    'owner_name': 'jane'
    }

pets.append(kitty)

rex = {
    'name': 'rex',
    'type_of_animal': 'lizard',
    'owner_name': 'gene'
    }
pets.append(rex)

spirit = {
    'name': 'spirit',
    'type_of_animal': 'horse',
    'owner_name': 'helen'
    } 
pets.append(spirit)


for pet in pets:
    for key, value in pet.items():
        print(f"  {key}\n    {value}")
    if pet == pets[-1]:
        print('end of list')
    else:
        i = pets.index(pet)
        remaining = len(pets[i:]) - 1
        print(remaining)


print('*' * 75) 

# 6-11 Cities

cities = {
    'stockholm':{
        'country': 'sweden',
        'population': '1 million',
        'fact': 'made up of 14 islands',
    },
    'london':{
        'country': 'england',
        'population': '9 million',
        'fact': 'river thames runs through it',
    },
    'oslo':{
        'country': 'norway',
        'population': '1/2 million',
        'fact': 'oslo has the more electric cars than any other city',
    },
}
for key, value in cities.items():
    print(key.title())
    for k, v in value.items():
         print(f" \t{k.title()}: {v.capitalize()}.")

print('*' * 75)    
