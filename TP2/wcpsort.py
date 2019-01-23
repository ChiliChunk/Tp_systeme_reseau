import os
import sys

if int(sys.argv[1]) < 1 or int(sys.argv[1]) > 3:
    exit(1)

rd ,wr = os.pipe()
command =["python" , "wcp.py"]

for param in range (2,len(sys.argv)):
    command.append(sys.argv[param])
if os.fork() == 0:
    os.dup2(wr, 1)
    os.close(rd)
    os.execvp("python" , command)

os.wait()
os.dup2(rd , 0)
os.close(wr)
os.execlp("sort","sort", "-k", sys.argv[1])