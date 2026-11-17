print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit.")

while True:

    first_number = input("First number: ")
    if first_number == 'q':
        break
    try:
        first_number = int(first_number)
    except ValueError:
        print("Please enter only numbers.")

    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        second_number = int(second_number)
    except ValueError:
        print("Please enter only numbers.")

    answer = first_number + second_number
    print(answer)

# using json to store files

from pathlib import Path
import json

def get_stored_username(path):
   """Get stored username if available."""
   if path.exists():
      contents = path.read_text()
      username = json.loads(contents)
      return username
   else:
      return None

def get_new_username(path):
   """Prompt for a new username."""
   username = input("What is your name? ")
   contents = json.dumps(username)
   path.write_text(contents)
   return username

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")
        
greet_user()