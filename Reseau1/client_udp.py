from socket import *
import sys

print(sys.argv)
conn = socket(AF_INET, SOCK_DGRAM)
rep = ""
TAILLE_TAMPON = 256
while rep != 'q':
    rep = input('Votre commande (q) pour quitter:\n')
    if rep != 'q':
        conn.sendto(rep.encode() , (sys.argv[1] , int(sys.argv[2])))
        data , _ = conn.recvfrom(TAILLE_TAMPON)
        print(data.decode())
conn.close()