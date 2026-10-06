# Functions

def display_message():
    print("I am learning functions, arguments and parameters in this chapter.")

display_message()

def favourite_book(title):
    print(f"One of my favourite books is {title.title()}.")

favourite_book("What Light")
favourite_book("Gods and Warriors")

def make_tshirt(text="I love Python", size="large"):
    print(f"\nThe T-shirt size is {size} and it is going to have '{text}' on it.")

make_tshirt("Jer 29:11")
make_tshirt(size= "small",text="worthy")
make_tshirt()

def describe_city(name,country="U.S.A"):
    print(f"\n{name.title()} is in {country.title()}.")

describe_city("kampala","uganda")
describe_city("los Angelos")
describe_city("miami")


