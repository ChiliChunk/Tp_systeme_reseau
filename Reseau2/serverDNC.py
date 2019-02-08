from socket import *
import sys
import threading
import json
import datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

pseudoAlreadyKnown = {} #key : pseudo , value : socket


def sendNewConnection(pseudo):
    print(f"nouvelle connextion de {pseudo}")
    for key in list(pseudoAlreadyKnown.keys()):
        if key != pseudo:
            pseudoAlreadyKnown[key].send(f"{datetime.datetime.now().strftime('%H:%M')} - Nouvelle connexion de {pseudo}".encode())

def sendMessage(pseudo , message):
    print(f"message {message} de {pseudo}")
    for key in list(pseudoAlreadyKnown.keys()):
        if key != pseudo:
            pseudoAlreadyKnown[key].send(f"{bcolors.HEADER}{pseudo}{bcolors.ENDC}:\n{message}".encode())

def traiter_client(socket_client): #CLIENT MESSAGE RECEIVED : [<pseudo>,<message>]
    wrapper = socket_client.makefile()
    package = wrapper.readline()
    print(package)
    if len(package)> 0:
        package = json.loads(package)
        if package[0] in list(pseudoAlreadyKnown.keys()): #send message to all client
            sendMessage(package[0] , package[1])
        else: #prevenir tout les clients d'une nouvelle connexion
            sendNewConnection(package[0])


if len(sys.argv) != 2:
    print('Usage : python serverDNC.py <port>')
    sys.exit(1)

sock_server = socket() #TCP socket
sock_server.bind(("", int(sys.argv[1])))
print(f"Server listening on port : {sys.argv[1]}")
sock_server.listen(10)

while True:
    try:
        sock_client , adr_client = sock_server.accept()
        print (f"Connexion de {adr_client}")
        threading.Thread(target=traiter_client , args=(sock_client,)).start()
    except KeyboardInterrupt:
        break
sock_server.shutdown(SHUT_RDWR)
print('\nshutting down')
for t in threading.enumerate():
    if t != threading.main_thread():
        t.join()
sys.exit(0)

