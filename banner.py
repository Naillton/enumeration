import socket
host = input('Digite o ip do alvo: ')
port = int(input('Digite a porta do dominio: '))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host,port))
print (sock.recv(2048))
sock.close()
