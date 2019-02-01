import threading
import time
import random

# ressources partagées : cpt de voitures
# voie a sens unique (sémaphore)


cptVoiture = 0
cptVoitreOnSU = 0
sensSU = -1

mutexVoiture = threading.Semaphore()
mutexSU = threading.Semaphore()


def circuler(sens ,osef): # je donne un second argument parce que python me demande de donner un iterable dans args dans lors de la creation de thread et j'ai esséy de donner un tuple mais ca ne donctionne pas...
    global cptVoiture
    localNumVoiture = -1

    with mutexVoiture:
        cptVoiture += 1
        localNumVoiture = cptVoiture

    time.sleep(2)  # roule voies a double sens

    with mutexSU:
        print(f'Voiture {localNumVoiture} roulant dans le sens{sens} (SU)')
        time.sleep(.5)

    time.sleep(2)  # roule voies a double sens


def pere():
    for i in range(10):
        threading.Thread(target=circuler, args=(round(random.uniform(0, 1)) , 'osef')).start()


if __name__ == '__main__':
    pere()
