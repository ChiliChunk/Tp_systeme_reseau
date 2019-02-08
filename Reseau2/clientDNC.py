from socket import *
import sys
import json
import threading
import time
if len(sys.argv) != 2:
    print('Usage : python clientDNC.py <port>')
    sys.exit(1)

sock_client= socket() #TCP socket
sock_client.connect(('localhost' , int(sys.argv[1])))

def envoyerMessageServeur(pseudo , message , ):
    strData = json.dumps([pseudo, message])
    sock_client.send(strData.encode())

def receiveMessage():
    while True:
        wrapper = sock_client.makefile()
        message = wrapper.readline()
        print(message)
        time.sleep(1)

pseudo = input('Entrez votre pseudo:\n')
envoyerMessageServeur(pseudo , "")
threading.Thread(target=receiveMessage)
while True:
    message = input("Votre message (ou QUIT):\n")
    if message == 'QUIT':
        break
    envoyerMessageServeur(pseudo , message)
