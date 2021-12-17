import random

def int_word(sol_set, sol_word):
    list_word = list(sol_word)
    for i in range(len(list_word)):
        if list_word[i] not in sol_set:
            list_word[i] = "-"
    return "".join(list_word)


def checks(i):
    result = True
    if len(i) != 1:
        print("You should input a single letter")
        result = False
    elif i.isalpha() == False or i.islower() == False:
        print("Please enter a lowercase English letter")
        result = False        

    return result


random.seed()
#list_words = ['python', 'java', 'kotlin', 'javascript']
list_words = ['javascript']
word = random.choice(list_words)
set_word = set(word)
solution_set = set()
guessed_set = set()

print("H A N G M A N")
check_play = True
while check_play == True:
    play = input('Type "play" to play the game, "exit" to quit: ')
    if play != "play" and play != "exit":
        continue
    elif play == "exit":
        break
    else:
        check_play = False
    n = 8
    while n > 0:
        print()
        result = int_word(solution_set, word)
        print(result)
        if result.find("-") == -1:
            print(f"You guessed the word {word}!\nYou survived!")
            check_play = True
            solution_set.clear()
            guessed_set.clear()
            print()
            break
        if result.find("-") != -1:
            a = input('Input a letter: ')
            if checks(a) == True:
                if a in guessed_set:
                    print("You've already guessed this letter")
                elif a in set_word :
                    solution_set.add(a)
                    guessed_set.add(a)
                elif a not in set_word:
                    guessed_set.add(a)
                    print("That letter doesn't appear in the word")
                    n -= 1
    else:
        print("You lost!")
        print()
        check_play = True
        solution_set.clear()
        guessed_set.clear()
