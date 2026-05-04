def main():
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
 
