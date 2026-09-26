# reversing a string with built-in function

s = input("Enter a string: ")

reverse = s[::-1]

print("Reversed string:", reverse)

# reversing a string without built-in function

s = input("Enter a string: ")

reverse = ""

for ch in s:
    reverse = ch + reverse

print("Reversed string:", reverse)
