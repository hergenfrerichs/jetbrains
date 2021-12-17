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
while n > 0:
    print()
    result = int_word(solution_set, word)
    print(result)
    if result.find("-") == -1:
        print("You guessed the word!\nYou survived!")
        break
    a = input('Input a letter: ')
    if a in set_word and a not in solution_set:
        solution_set.add(a)
    elif a in set_word and a in solution_set:
        print("No improvements")
        n-=1
    elif a not in set_word:
        print("That letter doesn't appear in the word")
        n -= 1
else:
    print("You lost!")  
