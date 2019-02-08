import os
rd , wr = os.pipe()
rd2 , wr2 = os.pipe()
reponse = ''

if os.fork() == 0:  #fils écrit dans wr et lit dans rd2
    os.close(rd)
    os.close(wr2)
    while reponse != 'QUIT':
        reponse = input("Entrez un nom de fichier ou QUIT: \n")
        if reponse != 'QUIT':
            os.write(wr , reponse.encode())
            servRep = os.read(rd2 , 256)
            print(servRep.decode())
        else:
            print('on termine')
            os._exit()
else: #pere écrit dans wr2 et lit dans rd
    os.close(wr)
    os.close(rd2)
    while True:
        reponse = os.read(rd , 256)
        reponse = reponse.decode()
        if reponse == 'QUIT':
            os.wait()
            break
        if os.path.exists(reponse):
            fd = os.open(reponse, os.O_CREAT | os.O_RDONLY | os.O_TRUNC)
            contFichier = os.read(fd , 256)
            os.write(wr2 , contFichier)
        else:
            os.write(wr2 , """Le fichier n'existe pas""".encode())
