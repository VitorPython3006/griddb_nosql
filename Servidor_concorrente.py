# -*- encodeing: utf-8 --
import socket, threading

# simples exemplo de servidor concorrente em python3

def conn(obj, cliente):
  while True:
    print('{} > {}'.format(cliente[0], str(obj.recv(1024).decode())))
    # aqui vai printar o cliente e a respectiva msg
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # criando socket TCP IPV4
s.bind(('127.0.0.1', 80))  # solicitando o endereço especificado + porta
s.listen(3) # aceitando apenas tres conecções respectivas
while True: # criando laço para aceitar conecçõees que estão por vir
  (obj, cliente) = s.accept() # o servidor aceita a conecção e o objeto socket
  obj.send('olá'.encode()) # aqui o servidor envia uma msg
  threading.Thread(target=conn, args=(obj, cliente)).start() # aqui o servidor coloca a conecção atual na thread para rodar em segundo plano
