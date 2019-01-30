from socket import *
import sys
import datetime

def translate(dayOrMonth):
    if dayOrMonth == 'January':
        return 'Janvier'
    elif dayOrMonth == 'February':
        return 'Fevrier'
    elif dayOrMonth == 'March':
        return 'Mars' #pour tout les mois
    elif dayOrMonth == 'Monday':
        return 'Lundi'
    elif dayOrMonth == 'Tuesday':
        return 'Mardi'
    elif dayOrMonth == 'Wednesday':
        return 'Mercredi'
    elif dayOrMonth == 'Thursday':
        return 'Jeudi'
    elif dayOrMonth == 'Friday':
        return 'Vendredi'
    elif dayOrMonth == 'Saturday':
        return 'Mardi'
    elif dayOrMonth == 'Sunday':
        return 'Dimanche'
    else:
        return 'Error'

def calc_easter( year):
    print(year)
    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1
    return datetime.datetime(year, month, day)


now = datetime.datetime.now()
logfile = open('date.log' , 'w')
logfile.write(f"{str(now)} starting server\n")

TAILLE_TAMPON = 256
conn = socket(AF_INET, SOCK_DGRAM)
conn.bind(("" , int(sys.argv[1])))
logfile.write(str(now) + " listening on :" + sys.argv[1] + "\n")
while True:
    try:
        requete = conn.recvfrom(TAILLE_TAMPON)
        (mess , addrClient) = requete
        ipClient , portClient = addrClient
        mess = mess.decode()
        result = ""
        now = datetime.datetime.now()
        if mess == 'date' or mess == 'DATE':
            result = now.strftime("%d/%m/%Y")
        elif mess == 'jour' or mess == 'JOUR':
            result = translate(now.strftime('%A'))
        elif mess == 'mois' or mess == 'MOIS':
            result = translate(now.strftime('%B'))
        elif mess == 'heure' or mess == 'HEURE':
            result = now.strftime("%H:%M:%S")
        elif mess == 'PACQUES' or mess == 'pacques':
            result = calc_easter(int(now.strftime("%Y"))).strftime("%d/%m/%Y")
            print(result)
        elif mess == 'HELP' or mess == 'help':
            result = 'commande dispo : date , jour , mois , heure, pacques , ascension'

        elif mess == 'ASCENSION' or mess == 'ascension':
            result = calc_easter(int(now.strftime("%Y"))) + datetime.timedelta(days=39)
            result = result.strftime("%d/%m/%Y")
            print(result)
        else:
            result = "Aucune commande correspondante"
        logfile.write(f"{str(now)} Receive {mess} from {ipClient}:{portClient}\n")
        conn.sendto(result.encode(), addrClient)

    except KeyboardInterrupt :
        break

logfile.write(f"{str(now)} server stopped\n")
logfile.close()
conn.close()

