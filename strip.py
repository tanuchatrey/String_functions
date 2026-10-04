# Program to use strip() function

name = input("Enter your name: ")

name = name.strip()

print("Your name is:", name)

#left strip
text = "   Hello Python   "

print("Original:", text)
print("After lstrip:", text.lstrip())


#right strip
text = "   Hello Python   "

print("Original:", text)
print("After rstrip:", text.rstrip())
