"""def main():
    age: int = 15
    print(age)

a = 5.6756
b = 0.000000001
c = '7'
d =1.234567
print(type(a))
print(type(b))
print(type(c))

print (f"{a:.2f}")

print(f"{b:e}")
print(f"{round(d, 1)}")

name = "Alice"
name2 = "Bob"
print(f"Hello, {name} and {name2}!")

greeting = "Hello world!"
print(f"length: {len(greeting)}")

print (f"First character: {greeting[0]}")
print (f"First character: {greeting[-1]}")
print(f"first 5: {greeting[0:5]}")

print(f"first 5: {greeting[4:]}")
if __name__ == "__main__":
    main()


text = 'hello,world'
print(text.upper())
print(text.lower())
print(text.strip())
print(text.title())
print(text.split(','))
print(text.split('o'))
var = 'ram'
greet = "hi"
print(f"hello{var}{greet}")

is_raining = True
print(f"Is it raining? {is_raining}")

is_adult = True
can_travel = False
go_out = is_adult and can_travel

print(go_out)

var = '1.5'

print(float(var))       
print(str(var))         
print(bool(var))         

num = int(float(var))
print(num)  

if 5==5:
    print("Equal")
print("Not equal")
if True:
    print("inside")
print("outside")

weather = "hot"
temp = 25   

if temp > 20:
    print(weather)
else:
    print("cold")



num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    print("Result:", num1 + num2)

elif choice == '2':
    print("Result:", num1 - num2)

elif choice == '3':
    print("Result:", num1 * num2)

elif choice == '4':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid choice")


import random

# generate random number
secret_number = random.randint(1, 10)

print("Guess a number between 1 and 10")

guess = int(input("Enter your guess: "))

if guess == secret_number:
    print("🎉 Correct! You guessed it right.")
elif guess > secret_number:
    print("Too high!")
else:
    print("Too low!")

print("The correct number was:", secret_number)
 
range(10)
print(list(range(10)))

range(5, 15)
for i in range(5, 15):
    print(i)
print(list(range(5, 15)) )

range(0, 20, 2)
print(list(range(0, 20, 2)) )

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits , start=1):
    print(f"Index: {index}, Fruit: {fruit}")
    
counter = 5
while counter > 0:
    print(f"Counter: {counter}")
    counter -= 1 
    if counter == 3:
        break
    print(f"Counter: {counter}")
    counter -= 1

cities = ["New York", "London", "Paris", "Tokyo"]
capitals = ["Washington D.C.", "London", "Paris",]
for city,capital in zip(cities, capitals):
    print(f"{city} has capital {capital}")

squares = [x**2 for x in range(10)]
print(squares)  

fruits = ["apple", "banana", "cherry"]
last = fruits[1:2]        # start:end:step
print(last)
list.append(fruits, "orange")
print(fruits)
list = [1, 2, 3, 4, 5]
list.insert(2, 10)  # Insert 10 at index 2
print(list)
list.remove(3)  # Remove the first occurrence of 3
print(list)
  # Remove and return the element at index 1
list.pop(1)
print(list)
num =[5, 2, 9, 1, 5]
num.sort()  # Sort the list in ascending order
num.reverse()  # Reverse the list
num.sort(reverse=True)  # Sort the list in descending order
num.count(3)  # Count the occurrences of 3
print(num)
print(num.count(5))

# Input string
text = input("Enter a string: ")

# Uppercase
print("Uppercase:", text.upper())

# Lowercase
print("Lowercase:", text.lower())

# Title Case
print("Title Case:", text.title())

# Word Count
words = len(text.split())
print("Word Count:", words)

# Replace
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")
print("After Replace:", text.replace(old_word, new_word))

# Length
print("Length of String:", len(text))

# Switch Case
print("Switch Case:", text.swapcase())


rows = 4

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("* " * (2*i - 1))

rows = 4

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()



import random

minimum = int(input("Enter minimum: "))
maximum = int(input("Enter maximum: "))

num = random.randint(minimum, maximum)

print("Random Number:", num)"""


"""
a1 = (2)
a2 = (3,)
print(type(a1))
print(type(a2))

# 📘 Dictionary Example: Phone Book

phone_book = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555"
}

# 🔹 Accessing a value using key
print("Alice's Number:", phone_book["Alice"])

# 🔹 Adding new items
phone_book["David"] = "111-222-3333"
phone_book["Eva"] = "444-555-6666"

# 🔹 Printing updated dictionary
print("\nUpdated Phone Book:")
print(phone_book)

# 🔹 Using get() method
retrieve = phone_book.get("Alice")

# 🔹 Using get() with default value
result = phone_book.get("Eve", "Not found")

print("\nRetrieved Value:")
print(retrieve)

print("\nChecking Missing Key:")
print(result)

# 🔹 Updating a value
phone_book["Bob"] = "000-000-0000"

print("\nAfter Updating Bob's Number:")
print(phone_book)

# 🔹 Removing an item
phone_book.pop("Charlie")

print("\nAfter Removing Charlie:")
print(phone_book)

# 🔹 Printing all keys
print("\nAll Names:")
print(phone_book.keys())

# 🔹 Printing all values
print("\nAll Phone Numbers:")
print(phone_book.values())

# 🔹 Looping through dictionary
print("\nPhone Book Details:")
for name, number in phone_book.items():
    print(name, ":", number)

# 🔹 Checking if key exists
if "Alice" in phone_book:
    print("\nAlice exists in the phone book.")

# 🔹 Length of dictionary
print("\nTotal Contacts:", len(phone_book))
"""


# Function with default argument
def greet(name, greeting="hello "):
    return f"{greeting}{name}"


result = greet("Alice")
print(result)


# Function using *args
def sum_values(*args):
    print(f"The values are {args}")
    print(f"This type is {type(args)}")


sum_values(1, 2)
sum_values(1, 2, 3, 4)


# Function using **kwargs
def employee(**details):
    print(details)
    print(type(details))


employee(name="ram", phone="0000", type="full time")

def everything(required, *args, default="default", **kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

everything("required value", 1, 2, 3, default="custom default", name="value1", age="2")