import random
random.seed()
list_words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(list_words)
hint = list(word)
for i in range(3, len(hint)):
    hint[i] = "-"
hint = "".join(hint)
print("H A N G M A N")
a = input(f'Guess the word {hint}: ')
if a == word:
    print("You survived!")
else:
    print("You lost!")
