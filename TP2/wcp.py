import sys
import os
listWC = ["wc"]
poubelle = os.open('/dev/null', os.O_CREAT|os.O_WRONLY|os.O_TRUNC)
os.dup2(poubelle, 2)
for index in range (1,len(sys.argv)):
    if os.fork() == 0:
        listWC.append(sys.argv[index])
        os.execvp("wc" , listWC)

echec = 0
for index in range (1, len(sys.argv)):
    (pid  , status) = os.wait()
    if status != 0:
        echec += 1

print (f"{echec} echecs")