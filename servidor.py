# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 16:26:49 2018

@author: User
"""

import socket
from datetime import *
 
host = '127.0.0.1'  # o mesmo que localhost
porta = 8800         # porta da conexão
alfabeto = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

chave = 3
# linha abaixo converte as letras para minúsculas
# mensagem = mensagem.lower()

# tamanho da lista alfabeto
# n = len(alfabeto)
# tamanho tabela ASCII
n = len(alfabeto)

cifrada = ""

soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #estou usando TCP/IP
recebe = (host, porta)
soquete.bind(recebe)
soquete.listen(2)
 
print('\nSERVIDOR INICIADO...IP: ', host, 'PORTA: ', porta,' EM: ',datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))
 
while True:
    conexao, enderecoIP = soquete.accept()
    print('\nSERVIDOR ACESSADO PELO CLIENTE:', enderecoIP, 'EM: ',datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))
 
    while True:
        mensagem = conexao.recv(2048)
       
        if not mensagem:
            break
        print('\nIP CLIENTE:', enderecoIP)
        print('MENSAGEN RECEBIDA: ', mensagem.decode(),' - ',datetime.now().strftime('%H:%M:%S'))
        for letra in mensagem.decode():
             
    # achar no alfabeto a letra que esteja chave posições a frente
            indice = alfabeto.index(letra)
    
    # nova_letra = alfabeto[(indice + chave)%n]
            nova_letra = alfabeto[(indice + chave)%n]
    # substituir na mensagem a letra pela nova_letra
            cifrada = cifrada + nova_letra
            
        print ("mensagem cifrada", cifrada)
    
    print('CONEXÃO COM O CLIENTE FINALIZADA...', enderecoIP, ' EM: ',datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))
    conexao.close()
    