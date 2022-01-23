import string

password = "aDgT9tq1PU0"

def hack_by_letter():
    list_symbols = string.ascii_letters + string.digits
    for i in list_symbols:
        yield i


guessed_password = []
str_guessed_password = ""
range_symbols = 62
range_pw_length = 50

for k in range(range_pw_length):
    hack_generator_2 = hack_by_letter()
    for j in range(range_symbols):
        attempt_pw = next(hack_generator_2)
        attempt_long = str_guessed_password + attempt_pw
        if attempt_long == password[:k + 1]:
            guessed_password.append(attempt_pw)
            str_guessed_password = ''.join(guessed_password)
            break
print(str_guessed_password) 


