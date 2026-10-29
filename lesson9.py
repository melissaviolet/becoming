class Restaurant:
    def __init__ (self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant is called {self.restaurant_name} and it does {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

my_restaurant = Restaurant("Quince", "Italian")
restaurant2 = Restaurant("Patio", "Chinise")
print(f"The restaurant is called {my_restaurant.restaurant_name}")
print(f"The restaurant cuisine is {my_restaurant.cuisine_type}")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
print(f"The restaurant is called {restaurant2.restaurant_name}")
print(f"The restaurant cuisine is {restaurant2.cuisine_type}")
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

class User:
    def __init__(self, first_name, last_name, age, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobby = hobby

    def describe_user(self):
        print(f"The user is {self.first_name.title()} {self.last_name.title()}.")
        print(f"The user is {self.age} years old and loves {self.hobby}.")

    def greet_user(self):
        print(f"Hello {self.first_name}!")

user1 = User("mark", "mulinya", 13, "football")
user2 = User("ian", "kirunda", 24, "football")
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()

        