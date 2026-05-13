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
        print(line.strip())