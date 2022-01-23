import socket

# working with a socket as a context manager
with socket.socket() as client_socket:
    hostname = '127.0.0.1'
    port = 9090
    address = (hostname, port)

    client_socket.connect(address)

    data = 'Wake up, Neo'
    data = data.encode()

    client_socket.send(data)

    response = client_socket.recv(1024)

    response = response.decode()
    print(response)
