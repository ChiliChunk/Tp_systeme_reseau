import os
import codecs
rd , wr = os.pipe()
rd2 , wr2 = os.pipe()
if os.fork() == 0:
    os.close(rd)
    reponse = "continue"
    while reponse != "QUIT":
        reponse = input("Entrez un nom de fichier ou QUIT")
        if reponse == "QUIT":
            os.exit(1)
        os.write(wr, codecs.encode(reponse))
else:
    os.close(wr)
    reponse = os.read(rd , 256)
