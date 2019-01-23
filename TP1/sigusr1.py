import signal
import sys

def handler(num_sig, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGTERM, signal.SIG_IGN)
signal.signal(signal.SIGUSR1 , handler)


while True:
    ...
