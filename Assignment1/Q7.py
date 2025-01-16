#Question 7:

#7.1
with open("example.txt", "w") as file:
    file.write("This is the first line.\nThis is the second line.")

with open("example.txt", "r") as file:
    content = file.read()

print("Content of the file:")
print(content)


#7.2
with open("example.txt", "a") as file:
    file.write("\nThis is an appended line.")

with open("example.txt", "r") as file:
    updated_content = file.read()

print("Updated content of the file:")
print(updated_content)


#7.3
with open("example.txt", "r") as file:
    lines = file.readlines()
    line_count = len(lines)

print(f"The number of lines in the file is: {line_count}")