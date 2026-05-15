"""
with open("file.txt", "w") as f:
    f.write("Hello World\n")
    f.write("This is Python file handling\n")

with open("file.txt", "a") as f:
    f.write("New line added\n")

with open("file.txt", "r") as f:
    content = f.read()
    print(content)

with open("file.txt", "r") as f:
    print(f.readline())
    print(f.readline())

with open("file.txt", "r") as f:
    lines = f.readlines()
    print(lines)

with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())"""
"""
import csv

student = [
    ["Name", "Age"],
    ["Raj", "21"],
    ["Shyam", "22"]
]

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(student)

with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"])

with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Age"])

with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old.")

with open("students.csv", "r+") as f:
    reader = csv.DictReader(f)
    students = list(reader)
    students.append({"Name": "Sita", "Age": "20"})
    f.seek(0)
    writer = csv.DictWriter(f, fieldnames=["Name", "Age"])
    writer.writeheader()
    writer.writerows(students) """
    
class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"
    def display_name(self):
        print( f"{self.name} is {self.age} years old.")
rex = dog("Rex", 5)
rex.display_name()
