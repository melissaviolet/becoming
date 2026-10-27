# Functions

def display_message():
    print("I am learning functions, arguments and parameters in this chapter.")

display_message()

# Favourite book
def favourite_book(title):
    print(f"One of my favourite books is {title.title()}.")

favourite_book("What Light")
favourite_book("Gods and Warriors")

# T-shirt size and text
def make_tshirt(text="I love Python", size="large"):
    print(f"\nThe T-shirt size is {size} and it is going to have '{text}' on it.")

make_tshirt("Jer 29:11")
make_tshirt(size= "small",text="worthy")
make_tshirt()

# Describe city
def describe_city(name,country="U.S.A"):
    print(f"\n{name.title()} is in {country.title()}.")

describe_city("kampala","uganda")
describe_city("los Angelos")
describe_city("miami")

# country city
def city_country(city, country):
    about_city = f"{city}, {country}"
    return about_city.title()

city = city_country("algiers", "algeria")
print(city)

# albums and artists
def make_album(artist_name, title):

 album_info = f"{artist_name} {title}"
 return album_info.title()

while True:
    print("\nPlease tell me the artist name and album title")
    print("(enter 'q' at any time to quit)")

    name = input("Artist name: ")

    if name == 'q':
        break
    title = input("Album title: ")

    if title == 'q':
    
        break

    make_album(name, title)
    print(f"The album {title.title()} is by {name.title()}")

# Passing lists in functions

short_messages = ["hello", "good morning", "well well", "good work"]
sent_messages = []

def send_messages(short_messages):
    for message in short_messages:
        
        print(message.title())
        sent_messages.append(message)
    print(sent_messages)

send_messages(short_messages[:])

# Passing arbitary number of arguments

def sandwich_toppings(*toppings):
    print("I want a sandwish with;")
    for topping in toppings:
        print(f"- {topping}")

sandwich_toppings("banana")
sandwich_toppings("macaroni", "eggs")
sandwich_toppings("eggs","cheese","beef")

def build_profile(first, last, **user_info):
   user_info['first_name'] = first
   user_info['last_name'] = last
   return user_info

user_profile = build_profile(first="Melissa", last="Violet", hobbies="music", aspirations="paino", language="swahili", fears="loneliness", zing="companianship")
print(user_profile)

def make_car(manufacturer, model_name, **car_info):
    car_info["manufacturer"] = manufacturer
    car_info["model_name"] = model_name
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)









