# Find length of a string using built-in function

string = input("Enter a string: ")

length = len(string)

print("Length of string is:", length)

# Find length of a string without using built-in function

s = input("Enter a string: ")

count = 0

for ch in s:
    count = count + 1

print("Length of string is:", count)
