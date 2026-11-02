class Restaurant:
    def __init__ (self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describes details about the restauarant"""
        print(f"The restaurant is called {self.restaurant_name} and it does {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Simple message that restauarnt is open"""
        print(f"{self.restaurant_name} is open!")

    def read_number_served(self):
        """Reads and shows number of people served so far"""
        print(f"{self.number_served} people served so far!")

    def set_number_served(self, n_of_people):
        """Sets number of people served"""
        if n_of_people >= self.number_served:
            self.number_served = n_of_people
        else:
            print("You can't roll back the number of people served!")

    def increment_number_served(self, n_of_people):
        """Increments number of people served"""
        self.number_served += n_of_people

# first restaurant instance
my_restaurant = Restaurant("Quince", "Italian")
my_restaurant.set_number_served(23)
my_restaurant.increment_number_served(54)
my_restaurant.read_number_served()

print(f"The restaurant is called {my_restaurant.restaurant_name}")
print(f"The restaurant cuisine is {my_restaurant.cuisine_type}")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()


# second restaurant instance
restaurant2 = Restaurant("Patio", "Chinise")
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
        self.login_attempts = 0


    def describe_user(self):
        print(f"The user is {self.first_name.title()} {self.last_name.title()}.")
        print(f"The user is {self.age} years old and loves {self.hobby}.")

    def greet_user(self):
        print(f"Hello {self.first_name.title()}!")

    def increment_login_attempts(self, login_times):
        """ Increment login attempts by 1"""
        pass

    
    def reset_login_attempts(self):
        """Reset login attempts to 0"""
        self.login_attempts = 0 

# user instance 1
user1 = User("mark", "mulinya", 13, "football")
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts(2)

# user instance 2
user2 = User("ian", "kirunda", 24, "football")
user2.describe_user()
user2.greet_user()

        