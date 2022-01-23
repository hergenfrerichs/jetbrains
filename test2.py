import string

#input_word = 'Hergen'

def all_numbers(pw):
    check = [k for k in pw if k in string.digits]
    if len(check) == len(pw):
        # print(pw)
        return True


def hack(password):
    count_comb = 2 ** len(password)

    if all_numbers(password) == True:
        yield password
    else:
        for a in range(count_comb):
            word = list(password.lower())
            binary = str(format(a, 'b'))
            if len(binary) < len(word):
                for i in range(1, len(word)):
                    if len(binary) == i:
                        add = (len(word) - i) * '0'
                        binary = f'{add}{binary}'
            for index, letter in enumerate(word):
                if letter in string.ascii_lowercase:
                    if binary[index] == '0':
                        word[index] = letter.lower()
                    if binary[index] == '1':
                        word[index] = letter.upper()
            yield ''.join(word)
        

password_file = open('passwords.txt', 'r')

for i in range(1000):
    line = password_file.readline().strip()
    hack_generator = hack(line)

    for i in range(1000000):
        try:
            attempt = next(hack_generator)
            #print(attempt)
            if attempt == 'superMan':
                print(f'Connection success!')
                break
        except:
            break
else:
        print('Too many attempts!')

password_file.close()
   
        
