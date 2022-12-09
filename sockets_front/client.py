import socket

host = '127.0.0.1'
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

print("Conectado al servidor")
while True:

    # algo = 'hola'
    # s.send(algo.encode("ascii"))
    recv = str(s.recv(1024).decode("ascii"))
    print(recv)

    # command = input('> ')
    # if len(command) == 0 or command == "bye":
    #     print("Saliendo...")
    #     s.send(command.encode("ascii"))
    #     break
    # else:
    #     s.send(command.encode("ascii"))
    #     recv = str(s.recv(1024).decode("ascii"))
    #     print(recv)