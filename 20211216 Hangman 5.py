import random

def int_word(sol_set, sol_word):
    list_word = list(sol_word)
    for i in range(len(list_word)):
        if list_word[i] not in sol_set:
            list_word[i] = "-"
    return "".join(list_word)


random.seed()
list_words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(list_words)
set_word = set(word)
solution_set = set()
n = 8

print("H A N G M A N")
for b in range(n):
    print()
    print(int_word(solution_set, word))
    a = input('Input a letter: ')
    if a in set_word:
        solution_set.add(a)
    elif a not in set_word:
        print("That letter doesn't appear in the word")
else:
    print()
    print("Thanks for playing!\nWe'll see how well you did in the next stage")  


