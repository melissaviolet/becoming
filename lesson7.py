# User inputs

user_choice = input("What kind of rental car would you like? ")
print(f"Let me see if I can find a {user_choice}.")

# Table reservation
number_of_people = input("How many people are in your dinner group? ")
number_of_people = int(number_of_people)
if number_of_people > 8:

    print("You will have to wait for a table!")
else:
    print("Your table is ready")

# Multiples of 10 
runner_number = input("Give me a number and I will tell you whether it is a multiple of 10 or not: ")
runner_number = int(runner_number)

if runner_number % 10 == 0:
    print(f"{runner_number} is a multiple of 10")
else:
    print(f"{runner_number} is not a multiple of 10!")

# While loops

# Pizza toppings question
prompt = "\nWrite the pizza toppings that you want: "
prompt += "\nType 'quit' to exit. "

while True :
    message = input(prompt) 
    if message != 'quit':
        print(f"We will add {message} to your pizza.")

    if message == 'quit': 
        break

#  Movie ticket prices based on age
qtn = "\nWhat is your age? "

message = 0
active = True

while active:
    message = input(qtn)
    message = int(message)
    if message <= 3:
        print(f"Your ticket is free!")
    elif message in range(4,13):
        print(f"Your ticket is 10$!")
    elif message >= 12:
        print(f"Your ticket is 15$!")
    break

# Using a while Loop with Lists and Dictionaries

sandwich_orders = ["egg", "banana", "pastrami","tuna","pastrami", "sausage","submarine", "pastrami"]
finished_sandwiches = []

print("The Deli has run out of pastrami sandwiches😕")

while sandwich_orders:
    while "pastrami" in sandwich_orders:
          sandwich_orders.remove("pastrami")

    sandwich = sandwich_orders.pop()

    print(f"I made you a {sandwich} sandwich!")

    finished_sandwiches.append(sandwich)

print(f"\nThese are the sandwiches I have finished;")
for sandwich in finished_sandwiches:
        print(sandwich.title())

# Dream vacation
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If I could visit one place in the world I would go to ")

    responses[name] = response

    repeat = input("Would you like another person to take the poll? Respond (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n-------------Polling Results--------------")
for name, response in responses.items():
    print(f"{name.title()} would really love to visit {response.title()}")

    




    
