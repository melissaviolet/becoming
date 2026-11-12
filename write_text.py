from pathlib import Path

path = Path("guest.txt")

prompt = "\nPlease enter your name: "
prompt += "\nEnter 'q' to quit "

guest_names = []

while True:
    name = input(prompt)

    if name.lower() == 'q':
        break

    print(f"\nThanks {name}, we'll add your name to the guest list")
    guest_names.append(name)

file_string = ''
for name in guest_names:
    file_string += f"{name}\n"

path.write_text(file_string)




