from concurrent.futures import thread
from operator import add
from socket import *
import threading

host = gethostname() #ele pega o nome da maquina do PC na mesma rede 
port = 8000



print(f'HOST: {host},PORT {port}')

server = socket(AF_INET, SOCK_STREAM) 

server.bind((host, port)) #para fazer a ligação com o host e a porta
def start(): 
    print("Iniciando o Servidor")
    server.listen() #para ouvir todas as conexões que chegar quando o servidor tiver executando
    while True: #para ficar aceitando novas conexões
        con, addr = server.accept() #utilizei para fazer a conexão com o cliente e o servidor, para ele aceitar
        thread = threading.Thread(target=clientes, args=(con, addr))
        thread.start()
        print('Aguardando o cliente se conectar')





def clientes(con, addr): #função para receber o socket cliente, fica recebendo a msg
    print('Conectado em', addr)
    while True:
     msg = con.recv(1024) #vai receer a mensagem 
     print(msg.decode()) #vai imprimir ela e decodificar
  
    



start()

