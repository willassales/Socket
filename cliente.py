from socket import *

host = gethostname() 
port = 8000

cli = socket(AF_INET, SOCK_STREAM) #defini em IPV4 e coloquei em TCP
cli.connect((host, port)) #fiz a conexão com o servidor


name = input("Digite seu Nome: ") 

while True:
      
    msg = input(f"{name}: ") #coloquei para a msg receber o imput e chamar o nome de usuário digitado anteriormente

    msg =  name +': '+ msg #msg vai recever o nome e a msg
    
    cli.send(msg.encode()) #o cliente vai enviar a mensagem codificada

