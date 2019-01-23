import sys
import os
stringDotO = ["gcc"]
mapNamePid = []
for index in range(1, len(sys.argv)): #on parcour tout les .c
    currentfile = sys.argv[index]
    currentfile = currentfile[:-2]
    currentfile = currentfile + ".o"
    stringDotO.append(currentfile)
    pid = os.fork()
    if pid == 0:
        nameFic = "error"+ sys.argv[index][:-2]
        ficError = os.open(nameFic, os.O_CREAT|os.O_WRONLY|os.O_TRUNC)
        os.dup2(ficError,2)
        os.execlp("gcc", "gcc" , "-c", sys.argv[index])
    else:
        mapNamePid.append((sys.argv[index][:-2] , pid))
        
for index in range(1,len(sys.argv)):
    (pid, status) = os.wait()
    if status == 0:
        for j in range (0, len(mapNamePid)):
            if mapNamePid[j][1] == pid:
                os.remove("error"+mapNamePid[j][0])

os.execvp("gcc" , stringDotO)

#