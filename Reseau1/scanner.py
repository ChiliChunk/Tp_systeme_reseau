import sys
import os

os.execlp("nmap" , "nmap" , "-p-" ,sys.argv[1])