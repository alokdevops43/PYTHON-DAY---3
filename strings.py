# 05_strings.py

# Creating strings

name = "Sahil"

print(name)


# String length

print(len(name))


# String indexing

print(name[0])
print(name[1])
print(name[2])


# String slicing

print(name[0:3])
print(name[1:5])


# Negative indexing

print(name[-1])
print(name[-2])


# String methods

text = "python programming"

print(text.upper())

print(text.capitalize())

print(text.title())

print(text.replace("python", "Python"))

print(text.find("programming"))


# Checking methods

message = "hello123"

print(message.isalpha())

print(message.isalnum())


# Concatenation

first_name = "Sahil"

last_name = "Choudhary"

full_name = first_name + " " + last_name

print(full_name)


# Repeating strings

print("Python " * 3)


# Escape sequences

print("Hello\nWorld")

print("Python\tProgramming")


# f-string

age = 21

print(f"My name is {name} and I am {age} years old.")