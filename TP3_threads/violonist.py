import threading
import time
import random

violons = threading.Semaphore(2)
archer= threading.Semaphore(1)

def musicien(num ):
    with archer:
        with violons:
            print(f'Violinste {num} entrain de jouer')
            time.sleep(random.uniform(0,1))

def pere():
    for i in range(3):
        threading.Thread(target=musicien, args=(i,)).start()


if __name__ == '__main__':
    pere()



    """
    
        A REFAIRE AVEC LES VARIABLES CONDITIONS
        
    """