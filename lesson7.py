# User inputs

user_choice = input("What kind of rental car would you like? ")
print(f"Let me see if I can find a {user_choice}.")


number_of_people = input("How many people are in your dinner group? ")
number_of_people = int(number_of_people)
if number_of_people > 8:

    print("You will have to wait for a table!")
else:
    print("Your table is ready")


runner_number = input("Give me a number and I will tell you whether it is a multiple of 10 or not: ")
runner_number = int(runner_number)

if runner_number % 10 == 0:
    print(f"{runner_number} is a multiple of 10")
else:
    print(f"{runner_number} is not a multiple of 10!")