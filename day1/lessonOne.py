# Variables + Input/Output
name = input("What's your name? ")
age = int(input("How old are you? "))
future_age = age + 5
print(f"Hello {name}, in 5 years you will be {future_age} years old.")

user = input("What is your name?: ")
favorite_language = input("What is your favorite programming language?: ")
print(f"Nice to meet you {user}, I see you like {favorite_language}!")

# Conditionals
age = int(input("Enter your age: "))
if age < 0:
    input("Invalid age. Please enter a valid age: ")
elif age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Loops
for i in range(21):
    if i % 3 == 0 and i %5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Functions
num = int(input("Enter a number: "))
def is_even(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
is_even(num)

# Band Name Generator
print("Welcome to the Band Name Generator.")
city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + city + " " + pet)

