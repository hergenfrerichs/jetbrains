import argparse
import socket

parser = argparse.ArgumentParser()
parser.add_argument("host")
parser.add_argument("port")
parser.add_argument("message")

args = parser.parse_args()

arguments = [args.host, args.port, args.message]
print(arguments)

client = socket.socket()
address = (host, int(port))
client.connect(address)
message = args.message.encode()
client.send(message)
response = client.recv(1024)
response = response.decode()
print(response)
client.close()



