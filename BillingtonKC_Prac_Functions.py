# Chapter 8: Functions
# Name: Kristina Billington
# Date: 27 SEP 2022

# 8-2 Favorite Books

def favorite_book(book_title):
    """accepts parameter, title of book"""
    print(f'\nOne of my favorite books is {book_title.title()}.\n')
    
favorite_book("seabiscuit")

# 8-5 Cities

def describe_city(city_name, country_name = 'sweden'):
    """accepts name of city and corresponding country""" 
    print(f'{city_name.title()} is in {country_name.title()}.')

describe_city(city_name= 'stockholm')
describe_city(city_name= 'eskilstuna')
describe_city(city_name= 'malmo')

print() 

# 8-7 Album

def make_album(artist_name, album_title, song_count=''):
    """return an album name"""
    if song_count :
        a = {
        "artist_name": artist_name, 
        "album_title":album_title,
        "song_count": song_count    
        }
        return a
    else:
        b = {
        "artist_name": artist_name,
        "album_title": album_title
        }
        return b 

album_2 = make_album('tom petty', 'damn the torpedoes', '6')
print(album_2)
album_3 = make_album('tom petty', 'full mooon fever')
print(album_3)
album_4 = make_album('tom petty', 'wildflowers')
print(album_4)

print() 

# 8-9 Messages

def show_messages(texts):
    """Print text messages"""
    for text in texts:
        msg = text
        print(msg)

messages = ['Hello, will you be home for dinner?', 'Hey, can you please pick up some dog food?', 'LOL!!!', "busy will call back"]
show_messages(messages)

print() 

# 8-12  Sandwiches

def make_sandwich(*toppings):
    '''Summarize the sandwich that is getting made'''
    print('\nMaking a sandwich with the following toppings:')
    for topping in toppings:
        print(f"- {topping}") 

make_sandwich('onion','pickle')
make_sandwich('lettuce', 'tomato', 'onion', 'salt and pepper')
make_sandwich('vinegar', 'oil', 'lettuce', 'oregano', 'bacon')

print()

# 8-14 Cars

def build_cars(manufacturer, model, **user_info):
    '''Build a dictionary containing everything we know about a vechicle'''
    user_info['manufacturer_name'] = manufacturer
    user_info['model_name'] = model 
    return user_info

user_profile = build_cars('subaru', 'WRX',
                        color = 'blue', 
                        trim = 'STI')
print(user_profile)