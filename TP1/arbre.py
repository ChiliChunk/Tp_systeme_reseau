import os

for i in range(4):
  if os.fork() != 0:
    print("PID = {}, i = {}".format(os.getpid(), i))

