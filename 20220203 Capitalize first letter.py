word = input().lower()
result = []
switch = 0
for index, letter in enumerate(word):
    if index == 0:
        letter = letter.upper()
        result.append(letter)
    elif letter == '_':
        switch = 1
    elif switch == 0:
        result.append(letter)
    elif letter != '_' and switch == 1:
        letter = letter.upper()
        result.append(letter)
        switch = 0

print(''.join(result))
        
sentence = input().split("_")
sentence = [word.capitalize() for word in sentence]
print("".join(sentence))
