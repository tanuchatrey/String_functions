# count the occurence of a word in a string using built-in function 

string = "I like Python. Python is easy. I love Python."

word = "Python"

count = string.count(word)

print("Word occurs", count, "times")

# count the occurence of a word in a string without using built-in function

string = "I like Python. Python is easy. I love Python."

word = "Python"

count = 0
i = 0

while i <= len(string) - len(word):
    if string[i:i+len(word)] == word:
        count = count + 1
        i = i + len(word)
    else:
        i = i + 1

print("Word occurs", count, "times")
