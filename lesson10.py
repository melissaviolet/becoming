from pathlib import Path

# Set the path to the file
path = Path('python_lessons.txt')

print("--- Reading the entire file:")
contents = path.read_text()
contents = contents.replace('Python', 'C')
print(contents)

print("\n--- Storing the lines in a list and looping:")

for line in contents.splitlines():
    line.replace('Python', 'C')
    print(line)
