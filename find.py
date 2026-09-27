# find a word in string using built-in function

string = "I am learning Python"

word = "Python"

position = string.find(word)

if position != -1:
    print("Word found at position:", position)
else:
    print("Word not found")

# find a word in string without using built-in function

string = "I am learning Python"
word = "Python"

position = -1
i = 0

while i <= len(string) - len(word):
    if string[i:i+len(word)] == word:
        position = i
        break
    i = i + 1

if position != -1:
    print("Word found at position:", position)
else:
    print("Word not found")
