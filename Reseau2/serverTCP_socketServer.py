import sys
from socket import *
import threading
import os
import datetime

if len(sys.argv) != 3:
    print('Usage : {} <port> <repertoire>')
    sys.exit(1)

DOC_ROOT = os.path.realpath(sys.argv[2])

def traiter_client(socket_client):
    ligne = 'continue'
    while ligne != 'QUIT':
        wrapper = socket_client.makefile()
        ligne = wrapper.readline()[:-1]
        message = 'error'
        if ligne == 'DATE':
            message = datetime.datetime.now().strftime("%d/%m/%Y\n")
        if ligne[:3] == "GET":
            arg = ligne.split(" ")
            fileName = DOC_ROOT + '/' + arg[len(arg)-1]
            if not os.path.dirname(fileName).startswith(DOC_ROOT):
                message = f"FILE {fileName} NOT FOUND"
            else: #si on peut servir le fichier
                with open (arg[len(arg) -1] , 'r') as file:
                    message = ''
                    cpt = 0
                    for ligneFile in file:
                        cpt += 1
                        message += ligneFile
                        if len(arg) == 3 : #nblignes spécifié
                            if cpt >= int(arg[1]):
                                break
        socket_client.send(message.encode())




sock_server = socket() #TCP socket
sock_server.bind(("", int(sys.argv[1])))
sock_server.listen(4)
print("le serveur écoute sur le port " + sys.argv[1], file=sys.stderr)
print("son repertoire de base est " + DOC_ROOT, file=sys.stderr)
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
