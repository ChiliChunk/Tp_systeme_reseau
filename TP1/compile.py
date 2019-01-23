import sys
import os #os._exit()
strProgC = ""
stringDotO = ["gcc"]
for index in range(1, len(sys.argv)): #on parcour tout les .c
    currentfile = sys.argv[index]
    currentfile = currentfile[:-2]
    currentfile = currentfile + ".o"
    stringDotO.append(currentfile)
    if os.fork() == 0:
        print("fils" , os.getpid())
        print("pere" , os.getppid())
        nameFic = "error"+ str(index)
        ficError = os.open(nameFic, os.O_CREAT|os.O_WRONLY|os.O_TRUNC)
        os.dup2(ficError,2)
        os.execlp("gcc", "gcc" , "-c", sys.argv[index])

for index in range(1,len(sys.argv)):
    os.wait()



print(stringDotO)
os.execvp("gcc" , stringDotO)

#