# Replace a word with another word using in-built function

string = "I like Java"
old_word = "Java"
new_word = "Python"

result = string.replace(old_word, new_word)

print(result)

# Replace a word with another word without using in-built function

string = "I like Java"
old_word = "Java"
new_word = "Python"

result = ""
i = 0

while i < len(string):
    if string[i:i+len(old_word)] == old_word:
        result = result + new_word
        i = i + len(old_word)
    else:
        result = result + string[i]
        i = i + 1

print(result)
