# # User inputs

# user_choice = input("What kind of rental car would you like? ")
# print(f"Let me see if I can find a {user_choice}.")


# number_of_people = input("How many people are in your dinner group? ")
# number_of_people = int(number_of_people)
# if number_of_people > 8:

#     print("You will have to wait for a table!")
# else:
#     print("Your table is ready")


# runner_number = input("Give me a number and I will tell you whether it is a multiple of 10 or not: ")
# runner_number = int(runner_number)

# if runner_number % 10 == 0:
#     print(f"{runner_number} is a multiple of 10")
# else:
#     print(f"{runner_number} is not a multiple of 10!")

# prompt = "\nWrite the pizza toppings that you want: "
# prompt += "\nType 'quit' to exit. "

# while True :
#     message = input(prompt) 
#     if message != 'quit':
#         print(f"We will add {message} to your pizza.")

#     if message == 'quit': 
#         break

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


    




    
