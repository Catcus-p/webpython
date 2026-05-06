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

print("The correct number was:", secret_number)"""
 
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
    """print(f"Counter: {counter}")
    counter -= 1 """
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