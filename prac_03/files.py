"""
CP1404/CP5632 Practical 03 - Files
Exercises to practice different file-reading techniques.
"""

name = input("Enter your name: ")

out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

#---------------------------------------

in_file = open("name.txt", "r")
name_from_file = in_file.read().strip()
in_file.close()

print(f"Hi {name_from_file}!")

#---------------------------------------

with open("numbers.txt", "r") as in_file:
    lines = in_file.readlines()

result = (int(lines[0]) + int(lines[1]))
print(result)


#---------------------------------------

total = 0

with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line)

print(total)